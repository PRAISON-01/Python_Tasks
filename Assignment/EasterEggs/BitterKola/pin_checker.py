"""
pin_checker.py

collect pin

while True:
    if pin >= 1000 and <= 9999
        collect validation
        if validation = pin
            print Valid pin
        else
            print try agin
        break
    else
        pin must be 4 digit

"""

pin = int(input("Enter 4-Digit PIN: "))

while True:
    if pin >= 1000 and pin <= 9999:
        validation = int(input("Enter PIN to confirm: "))
        if validation == pin:
            print("Valid PIN")
        else:
            print("Something Went Wrong. Try again later")
        break
    else:
        pin = int(input("Enter 4-Digit PIN. Try again!: "))
