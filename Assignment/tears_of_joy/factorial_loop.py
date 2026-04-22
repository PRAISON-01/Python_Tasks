"""
collect input and store as factorial
initialise count to one 
initialise answer to 1
the loop repeats as long as the count is <= factorial
    answer *= count
    count increments by one
print answer 
"""
factorial = int(input("Enter how many factorials: "))

count = 1
answer = 1
while count <= factorial:
    answer *= count
    count += 1
print(answer)
