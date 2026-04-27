"""
right_angle_triangle_star.py

initialize row as 1
while the row is <= 5
    initialise col as 1
    while the col <= row 
         print " * " and let it be on the same line
        increase the col by one
    print new line
    increase the row by one 
"""
row = 1
while row <= 5:
    space = 5
    col =1
    while space >= row:
        print(" ", end=" ") 
        space -= 1
    while col <= row:
        print("*", end=" ")
        col+= 1
    print()
    row += 1
        
