'''
outside loop 
0ut_loop is within 1 and 5 and decreases by 1
    print outside loop
    inside_loop is within 1 and 5 and decreases by 1
'''

for num in range(5,0,-1):
    for col in range(num,0,-1):
        print(col , end=" ")
    print(" ")
        
