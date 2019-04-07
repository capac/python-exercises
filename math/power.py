import sys
powers_dict = {}


def exponential(number, exponent):
    power = 1
    for i, _ in enumerate(range(1, exponent + 1)):
        power = power * number
        powers_dict[i] = power
    return powers_dict


if __name__ == '__main__':
    base = int(input('Choose the base: '))
    exp = int(input('Choose the exponent: '))
    if base <= 0 or exp <= 0:
        print('Base or exponent must be positive')
        sys.exit()
    for i, j in exponential(base, exp).items():
        print(f'The power of {base} to the {i + 1} is {j}')
