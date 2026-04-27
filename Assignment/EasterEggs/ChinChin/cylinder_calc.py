"""
cylinder_calc.py

collect radius

collect hieght
pi = 3..412
area =(2 * pi * radius * height) + (2 * pi) * (radius ** 2)
"""

radius = int(input("Enter Radius: "))
height = int(input("Enter Height: "))

pi = 3.412
area = (2 * pi * radius * height) + (2 * pi) * (radius ** 2)
print(area)

