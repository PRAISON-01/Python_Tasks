"""
gpa.py

collect grade
match grade with letter a, b, c, d and f
and print the gpa score

"""

grade = input("Enter Grade: ")

match grade:
    case 'A':
        print("4.0")
    case 'B':
        print("3.0")
    case 'C':
        print("2.0")
    case 'D':
        print("1.0")
    case 'F':
        print("0.0")
    case 'a':
        print("4.0")
    case 'b':
        print("3.0")
    case 'c':
        print("2.0")
    case 'd':
        print("1.0")
    case 'f':
        print("0.0")
    case _:
        print("Invalid Grade")    
