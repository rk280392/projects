#!/usr/bin/python3

"""Find palingrames (letter palingrams) in a dictionary file."""

import load_dictionary
def find_palingrams():
    """Find dictionary palingrams."""
    word_list = load_dictionary.load_file('dictionary.txt')
    palingram_list = []

    for word in word_list:
        length = len(word)
        rev_word = word[::-1]
        if length > 1:
            for i in range(length):
                if word[i:] == rev_word[:length-i] and rev_word[length-i:] in word_list:
                    palingram_list.append((word, rev_word[length-i:]))
                if word[:i] == rev_word[length-i:] and rev_word[:length-i] in word_list:
                    palingram_list.append((word, rev_word[:length-i]))
    return palingram_list

paligrams = find_palingrams()
sorted_palingram = sorted(paligrams)
for first, second in sorted_palingram:
    print(f"{first} {second}\n")


"""
Cprofile output
92187 function calls in 38.731 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   38.730   38.730 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.008    0.008 load_dictionary.py:12(load_file)
        1    0.004    0.004    0.007    0.007 load_dictionary.py:17(<listcomp>)
        1   38.718   38.718   38.730   38.730 palingrams.py:6(find_palingrams)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000   38.731   38.731 {built-in method builtins.exec}
    45333    0.003    0.000    0.003    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
     1506    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    45333    0.003    0.000    0.003    0.000 {method 'lower' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.001    0.001    0.001    0.001 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}

"""
