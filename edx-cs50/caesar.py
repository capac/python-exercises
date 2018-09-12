from sys import argv


def rotate_char(char):
    if char.isalpha():
        if char.islower():
            return chr(ord('a') + (ord(char) - ord('a') + int(argv[1])) % 26)
        else:
            return chr(ord('A') + (ord(char) - ord('A') + int(argv[1])) % 26)
    return char


def main():
    if len(argv) == 2:
        string = input("plaintext: ")
        cipher_text = []
        for char in string:
            cipher_text.append(rotate_char(char))
        print("ciphertext: ", ''.join(cipher_text))
    else:
        print("Only one argument!")


if __name__ == "__main__":
    main()

'''
:) encrypts "a" as "b" using 1 as key
:) encrypts "barfoo" as "yxocll" using 23 as key
:) encrypts "BARFOO" as "EDUIRR" using 3 as key
:) encrypts "BaRFoo" as "FeVJss" using 4 as key
:) encrypts "barfoo" as "onesbb" using 65 as key
:) encrypts "world, say hello!" as "iadxp, emk tqxxa!" using 12 as key
:) handles lack of argv[1]
'''
