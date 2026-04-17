"""A student wants to swap a=5 and b=10 so that a becomes 10 and b becomes 5. They write: a= b; b = a. Explain the bug. Write the correct solution"""

""""firstNum = 5
secondNum = 10
firstNum = 10
secondNum = 5

print("Swapped Result : a =",firstNum,"and b =",secondNum)"""

"""THE BUG: first number and second number had the same value until we reassigned the values to the other variables """

"""#correction1

a = 5
b = 10
temp = a
a = b
b = temp
print("Swapped Result : a =",a,"and b =",b)"""

#Correction2
a = 5
b = 10
a,b = b,a
print("Swapped Result : a,b : ",a,b)
