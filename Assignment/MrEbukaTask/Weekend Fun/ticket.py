age = int(input("Enter 'Age'=> "))

price =""

if age < 5:
    price="Free"
elif age < 12:
    price="$5"
elif age < 64:
    price = "$12"
elif age >= 65:
    price="$8"

print(price)
