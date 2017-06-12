# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random
the_number = random.randint(1,9)

user_input = raw_input("Guess a number between 1 and 9: ")

if user_input == the_number:
    print "Congrats, you didn't lose"

if user_input




