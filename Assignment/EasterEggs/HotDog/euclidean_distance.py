"""
euclidean_distance.py

collect x_one
collect y_one
collect x_two
collect y_two

x = (x_two - x_ one)** 2
y = (y_two - y_one)** 2
distance = (x + y) ** 0.5
print distance
"""

x_one = int(input("Enter X1: "))

y_one = int(input("Enter Y1: "))
x_two = int(input("Enter X2: "))
y_two = int(input("Enter Y2: "))

x = (x_two - x_one) ** 2
y = (y_two - y_one )** 2
Euclidean distance = (x + y) ** 0.5
print(f"Distance = {distance} units")
