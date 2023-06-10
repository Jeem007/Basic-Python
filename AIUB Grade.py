marks=float(input("Enter your marks: "))
if (marks>=90 and marks<=100):
    grade=4.00
elif(marks>=85 and marks<90):
    grade=3.75
elif(marks>=80 and marks<85):
    grade=3.50
elif(marks>=75 and marks<80):
    grade=3.25
elif(marks>=70 and marks<75):
    grade=3.00
elif(marks>=65 and marks<70):
    grade=2.75
elif(marks>=60 and marks<65):
    grade=2.50
elif(marks>=50 and marks<60):
    grade=2.25
else:
    grade=0.00

print("Your grade is",grade)

