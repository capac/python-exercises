#! /usr/bin/env python3

# Python3 implementation of the approach
# https://www.geeksforgeeks.org/maximum-non-attacking-knights-that-can-be-placed-on-an-nm-chessboard/

# Function to return the maximum number of
# knights that can be placed on the given
# chessboard such that no two
# knights attack each other


def max_knight(n, m):
    # Check for corner case #1
    # If row or column is 1
    if (m == 1 or n == 1):
        # If yes, then simply print total blocks
        # which will be the max of row or column
        return max(m, n)

    # Check for corner case #2
    # If row or column is 2
    elif (m == 2 or n == 2):
        # If yes, then simply calculate
        # consecutive 2 rows or columns
        c = 0
        c = (max(m, n) // 4) * 4
        if (max(m, n) % 4 == 1):
            c += 2
        elif (max(m, n) % 4 > 1):
            c += 4
        return c

    # For general case, just print the half of total blocks
    else:
        return (((m * n) + 1) // 2)


# Driver code
if __name__ == "__main__":
    n, m = 8, 8
    print(max_knight(n, m))
