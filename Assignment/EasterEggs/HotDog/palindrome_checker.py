"""
palindrome_checker.py

collect number = user input
collect original = number
collect reverse = 0

while number > 0
    collect last_digit = number % 10
    collect reverse = (reverse * 10) + last_digit
    collect number = number / 10 (integer division)


IF original == reverse
    PRINT "It is a palindrome"
else
    PRINT "It is not a palindrome"


"""

number = int(input("Enter Number: "))
original = number
reverse = 0

while number > 0:
    last_digit = number % 10
    reverse = (reverse * 10) + last_digit
    number = number // 10
print(f"reverse of {reverse}") 

if original == reverse:
    print("is a palindrome")
else:
    print("is 'NOT' a palindrome")
