"""
collect user input 
let the largest be zero
for number in range 1 to 10
input number again
if the number is grater than the largest 
largest is equal to the number
go out of if statement 
print lagest
"""
number = int(input("Enter number: "))
largest = 0
for number in range(1,11):
    number = int(input("Enter number: ")) 
    if number > largest:
        largest = number
        
print(f"The Largest of the 10 numbers is: {largest}")
