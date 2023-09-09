from random import randint


def game():  # function initiates one game iteration
    while True:
        try:
            playerNumber = int(input('playerNumber: '))
            if playerNumber < 1 or playerNumber > 5:
                raise ValueError  # this will send it to the print message and back to the input option
            break
        except ValueError:
            print("Invalid integer. The number must be in the range of 1-5.")
    compNumber = randint(1, 5)
    if playerNumber == compNumber:
        print('Yep, you guessed it!\n')
        print(restart())
    else:
        print('May be next time :(\n')
        print(restart())


def restart():  # restart game iteration
    user_input = input("Would you like to play again? Type 'yes' or 'no'\n\n")

    if user_input.lower() == "no":  # Converts input to lowercase for comparison
        return False
    elif user_input.lower() == "yes":
        return True

    
def startGame():  # welcomefunction for a first start
    while True:
        user_input = input('Welcome to "Guess the number"!\n' + "Type 'go' to roll the die... \n\n")

        if user_input == "go":
            print(game())
        else:
            print('Bye, bye....')


startGame()
