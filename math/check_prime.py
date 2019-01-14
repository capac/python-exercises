import math
import numpy

input_number = input('Input a number to determine if it is prime: ')

def check_prime(input_number):
    number_float = numpy.float32(input_number)
    sqrt_number = math.sqrt(number_float)
    print('int(sqrt_number) + 1 = ', int(sqrt_number)+1)
    for i in range(2, int(sqrt_number) + 1):
        print(number_float,'/',i,' = ', '{:.4f}'.format(number_float / i))
        if (number_float / i).is_integer():
            return False
    return True

if __name__ == '__main__':
    print('check_prime('+str(input_number)+') = ', check_prime(input_number))
