"""
future_investment.py

collect principal
collect annual rate 
ratep = rate / 100
collect year
future_return = principal * ((1 + ratep) ** (year))
print future_return
"""

principal = int(input("Enter investment Amount: $"))
rate = int(input("Enter Annual Rate: "))
ratep = rate / 100
year = int(input("Enter numbe of years: "))
future_return = principal * ((1 + ratep) ** (year))
print(f"future return aftre {year} years: {future_return}")
