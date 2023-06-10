"""
80-100 = A+
70-79 = A
60-69 = A-
"""
marks=float(input("Enter your marks:"))
if (marks>=80 and marks<=100):  #we can also write:  if(80<=marks<=100):
    print("Your grade is A+")
if (70<=marks<=79):
    print("Your grade is A")
if (60<=marks<=69):
    print("Your grade is A-")
