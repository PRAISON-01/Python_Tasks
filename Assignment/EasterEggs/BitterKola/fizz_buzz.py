"""
fizz_buzz.py

collext number
if number % 3 == 0
    didsplay fizz
elif number % 5 == 0
    display  buzz
elif number % 3 == 0 and number % 5 = 0
    display FizzBuzz

"""
number = int(input("Enter Number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FIZZBUZZ")
elif number % 3 == 0:
    print("FIZZ")
elif number % 5 == 0:
    print("BUZZ")
else:
    print(number)

