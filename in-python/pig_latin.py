#!/usr/bin/python3
"""Create pig latin equivalent from words."""

import sys

def main():
    """Take a word as input and create pig latin equivalent."""
    vowels = 'aeiou'

    while True:
        word = input("Please enter the word: ").strip()
        if word[0] in vowels:
            new_word = word + 'way'
        else:
            new_word = word[1:] + word[0] + 'ay'
        print(f"Pig Latin word: {new_word}\n", file=sys.stderr)
        try_again = input("Do you want to try again? (Press enter else press 'n' to exit): ")
        if try_again.lower() == 'n':
            sys.exit()

if __name__ == "__main__":
    main()
    