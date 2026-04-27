"""
month.py

collect number

match number
    case 1
        print January....
    cas _:
        print error message
"""
month = int(input("Enter Month Number: "))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("February")
    case 6:
        print("February")
    case 7:
        print("February")
    case 8:
        print("February")
    case 9:
        print("February")
    case 10:
        print("February")
    case 11:
        print("February")
    case 12:
        print("February")
    case _:
        print("Invalid MOnth Number")
   

