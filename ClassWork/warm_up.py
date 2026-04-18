"""
collect user input
if the purchsed price is >= 1,000 and <= 10,000
discount rate is 5 divided bby 100
discount is purchse price multiplied by the discount rate

elif the purchsed price is > 10,000 and <= 50,000
discount rate is 10 divided bby 100
discount is purchse price multiplied by the discount rate

elif the purchsed price is > 50,000 
discount rate is 20 divided bby 100
discount is purchse price multiplied by the discount rate"""

purchase_price = int(input("Enter Purchase Price: $"))

if purchase_price >= 1000 and purchase_price <= 10000:
    rate = 5/100
    discount = purchase_price * rate
    discount_price = purchase_price - discount
    print(f"Discount Price: ${discount_price}")

elif purchase_price > 10000 and purchase_price <= 50000:
    rate = 10/100
    discount = purchase_price * rate
    discount_price = purchase_price - discount
    print(f"Discount Price: ${discount_price}")

elif purchase_price  > 50000:
   rate = 10/100
   discount = purchase_price * rate
   discount_price= purchase_price - discount
   print(f"Discount Price: ${discount_price}")
