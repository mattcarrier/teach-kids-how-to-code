#!/usr/bin/env python

# imports for required libraries
from random import randint  # random number generator
from sys import stdin       # access to stdin to read input from player


def play_again():
    """
    Ask the player whether they want to 'play again'.

    :return: True if they do, False otherwise
    """

    # ask if the player would like to play again
    #
    # a general unix principal is that a capitalized letter is a default,
    #   so the player would not have to type in 'Y' to continue, they
    #   would only need to press the 'enter' key
    print("\nWould you like to play again? [Y/n]")

    # if the player's answer starts with 'n' then stop playing
    #
    # we need to strip the newline and lowercase the whole
    #   string, and then check if it starts with lowercase 'n'
    response = stdin.readline().strip().lower()
    if response.startswith("n"):
        return False
    # not response will return true if response is empty (default)
    elif not response or response.startswith("y"):
        return True

    # if response is not empty and doesn't start with 'y' or 'n' then
    #   ask the player again because we don't understand their response
    #
    # this is called 'recursion' when a function calls itself
    return play_again()


# loop until the player ends the game
while True:
    guess = None
    while not guess:
        # ask the player to guess a number from 1 to 10
        print("Guess a number from 1 - 10:")

        # read the number guessed from the player into the variable 'guess'
        #
        # since stdin.readline() returns a string that ends in 'newline' we
        #   need to strip the 'newline' and 'cast' the string to a number so
        #   we can compare the player's number to the random number later on
        try:
            guess = int(stdin.readline().strip())
        except:
            print('what you entered is not an integer')

    # pick a random number from 1 - 10 into the variable random
    random = randint(1, 10)

    # print out results
    #   - '\n' will print out a newline for readability
    #   - format will replace the '{}' with the passed-in variable
    print("\nNumber Guessed: {}".format(guess))
    print("Number Picked: {}".format(random))
    print("You Guessed Right!" if guess == random else "You Guessed Wrong :-(")

    # ask player if they would like to play again
    if not play_again():
        break
