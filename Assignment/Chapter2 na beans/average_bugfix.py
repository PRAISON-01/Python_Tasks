"""Question 5: Write a python eexpression that correctly computes the average of five numbers: 10, 20, 30, 40, 50. Many beginners write (10+20+30+40+50/5) --- Identify the bug and fix it"""

average = 10+20+30+40+50/5
avg = int(average)
print(avg)

#bug was the result was in decimal. fixed it by casting floating values with int

