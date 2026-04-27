"""
interest_balance.py

collect balance
collect rate
rate_d = rate / 100

interestA = balance * (1 + rate_d)
interestB = interestA * (1 + rate_d)
interestC = interestB * (1 + rate_d)

print blance after 1 year
print balance after 2 year
print balancce after 3 year

"""

balance = int(input("Enter your bank balance: $"))

rate = int(input("Enter Annual Rate: "))
rate_d = rate / 100

interestA = balance * (1 + rate_d)
interestB = interestA * (1 + rate_d)
interestC = interestB * (1 + rate_d)

print(f"Balance after 1 year: ${interestA:.3f}")
print(f"Balance after 2 year: ${interestB:.3f}")
print(f"Balance after 3 year: ${interestC:.3f}")

