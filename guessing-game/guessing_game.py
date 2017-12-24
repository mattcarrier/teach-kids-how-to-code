#!/usr/bin/env python

# imports for required libraries
from random import randint  # random number generator
from sys import stdin       # access to stdin to read input from player

# loop until the player ends the game
while True:
    # ask the player to guess a number from 1 to 10
    print("Guess a number from 1 - 10:")

    # read the number guessed from the player into the variable 'guess'
    #
    # since stdin.readline() returns a string that ends in 'newline' we
    #   need to strip the 'newline' and 'cast' the string to a number so
    #   we can compare the player's number to the random number later on
    guess = int(stdin.readline().strip())

    # pick a random number from 1 - 10 into the variable random
    random = randint(1, 10)

    # print out results
    #   - '\n' will print out a newline for readability
    #   - format will replace the '{}' with the passed-in variable
    print("\nNumber Guessed: {}".format(guess))
    print("Number Picked: {}".format(random))
    print("You Guessed Right!" if guess == random else "You Guessed Wrong :-(")

    # ask if the player would like to play again
    print("\nWould you like to play again? [Y/n]")

    # if the player's answer starts with 'n' then stop playing
    #
    # like above we need to strip the newline, then we're lower casing
    #   the whole string and checking if it starts with lowercase 'n'
    if stdin.readline().strip().lower().startswith("n"):
        break   # break stops the 'while' loop above
