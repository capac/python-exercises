from sys import argv


def rotate_char(k, char):
    if char.isalpha():
        p = len(argv[1])
        t = ord(argv[1][k % p].lower()) - ord('a')
        if char.islower():
            return chr(ord('a') + (ord(char) - ord('a') + t) % 26)
        else:
            return chr(ord('A') + (ord(char) - ord('A') + t) % 26)
    return char


def main():
    if len(argv) != 2:
        print("Only one argument!")
        return 1
    for i in range(len(argv[1])):
        if not argv[1][i].isalpha():
            print("Key can only contain letters!")
            return 1
    string = input("plaintext: ")
    cipher_text = []
    for k, char in enumerate(string):
        cipher_text.append(rotate_char(k, char))
    print("ciphertext: ", ''.join(cipher_text))


if __name__ == "__main__":
    main()

'''
:) encrypts "a" as "a" using "a" as keyword
:) encrypts "barfoo" as "caqgon" using "baz" as keyword
:) encrypts "BaRFoo" as "CaQGon" using "BaZ" as keyword
:) encrypts "BARFOO" as "CAQGON" using "BAZ" as keyword
:) encrypts "world!$?" as "xoqmd!$?" using "baz" as keyword
:) encrypts "hello, world!" as "iekmo, vprke!" using "baz" as keyword
:) handles lack of argv[1]
:) handles argc > 2
:) rejects "Hax0r2" as keyword
'''
