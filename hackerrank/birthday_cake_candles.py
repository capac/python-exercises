#! /usr/bin/env python3

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort()
    return candles.count(candles[-1])


if __name__ == '__main__':
    s = input('Enter array: ')
    result = birthdayCakeCandles(s)
    print(result)
