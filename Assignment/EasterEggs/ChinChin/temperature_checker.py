"""
temperature_checker.py

collect temperature

if temp < 0:
    diaplay freezing
elif temp <= 15
    display cold
elif temp <= 25
    display Warm
else:
    display Hot
"""

temp = int(input("Enter Temperature In Celcius: "))

if temp < 0:
    print("Freezing")
elif temp <= 15:
    print("Cold")
elif temp <= 25:
    print("Warm")
else:
    print('Hot')
