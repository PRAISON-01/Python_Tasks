"""
quadratic_root.py

colect a, b , and c
d = (b ** 2) - 4 * a * c
if(d > 0)
    root_one = (-b + (d ** 0.5))/2 * a
    root_two = (-b - (d ** 0.5))/2 * a
print(root_one , root_two)
elif(d = 0)
    root_three = (-b + (d ** 0.5))/2 * a
    root_four = (-b - (d ** 0.5))/2 * a
print(root_three , root_four)
"""

a = int(input("Enter Number for 'a': "))
b = int(input("Enter Number for 'b': "))
c = int(input("Enter Number for 'c': "))
d = (b ** 2) - 4 * a * c
if (d > 0):
    root_one = (-b + (d ** 0.5))/ 2 * a
    root_two = (-b - (d ** 0.5))/2 * a 
print(f"Two root of the quadratic equatin: {root_one} and {root_two}")
if(d == 0):
    root_three = (-b + (d ** 0.5))/2 * a
    root_four = (-b - (d ** 0.5))/2 * a
print("Roots of the quadratic equatiion is {root_three} and {root_four}")
