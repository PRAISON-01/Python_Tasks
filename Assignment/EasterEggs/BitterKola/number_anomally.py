
"""
number_anomally.py

collect a
collect b 

if a and b is greater than zero
    print their sum
else if a and be are lesser than zero 
    print their product
else
    if a > b
        print a - b
    else 
        print b - a
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > 0 and b > 0:
    print("Sum =", a + b)
elif a < 0 and b < 0:
    print("Product =", a * b)
else:
    if a > b:
        print("Difference =", a - b)
    else:
        print("Difference =", b - a)
