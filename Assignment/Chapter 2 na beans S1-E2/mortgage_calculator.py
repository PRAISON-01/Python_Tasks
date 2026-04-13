principal = int(input("Enter principal amount : "))
rate = int(input("Enter rate : ")) / 100
duration = int(input("Enter duration of loan : "))
num = rate * (1 + rate) ** duration
den = ((1 + rate) ** duration) - 1
result = int((principal * (num)) / den)
salary = print("Your Monthly payment amount : $",result)
