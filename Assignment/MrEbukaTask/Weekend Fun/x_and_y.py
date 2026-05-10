x = int(input("Enter 'X'=> "))
y = int(input("Enter 'Y' => "))

q =""

if x > 0 and y > 0:
    q = "Q1"
    
elif x < 0 and y > 0:
    q = "Q2"
    
elif x < 0 and y > 0:
    q = "Q3"
    
elif x < 0 and y > 0:
    q = "Q4"
    
elif x == 0 and y == 0:
    q = "Origin"
    
elif y == 0 and x != 0:
    q = "X-axis"
    
elif x == 0 and y != 0:
    q ="Y-axis"
    

print(q)
