number = int(input("Enter number of rows of stars => "))
size = number + 1

for row in range(1,size,1):
        for col in range(1,row + 1,1):
                print("*", end=" ")
        print("")
