#define _POSIX_C_SOURCE 200809L
#include <errno.h>
#include <math.h>
#include <omp.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static double now_seconds(void) {
    struct timespec ts;
    if (clock_gettime(CLOCK_MONOTONIC, &ts) != 0) {
        perror("clock_gettime");
        exit(2);
    }
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

static int compare_double(const void *left, const void *right) {
    const double a = *(const double *)left;
    const double b = *(const double *)right;
    return (a > b) - (a < b);
}

int main(int argc, char **argv) {
    int threads = 1;
    size_t elements = 16u * 1024u * 1024u;
    int repetitions = 8;

    if (argc > 1) {
        threads = atoi(argv[1]);
    }
    if (argc > 2) {
        elements = (size_t)strtoull(argv[2], NULL, 10);
    }
    if (argc > 3) {
        repetitions = atoi(argv[3]);
    }
    if (threads < 1 || elements < 1024 || repetitions < 3) {
        fprintf(stderr, "invalid arguments\n");
        return 2;
    }

    omp_set_dynamic(0);
    omp_set_num_threads(threads);

    double *a = NULL;
    double *b = NULL;
    double *c = NULL;
    const size_t bytes_per_array = elements * sizeof(double);
    if (posix_memalign((void **)&a, 64, bytes_per_array) != 0 ||
        posix_memalign((void **)&b, 64, bytes_per_array) != 0 ||
        posix_memalign((void **)&c, 64, bytes_per_array) != 0) {
        fprintf(stderr, "allocation failed for %zu bytes per array: %s\n", bytes_per_array, strerror(errno));
        free(a);
        free(b);
        free(c);
        return 3;
    }

    #pragma omp parallel for schedule(static)
    for (size_t i = 0; i < elements; ++i) {
        a[i] = 1.0 + (double)(i & 7u);
        b[i] = 2.0 + (double)(i & 3u);
        c[i] = 0.0;
    }

    double *rates = calloc((size_t)repetitions, sizeof(double));
    if (!rates) {
        fprintf(stderr, "rate allocation failed\n");
        free(a);
        free(b);
        free(c);
        return 3;
    }

    const double scalar = 3.0;
    const double moved_bytes = 3.0 * (double)bytes_per_array;
    for (int repetition = 0; repetition < repetitions; ++repetition) {
        const double started = now_seconds();
        #pragma omp parallel for schedule(static)
        for (size_t i = 0; i < elements; ++i) {
            c[i] = a[i] + scalar * b[i];
        }
        const double elapsed = now_seconds() - started;
        rates[repetition] = moved_bytes / elapsed / 1e9;
    }

    qsort(rates, (size_t)repetitions, sizeof(double), compare_double);
    const double median = (repetitions % 2)
        ? rates[repetitions / 2]
        : 0.5 * (rates[repetitions / 2 - 1] + rates[repetitions / 2]);
    const double best = rates[repetitions - 1];

    double checksum = 0.0;
    for (size_t i = 0; i < elements; i += 4096) {
        checksum += c[i];
    }

    printf("{\"threads\":%d,\"elements\":%zu,\"array_bytes\":%zu,\"repetitions\":%d,"
           "\"median_gbps\":%.6f,\"best_gbps\":%.6f,\"checksum\":%.6f}\n",
           threads, elements, bytes_per_array, repetitions, median, best, checksum);

    free(rates);
    free(a);
    free(b);
    free(c);
    return 0;
}
