#!/usr/bin/python3

from random import choice

def main():
    options_list = ["rock", "paper", "scissors"]
    computer_choice = choice(options_list)
    user_choice = ''
    while ( user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissor'):
        user_choice = input("Choose one option: rock, paper, scissor: ").lower()
    print(user_choice)
        
    winner = ''
    if user_choice == computer_choice:
        winner = 'Tie'
    elif user_choice == "rock" and computer_choice == "paper":
        winner = 'Computer'
    elif computer_choice == 'rock' and user_choice == 'scissors':
        winner = 'Computer'
    elif computer_choice == 'scissors' and user_choice == 'paper':
        winner = 'Computer'
    else:
        winner = 'User'

    if winner == 'Tie':
        print('We both chose', computer_choice + ', play again.')
    else:
        print(winner, 'won. The computer chose', computer_choice + '.')

if __name__ == "__main__":
    main()