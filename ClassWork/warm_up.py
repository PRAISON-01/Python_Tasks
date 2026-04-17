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

purchase_price = int(input("Enter Purchase Price: "))

    if purchase_price >= 1,000 and purchase_price <= 10,000:
        rate_one = 5/100
        discount_one = purchase_price * rate_one
        discount_price_one = purchase_price - dicount_one
        print(f"Discount Price: {discount_price_one}")

    if purchase_price > 10,000 and purchase_price <= 50,000:
        rate_two = 10/100
        discount_two = purchase_price * rate_two
        discount_price_two = purchase_price - dicount_two
        print(f"Discount Price: {discount_price_two}")

    if purchase_price > 10,000 and purchase_price <= 50,000:
        rate_three = 10/100
        discount_three = purchase_price * rate_three
        discount_price_three = purchase_price - dicount_three
        print(f"Discount Price: {discount_price_three}")
