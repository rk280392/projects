#!/usr/bin/python3

def check_palindrome(s):
    if len(s) <= 0:
        return "String length is invalid"
    if s == s[::-1]:
        return True
    
if __name__ == "__main__" :
    input_string = input("Please enter the string to check palindrome: ")
    check_palindrome(input_string)
    if check_palindrome :
        print(f"The string {input_string} is a palndrome.")
    else:
        print(f"The string {input_string} is not a palndrome.")