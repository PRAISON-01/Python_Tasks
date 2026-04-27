"""
prductivity_checker.py

collect wph (wage per hour)

collect hour

if hours <= 40
    pay = wph * hour
else 
    over_time = hours - 40
    pay = (wph * 40) + (over_time * wph * 1.5);
print ("Hours Worked : "+ hours +": Total Pay : "+ normalPay)

"""

wph = int(input("Enter Wage Per Hour: "))
hour = int(input("Enter Number of hours worked: "))

if hour <= 40:
    pay = wph * hour
else:
    over_time = hours - 40
    pay = (wph * 40) + (over_time * wph * 1.5)
print(f"Hours Worked : {hour}: Total Pay : {pay}")
