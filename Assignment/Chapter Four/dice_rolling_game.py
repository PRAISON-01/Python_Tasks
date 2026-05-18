"""
infinite(loop)
Ask user for input
    if useer says yes
        generate two random numbers
        print them
    if user enters no
        print thank you message
        terminate
    else
        print invalid choice



"""

import random

count = 0
while True:

    choice = input("Roll the dice (yes/no) => ").lower()

    if choice == 'yes':
        die_one = random.randint(1, 6)
        die_two = random.randint(1, 6)
        print(f'First Die: {die_one}, Second Die: {die_two}')
    elif choice == 'no':
        print("Goodbye Thanks for playing")
        break
    else:
        print('Invalid choice!')
