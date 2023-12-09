#!/bin/python3

def separateNumbers(s):
    # Write your code here
    for i in range(1, len(s)):
        current_num = int(s[:i])
        print(f"current_num: {current_num}")
        remaining_str = s[i:]
        print(f"remaining_str: {remaining_str}")

        if remaining_str.startswith("0") or current_num >= int(remaining_str):
            continue

        valid = True
        while remaining_str:
            next_num = current_num + 1
            next_str = str(next_num)

            if not remaining_str.startswith(next_str):
                valid = False
                break

            current_num = next_num
            remaining_str = remaining_str[len(next_str):]

        if valid:
            return True

    return False
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()

        separateNumbers(s)

