"""
circle_area.py

collect radius
area = (math.pi) * radius ** 2
print area

"""
import math

radius = int(input("Enter Radius: "))
area = (math.pi) * (radius ** 2)
print(f"Area of circle = {area:.3f} Square units")
