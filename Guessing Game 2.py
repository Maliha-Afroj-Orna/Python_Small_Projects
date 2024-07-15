import random


# main function
def guessing_game():
    print("************** Welcome to the Guessing Game ************")
    print(" Please choose the number between 1 to 100 ")

    random_number = random.randint(1, 100)

    n = 0

    while True:
        user_number = int(input('Guess a number between 1-100: '))
        n += 1

        if user_number > random_number:
            print("Your guess is too high")

        elif user_number < random_number:
            print("Your guess is too low")

        else:
            print(f"Your guess is correct! It took you {n} tries to guess the right number")
            print("Random number: ", random_number)
            break


    # play again?
    play_again = input("Do you want to play again (y/n): ")

    if play_again == 'y':
        guessing_game()
    else:
        print("Thank's for playing")


# main function call
guessing_game()

