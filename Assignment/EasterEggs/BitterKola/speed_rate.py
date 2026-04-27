"""
speed_rate.py

collect speed 
if speed == 0
    print stationary
if speed >= 1
    print slow
if speed > 40
    print moderate
if speed > 80
    print fasr
if speedd > 120
    print Over Speeding
"""

speed = int(input("Enter speed: "))
if speed == 0:
    print("Stationary")
elif speed <= 40:
    print("Slow")
elif speed <= 80:
    print("Moderate")
elif speed <= 120:
    print("Fast")
else:
    print("Over Speeding!")
