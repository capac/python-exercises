#! /usr/bin/env python

import random


def bernoulli_trial(p: float) -> int:
    return 1 if random.random() < p else 0


def binomial(n: int, p: float) -> int:
    return sum(bernoulli_trial(p) for _ in range(0, n))


if __name__ == "__main__":
    n = int(input('Enter a value for n: '))
    p = float(input('Enter a value for p: '))
    print(f'Binomial of n = {n} and p = {p} is {binomial(n, p)}.')
