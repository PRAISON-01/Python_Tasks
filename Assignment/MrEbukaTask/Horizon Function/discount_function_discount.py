"""
Write a function that accepts the item of an item, the original
price of the item, and a promotional code. If the promotional code
is "SAVE10", apply a 10% discount, if it’s "HALFOFF", apply a 50%
discount and if there’s no valid code apply no discount. Return the
discounted price. write tests confirming that the correctness of the
function and ensure you handle potential edge cases.
"""


#def discount_price(item, price, promo_code):
#    
#    discount_msg = promo.upper()
#
#    if discount_msg == "SAVE10":
#        discount = 10/100
#    elif discount_msg == "HALFOFF":
#        discount =  50/100
#    else:
#        discount = 0
#    
#    discount_price = price * (discount)
#    return discount_price
#
#    if item_choice == 1:
#        item, price = "Rice $", 500.0
#
#    elif item_choice == 2:
#        item, price = "Beans $", 250.0
#
#print(f"if you entered {item}")
#print(f"Price: {price}")
#
#print(f"Discount price for {item}: ${discount_price}")





def discount(name, price, promo_code):

    if promo_code.lower() == "save10":
        discount_price = price * (10 / 100)
        final_price = price - discount_price
        
        return final_price
        
    elif promo_code.lower() == "halfoff":
        discount_price = price * (50 / 100)
        final_price = price - discount_price
        
        return final_price
        
    else:
        final_price = price
        
        return final_price


    if item_choice == 3:
        item, price = "Zobo $", 100.0

    else:
        print("Erro 404 'position out of boun'd")
    

        return(item, price, promo_code)


print(f"if you entered {item}")
print(f"Price: {price}")

print(f"Discount price for {item}: ${discount_price}")

    

    
    


