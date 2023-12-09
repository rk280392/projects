#!/usr/bin/python3

def reverse_string(s):
    if len(s) <= 0:
        return "string length is invalid"
    reverse_string = s[::-1]
    return reverse_string

if __name__ == "__main__":
    input_string = input("Please enter the string to reverse: ")
    output_string = reverse_string(input_string)
    print(output_string)