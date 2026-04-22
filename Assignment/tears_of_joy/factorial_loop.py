factorial = int(input("Enter how many factorials: "))

count = 1
answer = 1
while count <= factorial:
    answer *= count
    count += 1
print(answer)
