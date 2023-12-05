#!/usr/bin/python3

"""Find palindromes (letter palingrams) in a dictionary file."""

import load_dictionary

word_list = load_dictionary.load_file('dictionary.txt')
palindrom_list = []

for i in word_list:
    if len(i) > 1 and i[:] == i[::-1]:
        print(f"{i} is a palindrom")
        palindrom_list.append(i)
    else:
        print(f"{i} is not a palindrom")
print(f"list of palindroms: {palindrom_list}")
print(f"Number of palindroms: {len(palindrom_list)}")