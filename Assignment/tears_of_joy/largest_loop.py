number = input("Enter number: ")
largest = None

while number != "done":
    number = int(number)
    if largest is None or number > largest:
        largest = number
        
    number = input("Enter number: ")
print(largest, " is the largest")
