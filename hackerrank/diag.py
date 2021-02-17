#! /usr/bin/python3

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.


def diagonalDifference(arr):
    # Write your code here
    sum_primary_diag = 0
    sum_secondary_diag = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                sum_primary_diag += arr[i][j]
                print(f'i, j, sum_primary_diag: {i, j, sum_primary_diag}')
            if i == n - j - 1:
                sum_secondary_diag += arr[i][j]
                print(f'i, j, sum_secondary_diag: {i, j, sum_secondary_diag}')
    return abs(sum_primary_diag - sum_secondary_diag)


if __name__ == '__main__':
    arr = [[11, 2, 4, 6], [2, 4, 5, 6], [-2, 10, 8, -12]]
    result = diagonalDifference(arr)
    print(f'result: {result}')
