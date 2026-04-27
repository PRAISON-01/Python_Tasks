"""
sum_of_number.py

collect number 

total = 0
while number > 0:
    digit = number % 10
    total += digit
    number = number / 10
print total

"""
number = int(input("Enter Number: "))

total = 0

while number > 0:
    digit = number % 10
    total += digit
    number = number // 10
print(total)
