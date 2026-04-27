"""
first_and_last_sum.py

collect number 

first = number // 10000
last = number % 10

total = first + last
print result
"""
number = int(input("Enter a five digit integer: "))
while True:
    if number > 9999:
        break
    else:
        number = int(input("Enter A five digit integer: "))

first = number // 10000
last = number % 10
total = first + last
print(f"Total of {first} and {last} digit: {total}")
