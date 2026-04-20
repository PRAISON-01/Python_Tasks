"""
collect user input and store as number
initiialise count ro zero
using for loop set count is >= 10
    product = number * count
    print nummber x count = product
    count++
end loop
"""

number = int(input("Enter number: "))
count = 0
for count in range(1,11):
    product = number * count
    print(f" {number} x {count} = {product}")
    count += 1
