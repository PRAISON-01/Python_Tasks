"""
assign variable and collect user input for five digit nmber
for when the number is greater than zero
the last digit is equal to the remainder of the digit when divided by 10
print laast digit
digit itsekf is then divided by 10
repeat for loop
"""

number = int(input("Enter a number: "))

while number > 0:
    last_digit = number % 10
    print(last_digit)
    number = number // 10
