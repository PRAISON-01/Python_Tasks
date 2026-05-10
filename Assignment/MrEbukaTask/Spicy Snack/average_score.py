first = int(input("Enter first score => "))
second = int(input("Enter second score => "))
third = int(input("Enter third score => "))

total = first + second + third

score = total/3
grade = ""
if score >= 90 or score <= 100:
    grade ="A"

elif score >= 80 or score < 90:
    grade ="B"

elif score >= 70 or score < 80:
    grade ="C"

elif score >= 60 or score < 70:
    grade ="D"

elif score >= 0 or score <60:
    grade ="F"

print(grade)

