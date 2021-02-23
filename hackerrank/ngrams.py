#! /usr/bin/env python


def create_ngrams(string, num):
    arr = list(string)
    num = int(num)
    return list(zip(*[arr[i:] for i in range(num)]))


if __name__ == '__main__':
    string = input('Please provide string: ')
    num = input('Please provide n-gram length: ')
    res = create_ngrams(string, num)
    print(res)
