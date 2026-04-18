"""
collect input for principal
initailise rate is 7 / 100
initialise year to 1
for when year is 1 to 30
anual deposit is the principal * 1 + rate ** year
year increases by one 
"""
principal = int(input("Enter Principal: $"))

rate = 7 / 100

year = 1

for year in range(1,31):

    investment = (principal) * (1 + rate) ** year

    year += 1

    print("$",investment)
    
