"""
positive_integer.py

collect n 
while true:
    if n >= 0:
        break
    elif enter a positive number
result = (n * (n + 1)) / 2
"""

n = int(input("Enter Number 'n': "))
while True:
    if n >= 0:
        break
    else:
        n = int(input("Enter a positive number: "))

result = (n * (n + 1)) / 2
print(f"(n x (n + 1))/ 2 = {result}")
