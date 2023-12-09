#!/usr/bin/python3

def capitalize_string(s):
    if len(s) == 0:
        return "String length is invalid"
    list_string = s.split()
    capital_string_list = []
    for i in list_string:
        capital_string_list.append(i.capitalize())
    return (' ').join(capital_string_list)


if __name__ == "__main__":
    input_string = input("Please enter the string: ")
    output_string = capitalize_string(input_string)
    print(output_string)