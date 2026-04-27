"""
cost_of_trip_calc.py

collect distance
collect mpg
and the ppg
cost of trip = (distance/mpg) * ppg
print cost of trip
"""

distance = int(input("Enter distance: "))
mpg = int(input("Enter Miles Per Gallon: "))
ppg = int(input("Enter Price Per gallon: $"))
cost_of_trip = (distance/mpg) * ppg
print(f"Cost of trip ${cost_of_trip:.3f}")
