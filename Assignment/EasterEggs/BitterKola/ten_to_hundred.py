"""
ten_to_hundred.py

collect number
if number >= 10 and number <= 100
    print Number is between 10 and 100
else 
    print Number is 'Not' 10 and 100s
"""

while True:
    number = int (input('Enter Number Between 1 and 100: '))
    if number >= 10 and number <= 100:
        print("Number is between 10 and 100")
        break
    else:
        print("Number is 'NOT' between 10 and 100")
