#Collect father's age

#Collect son's age'

#if father  and son age is less than and greater than 80 return age outof bound 

# Double the son's age and calculate the differnce between the age

#print the result
father = int(input("Enter First age: "))
son = int(input("Enter son's age: "))

if father < 0 or father > 80:
    print('Age out of bound')
elif son < 0 or son > 80:
    print('Age out of bound')
    

else:
    difference = abs(father -(son * 2))

    print(f"He was twice as old as his son {difference} years ago")
