#! /usr/bin/env python


def is_num_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        print(f'Reverse number: {reversed_num}')
        temp = temp // 10
        print(f'Temp number: {temp}')

    if num == reversed_num:
        return num
    else:
        return False


if __name__ == '__main__':
    num = int(input('Please input number: '))
    res = is_num_palindrome(num)
    print(f'Result: {res}')
