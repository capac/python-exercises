#!/bin/python3

#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

# Find the Smallest Missing Positive Integer

# Given an unsorted array of integers, find the smallest positive integer
# not present in the array in O(n) time and O(1) extra space.

# Example

# Input

# orderNumbers = [3, 4, -1, 1]

# Output

# 2

# Explanation

# We want the smallest positive missing integer.

# Start with [3, 4, -1, 1]
# - i=0: value 3 ⇒ swap with index 2 ⇒ [-1, 4, 3, 1]
# - i=0: value -1 is out of range ⇒ move on
# - i=1: value 4 ⇒ swap with index 3 ⇒ [-1, 1, 3, 4]
# - i=1: value 1 ⇒ swap with index 0 ⇒ [1, -1, 3, 4]
# - now 1 at index 0, 3 at 2, 4 at 3; -1 remains at index 1

# Scan from index 0:
# index 0 has 1 (correct), index 1 has -1 (not 2) ⇒ missing positive is 2

# Input Format

# An integer n on the first line, where 0 ≤ n ≤ 1000.
# The next n lines contains an integer representing orderNumbers[i].

# Example

# 4
# 3
# 4
# -1
# 1

# here 4 is the length of array, followed by the elements of array
# on each line.

# Constraints

#     0 <= orderNumbers.length <= 1000
#     -10^9 <= orderNumbers[i] <= 10^9 for all 0 <= i < orderNumbers.length
#     Duplicates are allowed in orderNumbers
#     Negative numbers and zero are allowed in orderNumbers

# Output Format

# A single integer denoting the smallest positive order number (≥1)
# that does not appear in the input array.


def findSmallestMissingPositive(orderNumbers):
    n = len(orderNumbers)
    a = orderNumbers
    if n == 0:
        return 1

    i = 0
    while i < n:
        x = a[i]
        if 1 <= x <= n and a[x-1] != x:
            a[i], a[x-1] = a[x-1], a[i]
        else:
            i += 1

    for i in range(n):
        if a[i] != i+1:
            return i+1

    return n+1


if __name__ == '__main__':
    orderNumbers = [
        [3, 4, -1, 1],
        [9, 5, 2, 1],
        [1, 3, 6, 8],
        [1, 2, 2, 4]
        ]
    for order_num in orderNumbers:
        result = findSmallestMissingPositive(order_num)
        print(result)
