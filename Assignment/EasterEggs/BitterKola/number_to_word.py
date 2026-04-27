"""
number_to_word.py

collect amount in dollars
if amount = 1
    print one dollar...to ten dollar
else
    invalid amount
"""

amount = int(input("Enter Any Amount (1 - 10): $"))
match amount:
    case 1:
        print("One Dollar")
    case 2:
        print('Two dollar')
    case 3:
        print("Three Dollars")
    case 4:
        print("Four Dollars")
    case 5:
        print("Five Dollars")
    case 6:
        print("Six Dollars")
    case 7:
        print("Seven Dollars")
    case 8: 
        print("Eight Dollars")
    case 9:
        print("Nine Dollars")
    case 10:
        print("Ten Dollars")
    case _:
        print("Invalid Amounnt")

