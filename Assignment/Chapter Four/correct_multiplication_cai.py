"""
correct_multiplication_cai.py
Computer assisted instruction CAI

"""

def get_correct(answer):
    if answer == 42:
        return answer

while(True):
    answer = int(input("How much is 6 x 7 = "))
    if(answer == get_correct(answer)):
        print("Correct Answer!")
        break
    else:
        print("Wrong answer! please try gain")


