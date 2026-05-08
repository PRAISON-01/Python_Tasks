def validate_email(email):
    if "@" not in email:  #priority reasons 
        return False
    if email[0] == "@" or email[-1] == "@":
        return "Invalid Email"
    if len(email) >= 8:
        return True
    if len(email) < 8:
        return False
#because every string is either 8+ or shorter so the function finishes when at either whetther the  is either 8+ or less and returns it never reches to check if @ for the @ symbol.... in essence detail comes before length
def calculate_balance(transactions):
    total = 0
    for amount in transactions:
        total+= amount
    return total
#using list for transactions and iterate through the elements and acumulate to total then return total
def is_strong_password(password):
    if len(password) >= 8:
        return True
    return False

def apply_interest(balance, rate, year):
    if rate < 0 or year < 1:
        raise ValueError("Invalid rate or year!")
    compound_interest = round(balance * (1 + rate) ** year, 2)
    return compound_interest
