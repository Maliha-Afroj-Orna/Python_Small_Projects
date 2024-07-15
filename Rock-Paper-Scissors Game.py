import random


# welcome message
def welcome_message():
    print('=====================================================')
    print('     Welcome to Rock, Paper, Scissors Game    ')
    print('=====================================================')
    print(' Instructions ')
    print(" 1. Choose 'rock' 'paper' or 'scissors' ")
    print(' 2. Rock beats Scissors, Scissors beats Paper, Paper beats Rock')
    print(' 3. Show the choice of User and Computer')
    print(' 4. Display the result of Win/Lose')
    print(' 5. Keep track of the scores')
    print(' 6. Ask the User if he wants to play again')
    print('========================================================')


welcome_message()

user_score = 0
computer_score = 0


# logic
while True:
    # user input
    user_choice = input("Choose Rock, Paper or Scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Choose from 'rock','paper' or 'scissors'")
        user_choice = input("Choose Rock, Paper or Scissors: ").lower()

    # computer input
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    #showing the choice of user and computer
    print(f"User's Choice = ({user_choice}), Computer's Choice =({computer_choice})")

    #logic
    if user_choice == computer_choice:
        print("It's a tie")
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print('Rock beats scissors! You Win')
            user_score += 1
        else:
            print('Paper beats rock! You Lose')
            computer_score += 1
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print('Scissors beats paper! You Win')
            user_score += 1
        else:
            print('Rock beats scissors! You Lose')
            computer_score += 1
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print('Paper beats rock! You Win')
            user_score += 1
        else:
            print('Scissors beats paper! You Lose')
            computer_score += 1

    # play again
    play_again = input('Play Again(y/n): ')
    if play_again.lower() != 'y':
        break

# total score
print(f"User Score: {user_score}, Computer Score: {computer_score}")
