"""
simple_compound_interest.py

collect principal
collect rate
collect time
collect frequency
si = (principal * rate * time)/ 100

ci_base = 1 + ((rate / 100) / freq)
ci_index =  freq * time
ci = principal * Math.pow(ci_base, ci_index)) - (principal)
"""

principal = int(input("Enter Principal: $"))
rate = int(input('Enter rate: '))
time = int(input("Enter Time: "))
freq = int(input("Enter Frequency: "))

si = (principal * rate * time)/ 100

ci_base = 1 + ((rate / 100) / freq)
ci_index =  freq * time
ci = principal * (ci_base ** ci_index) - (principal)

print(f"Simple Interest: ${si:.3f}")
print(f"compound Interest: ${ci:.3f}")

