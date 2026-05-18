
#check_out.py

from datetime import datetime, date

time = datetime.now()

name = input("What is the customer name => ")

item_list = []
quantity_list = []
price_list = []

is_running = True
count = 0

while is_running:

    item_input = input("What did the user buy? => ")
    item_list.append(item_input)

    quantity_input = int(input("How many pieces? => "))
    quantity_list.append(quantity_input)

    price_input = int(input("How much per unit? => #"))
    price_list.append(price_input)

    add_more = input("Add more items? (yes/no)  ")

    count += 1
    if add_more.lower() == "no":
        is_running = False
        break


#print(count)
cashier = input("Enter cashier name => ")

rate_input = int(input("How much discount will he get? => "))

sub_total = 0.0
for i in range(0, count):
    sub_total += (price_list[i] * quantity_list[i])

rate = rate_input/100


discount = sub_total * rate
vat = sub_total * 0.175
bill_total = sub_total - discount + vat



print()
print()

print("SEMICOLON STORES")

print("MAIN BRANCH")

print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.")

print("TEL: 091-SEMI-0000")

print(f"Date: {time}")

print(f"Cashier: {cashier}")

print(f"Customer Name: {name}")
print()
print()
print("============================================================")
print("                     ITEM    QTY     PRICE       TOTAL(NGN)")
print("============================================================")
print()
print()
for index in range(0, count):
    item_total = price_list[index] * quantity_list[index]
    print(f"{item_list[index]:<20}{quantity_list[index]:>8}{price_list[index]:>14.2f}{item_total:>18.2f}")

print()
print()
print("============================================================")
print()
print(f"                                     Sub Total => {sub_total:.2f}")
print(f"                                      Discount => {discount:.2f}")
print(f"                                  VAT @ 17.50% => {vat:.2f}")
print()
print("============================================================")
print()
print(f"                                    Bill Total => {bill_total:.2f}")
print()
print("============================================================")
print(f"THIS IS NOT A RECIEPT KINDLY PAY #{bill_total:.2f}")
print("============================================================")

paid = float(input("How much did the customer give yo you? => "))

balance = paid - bill_total

#Reciept
print()
print()

print("SEMICOLON STORES")

print("MAIN BRANCH")

print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.")

print("TEL: 091-SEMI-0000")

print(f"Date: {time}")

print(f"Cashier: {cashier}")

print(f"Customer Name: {name}")
print()
print()
print("============================================================")
print("                     ITEM    QTY     PRICE       TOTAL(NGN)")
print("============================================================")
print()
print()
for index in range(0, count):
    item_total = price_list[index] * quantity_list[index]
    print(f"{item_list[index]:<20}{quantity_list[index]:>8}{price_list[index]:>14.2f}{item_total:>18.2f}")


#discount = sub_total - (sub_total * rate)
#
#bill_total = discount + subtotal
#

print()
print()
print("============================================================")
print()
print(f"                                     Sub Total => {sub_total:.2f}")
print(f"                                      Discount => {discount:.2f}")
print(f"                                  VAT @ 17.50% => {vat:.2f}")
print()
print("============================================================")
print()
print(f"                                    Bill Total => {bill_total:.2f}")
print(f"                                   Amount Paid => {paid:.2f}")
print(f"                                       Balance => {balance:.2f}")
print("============================================================")
print("                 THANK YOU FOR YOUR PATRONAGE                    ")
print("============================================================")




