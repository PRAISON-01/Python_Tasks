"""
input binary
set decimal_value to zero
set power to zero
while the binary is greater than zero
    set digit = binary % 10
    set decimal_value = digit * (2 ** power)
    power += 1
    digit = binary // 10
display decimal_value
"""

binary = int(input("Oga, Enter binary value: "))
decimal_value = 0
power = 0
decimal = 0
while binary > 0:
    digit = binary % 10
    decimal_value = digit * (2 ** power)
    decimal += decimal_value
    power += 1
    binary //= 10

print(f"The Decimal equiuvalent of the binary is {decimal}")
