collatz_numbers = []


def collatz(n):
    if n == 1:
        collatz_numbers.append(n)
        return collatz_numbers
    elif n % 2 == 0:
        collatz_numbers.append(n)
        return collatz(int(n / 2))
    else:
        collatz_numbers.append(n)
        return collatz(int(3 * n + 1))


def collatz_num(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz_num(n / 2)
    else:
        return 1 + collatz_num(3 * n + 1)


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    # len_collatz = len(collatz(number))
    # collatz_numbers.clear()
    print("Collatz of {0:d} is {1:d} and the numbers are: {2!a}".format(
        number, collatz_num(number), collatz(number)))
