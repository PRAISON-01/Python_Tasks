print("Multiplication Table\n\n")
for num in range(1,10):
    print(num, end="|")
    for number in range(1,10):
        product = number * num
        print(f"{product:>3}", end=" ")
    print()
    for _ in range(1,10):
        if num ==1: print(f"{"___":>3}", end=" ")
    print()
