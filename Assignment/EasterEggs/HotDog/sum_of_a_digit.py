"""
sum_of_a_digit.py

collect integer from 0 to 1000 and store as integer
digit = 0
while the integer > 0
    last_digit = integer % 10
    digit += last_digit
    integer /= 10
print(total)
""" 
digit = 0
integer = int(input("Enter an integer: "))
while integer > 0:
    last_digit = integer % 10
    digit = digit + last_digit
    integer //= 10
print(digit)
