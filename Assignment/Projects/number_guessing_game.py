"""
import random

random_number = random.randint(1, 100)
while True:
    
    try:
         Ask user for input
        if number == random_number:
        print congratulatiojns you got the number
        break
     elif number > random_number:
        print 'too high'
        
     elif number < random_number:
        print 'too low'
    
    except valuError
        print enter a valid number


"""

import random 

random_number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100 => "))
        if guess ==random_number:
            print("congratulations yoou got the number")
            break
        elif guess  > random_number:
            print("Too high")
        elif guess < random_number:
            print("Too low")
    except ValueError:
        print("Please enter a valid number")
