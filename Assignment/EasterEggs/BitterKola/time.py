"""
time.py
"""

h1 = int(input("Enter first hour: "))
m1 = int(input("Enter first minute: "))

h2 = int(input("Enter second hour: "))
m2 = int(input("Enter second minute: "))

hours = h1 + h2
minutes = m1 + m2

hours += minutes // 60
minutes = minutes % 60

print(f"Total time = {hours}:{minutes}")
