"""
hypotenuse_calculator.py

collect length of the opposite side of the triangle
collect for adjacent

hyp = ( (opp ** 2) + (adj ** 2)) ** 0.5
"""

opp = int(input("Enter Length of opposite: "))
adj = int(input("Enter length of adjacent: "))


hyp = ( (opp ** 2) + (adj ** 2)) ** 0.5
print(hyp)
