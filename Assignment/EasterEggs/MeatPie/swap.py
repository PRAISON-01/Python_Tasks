"""
swap.py


collect a
colect b
set temp = a
a becomes b
b = temp

"""

a = int(input("Enter 'a': "))

b = int(input("Enter 'b': "))

temp = a
a = b
b = temp
print(" ")
print(f"swapped a = {a}")
print(f"swapped b = {b}")
