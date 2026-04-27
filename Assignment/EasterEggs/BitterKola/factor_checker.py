"""
factor_checker.py

collect first number 
collect second number
    if first % second == 0
        print resullt
    else 
        print not a factor...

"""
first = int(input("ENter first Number: "))
second = int(input("Enter Second Number: "))
if first % second == 0:
    print(f"{first} is 'NOT' a factor of {second}")
else:
    print(f"{first} is a factor of {second}")
