seconds = int(input("Enter any number of seconds : "))

hour = int(seconds / 3600)
minutes = int((seconds % 3600) / 60)
secondRemaining = int(seconds % 60)
print(seconds," is equivalent to",hour,"hours,",minutes,"minutes,", secondRemaining,"seconds") 
