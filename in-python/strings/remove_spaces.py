#!/usr/bin/python3

def remove_spaces(s):
    if len(s) == 0:
        return "String length is invalid."
    remove_spaces = s.strip()
    return remove_spaces

if __name__ == "__main__":
    input_string = input("Please enter the strings: ")
    output_string = remove_spaces(input_string)
    print(output_string)