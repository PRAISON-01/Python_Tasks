"""
gratuity.py

collect subtotal
collect rate
gratuity = rate * subtotal
subtotal = gratuity + subtotal
print gratuity and subtotal
"""

subtotal = int(input("Enter Subtotal: "))
rate = int(input("Enter rate: "))
ratep = rate / 100
gratuity = ratep * subtotal
total = gratuity + subtotal
print(f"Gratuity: ${gratuity} ")
print(f"Total: ${total}")

