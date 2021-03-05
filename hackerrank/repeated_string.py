#! /usr/bin/env python3


def repeated_string(s, k):
    # works fine for small k
    how_many_chars = k // s.count('a')
    first_k_charcters = []
    for _ in range(how_many_chars):
        first_k_charcters.extend(s)
    first_k_charcters = ''.join(first_k_charcters)
    return first_k_charcters[:k].count('a')


if __name__ == '__main__':
    s = input('Please input string: ')
    k = int(input('Please input the first k characters of the string: '))
    res = repeated_string(s, k)
    print(f'Result: {res}')
