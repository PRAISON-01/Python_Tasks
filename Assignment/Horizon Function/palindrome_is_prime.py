"""
create a function to check for palindrome

    create an empty string for store the revervsed digits
    loop through each digits 
        then the 'reverse' adds up the digits as a string from the back

    if the number is 'NOT' equals to the reverse or the reverse is 'NOT' number
        the number is not a palindrome (return false)
    otherwise it is a palindrome

    create a function for checking if number is a prime number 
        if number is lesser than one
            the number is not prime (return false)
        if number is less than 3
            number is prime {numbers less than 3 incluedes 2 and 3}(return true)
        if number % 2 == 0 and number % 3 == 0 
            to exclude the numbers that are even and the ones divisible than 3 (return false)

        
        //for square value
        initialise i to 5 
        so odd numbers start counting from 5 for the square root condition
        while square of i <= n
            if number % i == 0 or number % 3 == 0 (return false)
            
            increase i with 6 for cases of (5+6 = 11) as a short cut
            (return true)

       in the palindrome funtion return the inner function

"""

def is_palindrome(number):

    reverse = ""
    for digits in number:
        reverse = digits + reverse

    if number != reverse or reverse != number:
        return False
#    return True

    def is_prime(number):
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False

        i = 5
        while i * i <= 5:
            if number % i == 0 or  number % (i + 2) == 0:
                return False
            i += 6
        return True

    return is_prime(int(number))

number = (input("Enter a number => "))
print(is_palindrome(number))

