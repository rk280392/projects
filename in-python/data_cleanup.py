#!/usr/bin/python3

"""Remove single-letter words from list"""
import load_dictionary

def main():
    """Remove single-letter words from list"""
    word_list = load_dictionary.load_file('dictionary.txt')
    filtered_list = [word for word in word_list if len(word) > 1]
    print(filtered_list)

if __name__ == "__main__":
    main()
