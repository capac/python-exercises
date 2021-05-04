#! /usr/bin/env python

import time
from contextlib import contextmanager


class ExecutionTime():
    def __init__(self):
        self.tm = 0

    def __enter__(self):
        self.tm = time.time()
        return self

    def __exit__(self, exc_type, xec_val, exc_tb):
        self.diff = time.time() - self.tm
        print(f'Time elapsed: {round(self.diff, 2)} seconds')


@contextmanager
def elapsed_time(x):
    try:
        t0 = time.time()
        yield show_average(x)
    finally:
        print(f'Time elapsed: {round(time.time() - t0, 2)} seconds')


def show_average(x):
    time.sleep(1)
    print(round(sum(x)/len(x), 3))


# with ExecutionTime() as exc:
#     show_average([13, 27, 53])

with elapsed_time([31, 72, 43]) as elaps:
    print('Done!')
