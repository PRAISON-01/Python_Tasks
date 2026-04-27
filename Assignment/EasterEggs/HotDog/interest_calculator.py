"""
interest_calculator.py

collect balance
collet rate
interest = balance * (interest / 1200)
print(interest)
"""

balance = int(input("Enter Balance: "))
rate = int(input("Enter rate: "))
ratep = rate / 100
interest = balance * (ratep / 1200)
print(f"Interest for the next MOnth: {interest:.2f}")
