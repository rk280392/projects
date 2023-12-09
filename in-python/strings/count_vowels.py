#!/usr/bin/python3

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
    return count

if __name__ == "__main__":
    input_string = input("Please enter the string: ")
    count = count_vowels(input_string)
    print(f"{input_string} has {count} of vowels")