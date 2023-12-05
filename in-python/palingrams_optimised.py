#!/usr/bin/python3

"""Find palingrames (letter palingrams) in a dictionary file."""

import load_dictionary
def find_palingrams():
    """Find dictionary palingrams."""
    word_list = load_dictionary.load_file('dictionary.txt')
    palingram_list = []
    words = set(word_list)
    for word in words:
        length = len(word)
        rev_word = word[::-1]
        if length > 1:
            for i in range(length):
                if word[i:] == rev_word[:length-i] and rev_word[length-i:] in words:
                    palingram_list.append((word, rev_word[length-i:]))
                if word[:i] == rev_word[length-i:] and rev_word[:length-i] in words:
                    palingram_list.append((rev_word[:length-i], word))
    return palingram_list
paligrams = find_palingrams()
sorted_palingram = sorted(paligrams)
for first, second in sorted_palingram:
    print(f"{first} {second}\n")
