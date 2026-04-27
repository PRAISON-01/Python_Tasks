"""
three_digit_checker.py

colect number 

while true

    if number > 99 and number <= 999
        print number is a three digit number
        break


    else
        priint Enter a 3 digit integer
"""
number = int(input("Enter Number: "))

while True:
    if number > 99  and number <= 999:
        print(f"{number} is a Three Digit Number")
        break
    else:
        number = int(input("Enter a 3 digit integer: "))
