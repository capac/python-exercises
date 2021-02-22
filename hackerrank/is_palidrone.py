#! /usr/bin/env python3


def is_palidrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-1 - i]:
            return False
        else:
            return True


if __name__ == '__main__':
    s = input('Please provide possible palidrome: ')
    result = is_palidrome(s)
    print(result)
