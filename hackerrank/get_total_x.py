#! /usr/bin/env python

from numpy import gcd
from numpy import lcm


def getTotalX(arr_a, arr_b):
    count = 0
    lcm_val = lcm.reduce(arr_a)
    print(f'Lesser common multiple: {lcm_val}')
    gcd_val = gcd.reduce(arr_b)
    print(f'Greater common divisor: {gcd_val}')
    multiple = 0
    while multiple <= gcd_val:
        multiple += lcm_val
        if gcd_val % multiple == 0:
            print(f'Multiple of LCM: {multiple}')
            count += 1
    return count


if __name__ == '__main__':
    arr_a = [16, 32]  # input("Please input first array: ")
    arr_b = [1024, 2048]  # input("Please input second array: ")
    res = getTotalX(arr_a, arr_b)
    print(res)
