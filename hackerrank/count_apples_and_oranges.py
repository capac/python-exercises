#! /usr/bin/env python3


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_from_a = [apple + a for apple in apples]
    oranges_from_b = [orange + b for orange in oranges]
    print(sum((s <= apple and apple <= t) for apple in apples_from_a))
    print(sum((s <= orange and orange <= t) for orange in oranges_from_b))


if __name__ == '__main__':
    s = input('''Distance from apple tree to Sam's house: ''')
    t = input('''Distance from orange tree to Sam's house: ''')
    a = input('''Distance of apple tree: ''')
    b = input('''Distance of orange tree: ''')
    apples = input('Please input array for apples: ')
    oranges = input('Please input array for oranges: ')
    countApplesAndOranges(s, t, a, b, apples, oranges)
