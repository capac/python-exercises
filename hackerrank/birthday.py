#! /usr/bin/env python


def birthday(s, d, m):
    number = 0
    for i in range(len(s)-m+1):
        sum_ = 0
        for j in range(m):
            sum_ += s[i+j]
            print(f'i, j, sum_: {i, j, sum_}')
        if sum_ == d:
            number += 1
    return number


if __name__ == "__main__":
    arr = [int(s) for s in list(input('Please input array: '))]
    d = int(input('Sum: '))
    m = int(input('Length: '))
    res = birthday(arr, d, m)
    print(f'Result: {res}')
