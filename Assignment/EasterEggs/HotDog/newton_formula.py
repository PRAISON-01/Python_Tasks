"""
newton_formula.py

collect velocity
collect time span
collect acceleration
distance = (velocity + time) + (0.5)*(accelration)*(time ** 2)
"""
velocity = int(input("Enter Velocity: "))
time = int(input("Enter Time: "))
acceleration = int(input("Enter Acceleration: "))
distance = (velocity * time) + (0.5) * (acceleration) * (time ** 2)
print(f"Distance travelled = {distance} units ")
