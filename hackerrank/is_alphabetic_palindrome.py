#!/usr/bin/env python

#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#


# Check Palindrome by Filtering Non-Letters

# Given a string containing letters, digits, and symbols, determine if it
# reads the same forwards and backwards when considering only alphabetic
# characters (case-insensitive).

# Example

# Input

# code = A1b2B!a

# Output

# 1

# Explanation

# - Step 1: Extract only letters → ['A','b','B','a']
# - Step 2: Convert to lowercase → ['a','b','b','a']
# - Step 3: Compare sequence forward and backward: 'abba' == 'abba' → true

# Input Format

# A string code containing letters (A–Z, a–z), digits (0–9), and symbols

# Constraints

# 0 <= code.length <= 1000
# For all 0 <= i < code.length: 33 <= ASCII(code[i]) <= 126
# code contains only printable ASCII characters (letters, digits, symbols)


def isAlphabeticPalindrome(code):
    char_list = [char.lower() for char in code if char.isalpha()]
    print(f'char_list: {''.join(char_list)}')
    print(f'''reversed_char_list: {''.join(reversed(char_list))}''')
    return int(char_list[::-1] == char_list)


if __name__ == '__main__':
    code = 'QaB2Cba1d£2wq'
    result = isAlphabeticPalindrome(code)
    print(int(result))
