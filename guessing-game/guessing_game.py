#!/usr/bin/env python

# imports for needed libraries
from random import randint
from sys import stdin

while True:
    # output the guessing statement
    print("Guess a number from 1 - 10:")

    # read the number guessed from the user into the variable guess
    guess = int(stdin.readline().strip())

    # pick a random number from 1 - 10
    random = randint(1, 10)

    # print out results
    print("\nNumber Guessed: {}".format(guess))
    print("Number Picked: {}".format(random))
    print("You Guessed Right!" if guess == random else "You Guessed Wrong :-(")

    # ask if they would like to play again
    print("\nWould you like to play again? [Y/n]")

    # if their answer starts with 'n' then stop playing
    if stdin.readline().strip().lower().startswith("n"):
        break
