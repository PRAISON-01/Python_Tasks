weight = int(input("Enter Weight => "))

height = int(input('Enter haeight => '))

bmi = weight /(height * height)

result =""

if bmi < 18.5:
    result = "UnderWeight"
elif bmi >= 18.5 or bmi <=24.9:
    result = "Over weight"
elif bmi >= 30:
    result = "Obese"

print(result)
