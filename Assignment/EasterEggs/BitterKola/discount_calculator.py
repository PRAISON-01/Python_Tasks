"""
discount_calculator.py

collect price
collect discount rate
ratep = rate / 100
discount = price * ratep
discount_price = price - (discount)

"""
price = int(input("Enter Price: $"))
rate = int(input("Enter Discount rate: "))
ratep = rate/ 100
discount = price * ratep
discount_price = price - (discount)
print(f"Discount Price of {rate}% off: {discount_price}")
