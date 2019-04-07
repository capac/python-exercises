import sys
powers_dict = {}


def exponential(number, exponent):
    power = 1
    counter = 0
    while exponent > 0:
        power = power * number
        powers_dict[counter] = power
        exponent -= 1
        counter += 1
    return powers_dict


if __name__ == '__main__':
    base = int(input('Choose the base: '))
    exp = int(input('Choose the exponent: '))
    if base <= 0 or exp <= 0:
        print('Base or exponent must be positive')
        sys.exit()
    for i, j in exponential(base, exp).items():
        print(f'The power of {base} to the {i + 1} is {j}')
