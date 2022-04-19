# !/usr/bin/env python3
# Created by: Jedidiah
# Created on: April 18 2022
# This program is random number
# guesser using a try statement

import random
random.Random


def main():
    # this function uses a try statement
    # this function uses a try statement

    try:
        # input
        guess = int(input("Guess a number from 0 to 9! "))
        # process
        n = random.randint(0, 1)
        # output
        if guess == n:
            print("You guessed correctly!") 
        if guess != n: 
            print("You guessed incorrectly the correct number was {}!".format(n))
    except ValueError:
        print ("that is not an integer")
    else:
        print("")
    finally:
        print ("thanks for using this program")


if __name__ == "__main__":
    main()

