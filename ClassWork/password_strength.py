"""
collect user input
if the input is < 8 display very-weak
if the iinput is == 8 display weak
if the input is >= 8 and <=16 strong
if the input iis > 16 very strong
"""



password = input("Enter password: ")

if len(password) < 8:
    print("Very Weak")

if len(password) == 8:
    print("Weak") 

if len(password) >=8:
    print("Strong")

if len(password) > 16:
    print("very Strong")
