def cube(x):
    """Calculate th cube of x"""
    ans = x ** 3
    return ans

def mystery(x):
    y = 0
    for element in x:
        y += element ** 2
    return y

def seconds_since_midnight(hours, minutes, seconds):
    hours_to_second = hours * 3600
    minutes_to_seconds = minutes * 60
    
    total_seconds = hours_to_second + minutes_to_seconds + seconds
    return total_seconds

import datetime 

def date_and_time():
    print(datetime.datetime.today())

def to_farenheit(c):
    f = (9/5) * c + 32
    return f

#def getCorrect()

#
#
#
#
print(f"The cube of 2 is {cube(2)}")
print("Mystery Number: ",mystery([1,2,3,4,5]))
print("Time is: ",seconds_since_midnight(13,30,45))
date_and_time()

c = "Celcius"
f = "Farenheit"
print(f"{c:<10} ---- {f:>12}")
count = 1
while count <= 100:
        
    print(f"|{count:<10} ---- {to_farenheit(count):>10.2f}|")
    count += 1



