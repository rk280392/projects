#!/usr/bin/python3

"""Map letters from string into dictionary & print bar chart of frequency."""

from collections import defaultdict
import pprint
import sys

def main():
""" defaultdict module lets you build dictionary keys on the fly."""
    text = input("Please enter your text below: \n")
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    my_dict = defaultdict(list)
    for c in text:
        c = c.lower()
        if c in alphabets:
            my_dict[c].append(c)
    print()
    print(f"text = {text}\n",file=sys.stderr)
    pprint.pprint(my_dict)
if __name__ == "__main__":
    main()
