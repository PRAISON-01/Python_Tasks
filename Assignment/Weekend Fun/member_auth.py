total_bill = int(input("Enter a Total bill => $"))

member = input("Enter a (yes/no) => ").lower()

if member == "yes":
    answer = total_bill * (10/100)
    print(answer)
elif member =="no":
    answer = total_bill * (5/10)
    print(answer)
