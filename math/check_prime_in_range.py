import numpy as np

def check_prime(y):
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:
        print(y, 'is prime')

if __name__ == "__main__":
    number = int(input('Choose the number of random numbers between 1 and 100: '))
    randint_arr = np.random.randint(1, 100, size=number)
    pretty_arr = ', '.join([str(k) for k in randint_arr])+'.'
    print('Choosing '+str(number)+' random numbers between 1 and 100: ', pretty_arr)
    for randint in randint_arr:
        check_prime(randint)
