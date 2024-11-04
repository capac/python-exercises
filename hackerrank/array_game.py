# We have an array of integers and need to determine the number of moves
# required to make all elements equal. In each move, we can increment all
# but one element by 1.

# Observations

# Instead of thinking about incrementing all but one element, we can
# reframe the problem. Instead of adding to most elements, it's equivalent
# to decreasing one element at a time. The total number of moves required
# to make all elements equal is the sum of the differences between each
# element and the minimum element in the array.

# Mathematical Formulation

# If we define:

#     min_element: min_element as the smallest number in the array.
#     numbers = [a_1, a_2,..., a_n]

# Then the number of moves required is:
# Sum(a_i − min_element)

# where we sum over all elements a_i in the array.


def countMoves(numbers):
    # Find the minimum element in the array
    min_element = min(numbers)

    # Compute the total number of moves required
    moves = sum(num - min_element for num in numbers)

    return moves


if __name__ == '__main__':
    # Example test case
    numbers = [3, 4, 6, 6, 3]
    print(countMoves(numbers))  # Output: 7
