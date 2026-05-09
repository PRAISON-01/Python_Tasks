print("===SIMPLE CALCULATOR===")

firstnumber = int(input("\nEnter First Number: "))
operator = input("Enter operatorerator (+, -, /, //, *, **, %): ").strip()
secondnumber = int(input("Enter Second Number: "))

if operator == "+":
    print(f"Result: {firstnumber + secondnumber}")
elif operator == "-":
    print(f"Result: {firstnumber - secondnumber}")
elif operator == "*":
    print(f"Result: {firstnumber * secondnumber}")
elif operator == "/":
    if secondnumber != 0:
        print(f"Result: {firstnumber / secondnumber}")
    else:
        print("Error: Division by zero")
elif operator == "//":
    if secondnumber != 0:
        print(f"Result: {firstnumber // secondnumber}")
    else:
        print("Error: Division by zero")
elif operator == "**":
    print(f"Result: {firstnumber ** secondnumber}")
elif operator == "%":
    print(f"Result: {firstnumber % secondnumber}")
else:
    print("Invalid operatorerator.")

