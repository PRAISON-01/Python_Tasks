"""
largest_of_three.py

set largest to zero
set count to one
while the count is <= 3
    collect number
    if number > largest
        largest = number
    increase count by one
print largest
"""

largest = 0
count = 1
while count <= 3:
    number = int(input("Enter number: "))
    if number > largest:
        largest = number
    count += 1
print(largest)
