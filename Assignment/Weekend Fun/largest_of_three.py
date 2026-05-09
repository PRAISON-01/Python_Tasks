first = int(input('Enter first number: '))
largest = 0


second = int(input('Enter second number: '))
third = int(input('Enter third number: '))

if first >largest:
    largest = first

if second > largest:
    largest = second
if third > largest:
    largest = third

print(largest)
