"""
bmi_checker.py

collect weight 
collect height 

bmi = weight/ (height ** 2)

print bmi

if bmi < 18.5
    print underweight
elif bmi < 25
    print Normal
elif bmi < 30
    print overweight
else
    obese
"""

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print(f"BMI = {bmi:.3f}")

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 30:
    print("Overweight")
else:
    print("Obese")
