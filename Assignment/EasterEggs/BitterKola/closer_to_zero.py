"""
closer_to_zero.py

collect first number
collect second number


if first = second:
    print both closer to zero
elif first > second:
    print second is closer to zero
else:
    print first is cloer to zero 
"""

first = int(input("Enter First Number: "))
second = int(input("Enter Second Number: "))

if first == second:
    print(f"Both {first} and {second} are closer to Zero")
elif first > second:
    print(f"{second} number is closer to zero")
else:
    print(f"{first} is closer to zero")
