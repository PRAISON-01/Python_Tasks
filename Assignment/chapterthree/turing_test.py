""" 
prompt user and collect input "What is your problem"
collect the user input and ignore
prompt the user again with "Have you had this problem before (yes/no)"
if the user enters 'yes' print "Well you have it again"
else if 'no' print "well, you have it now"
"""

problem = input("Oga, wetin be your problem?  ")

question = input("This thing done do you before? (yes/no)  ")

if question == "yes":
   print("Well, e done do you again")

if question == "no":
   print("well, you done get am")


