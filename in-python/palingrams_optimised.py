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


"""
Cprofile output
92158 function calls in 0.120 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.120    0.120 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.009    0.009 load_dictionary.py:12(load_file)
        1    0.004    0.004    0.007    0.007 load_dictionary.py:17(<listcomp>)
        1    0.108    0.108    0.119    0.119 palingrams_optimised.py:6(find_palingrams)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.120    0.120 {built-in method builtins.exec}
    45304    0.002    0.000    0.002    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
     1506    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    45333    0.003    0.000    0.003    0.000 {method 'lower' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.002    0.002    0.002    0.002 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}

Sets are much faster than lists when using the in keyword. Sets use a hashtable for veryfast lookups. 
With hashing, strings of text are converted to unique numbers that are much smaller than the 
referenced text and much more efficient to search. With a list, on the other hand, you have 
to do a linear search through each item.

A downside to using sets is that the order of the items in the set isn’t controllable and
duplicate values aren’t allowed. With lists, the order is preserved and duplicates are
allowed, but lookups take longer.

"""
