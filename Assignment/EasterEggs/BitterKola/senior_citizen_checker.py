"""
senior_citizen_checker.py

collect birth year
if year <= 1961:
    print eligible
else
    priint ineligible

"""
year = int(input("Enter Birth Year: "))
if year <= 1961:
    print("You are eligible for the Senior Citizen Discount: ")
else:
    print("You are 'NOT' eligible for the senior citizen discount")
