principal = int(input("Enter Principal : "))
rate = int(input("Enter Rate : ")) / 100
time = int(input("Enter Time : "))

si = principal * rate * time
totalAmt = principal + si

print("Simple Interest : ",si)
print("Total Amount : ",totalAmt)

