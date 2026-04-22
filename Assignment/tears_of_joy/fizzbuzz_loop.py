"""
the count should be within the range of 1 and 50
    if the count is divisible by 3 with no remainder and count is divisible by   with no remainder print "FIZZBUZZ"
    else if the count is divisible by 3 with no remainder print "Fizz"
    else if the count is divided by 5 with no remainder print "Buzz"
    else print count then new line

"""
for count in range(1,51):

    if count % 3 == 0 and count % 5 == 0:
        print("FizzBuzz", end=" ")
    elif count% 3 == 0:
        print("Fizz", end=" ")
    elif count % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(count, end=" ")
