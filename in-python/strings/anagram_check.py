#!/usr/bin/python3

def anagram_check(s):
    if len(s[0]) != len(s[1]):
        return False
     
    for i in range(len(s[0])):
        if s[0][i] in s[1]:
            return True
    return False

if __name__=="__main__":
    input_string_list = input("Please enter two strings to check the anagram: ").split()
    while True:
        if len(input_string_list) == 2:
            break
        else:
            input_string_list = input("\ninvalid number of strings. \nPlease enter two strings to check the anagram: ").split()
    if anagram_check(input_string_list) :
        print("strings are anagrams")
    else:
        print("strings are not anagrams")