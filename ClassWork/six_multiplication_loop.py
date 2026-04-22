"""
collect user input and store as number
for when count <= 10 remains true
    product = number * count
    print nummber x count = product
    count++
end loop

"""

number = int(input("Enter number: "))
for count in range(1,11,1):
    product = number * count
    print(f" {number} X {count} = {product}")
    
