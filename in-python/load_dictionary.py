#!/usr/bin/python3
"""Load a text file as a list.
Arguments:
-text file name (and directory path, if needed)
Exceptions:-IOError if filename not found.
Returns:
-A list of all words in a text file in lower case.
Requires-import sys
"""
import sys

def load_file(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            texts = in_file.read().strip().split('\n')
            lowercase_texts = [x.lower() for x in texts]
            return lowercase_texts
    except IOError as e:
        print(f"{e}\n Error Opening {file}. Terminating the program.", file=sys.stderr)
        sys.exit(1)
    
