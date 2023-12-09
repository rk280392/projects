#!/usr/bin/python3

def convert_to_lower(s):
    if len(s) == 0:
        return "String length is invalid"
    return s.upper()

if __name__ == "__main__":
    input_string = input("Please enter the string: ")
    output_string = convert_to_lower(input_string)
    print(output_string)