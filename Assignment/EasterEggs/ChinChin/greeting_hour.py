"""
greeting_hour.py

collect hour

str greeting = match hour:
    case 5, 6, 7, 8, 9, 10, 11:
        ptint Good Morning
    case 12, 13, 14, 15, 16, 17:
        print Good AfterNoon
    case 18, 19, 20, 21:
        print Good Evening
    case 23, 24, 1, 2, 3, 4:
        print Good Night
print(greeting)
"""

hour = int(input("Enter Hour Of the Day: "))
str greeting = match hour:
    case 5, 6, 7, 8, 9, 10, 11:
        print(" Good Morning ")
    case 12, 13, 14, 15, 16, 17:
        print(" Good AfterNoon ")
    case 18, 19, 20, 21:
        print(" Good Evening ")
    case 23, 24, 1, 2, 3, 4:
        print(" Good Night ")
    case _:
        print("Invalid Input")
print(greeting)
