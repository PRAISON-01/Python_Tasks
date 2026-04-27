"""
palindrome_checker.py

collect number

for num in range(1,4)
    last_digit = number % 10
    number /= 10
print number
"""

number = int(input("Enter Number: "))

for num in range(1,4):
    last_digit = number % 10
    number /= 10
print(number)
