#!/usr/bin/env python3


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    n = 0
    x1, v1, x2, v2 = int(x1), int(v1), int(x2), int(v2)
    diff = lambda n, x1, v1, x2, v2: x1 + n * v1 - x2 - n * v2
    if (x1 <= x2 and v1 <= v2) or (x1 >= x2 and v1 >= v2):
        return 'NO'
    elif (x1 < x2 and v1 > v2) or (x1 > x2 and v1 < v2):
        while diff(n, x1, v1, x2, v2) < 0:
            n += 1
            if diff(n, x1, v1, x2, v2) == 0:
                return 'YES'
        return 'NO'


if __name__ == '__main__':
    arr = input('Please input x1, v1, x2, v2: ')
    result = kangaroo(arr)
    print(result)
