#! /usr/bin/env python3


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counter = 0
    count_socks = [ar.count(i) for i in set(ar)]
    for sock in count_socks:
        if sock % 2 == 0:
            pairs = sock // 2
            counter += pairs
        elif (sock - 1) % 2 == 0 and sock > 1:
            pairs = (sock - 1) // 2
            counter += pairs
    return counter


if __name__ == '__main__':
    ar = input('Please provide an array of integers: ')
    n = len(ar)
    result = sockMerchant(n, ar)
    print(result)
