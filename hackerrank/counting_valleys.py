#! /usr/bin/env python3


def countingValleys(path):
    # Write your code here
    units_list = []
    cum_sum = 0
    counter = 0
    for item in path:
        if item == 'U':
            units_list.append(1)
        elif item == 'D':
            units_list.append(-1)
    for item in units_list:
        cum_sum += int(item)
        if cum_sum == 0 and item > 0:
            counter += 1
    return counter


if __name__ == '__main__':
    arr = input('Please provide an array of uphill and downhill units: ')
    result = countingValleys(arr)
    print(result)
