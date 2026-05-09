password = input("Enter your password: ")

size = len(password)
strength =""
if size > 6 and size <= 10:
    strength ="Medium"
elif size < 6:
    strength ="Weak"

elif size > 10:
    strength ="Strong"

else:
    strength ="Password is invalid"

print(strength)
