"""
asterix_box.py

set row to 1
while riow <= 4
    setcol to onoe
    while col <= 4
        print( asterix on the same line
        increase col by one 
    print new line
    increase row ny one
"""
row = 1
while row <= 4:
    col = 1
    while col <= 4:
        print("*", end="|")
        col+=1
    print()
    row+=1
