import random

def get_random_number():
    return random.randint(1, 100)

def get_swap(first_number, second_number):
    if first_number > second_number:
        return first_number, second_number
    return second_number, first_number

#count = 1
#correct = 0
#wrong_count = 0
#
#loading = True
#while loading:
#    first_number = get_random_number()
#    second_number = get_random_number()
#
#    first, second = get_swap(first_number, second_number)
#    difference = first - second
#
#    try:
#        number = int(input(f"\nQuestion {count}/10: {first} - {second} => "))
#
#        if number == difference:
#            print("Correct!")
#            correct += 1
#            count += 1  
#        else:
#            print("Incorrect. Let's try one more time.")
#            number = int(input(f"Try again: {first} - {second} => "))
#            
#            if number == difference:
#                print("Correct on second try!")
#                correct += 1 
#            else:
#                print(f"Wrong. The correct answer was {difference}.")
#                wrong_count += 1
#            
#            count += 1
#
#    except ValueError:
#        print("Please enter a valid whole number")
#        count += 1 
#
#    if count > 10:
#        loading = False
#
#print("\n============================")
#print("  Results from 10 Questions ")
#print("------------------------------")
#print(f"Correct Answers : {correct}")
#print(f"Wrong Answers   : {wrong_count}")
