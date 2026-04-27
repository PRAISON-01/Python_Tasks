"""
insurance_deduction.py

collect salary

if salary <= 50000:
    deduction = salary * 0.00
elif salary <= 150000:
    deduction = salary * 0.05
elif salary <= 500000:
    deduction = salary * 0.075
else:
    deduction = salary * 0.1

net_salary = (salary - deduction)
print Social Insurance Deduction   
"""

salary = int(input("Enter Salary: "))

if salary <= 50000:
    deduction = salary * 0.00
elif salary <= 150000:
    deduction = salary * 0.05
elif salary <= 500000:
    deduction = salary * 0.075
else:
    deduction = salary * 0.1

net_salary = (salary - deduction)
print(f"Social Insurance Deduction: {deduction}")
print(f"Net Salary : {net_salary}")
