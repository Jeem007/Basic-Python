num1=int(input("Enter your 1st number: "))#num1=20
num2=int(input("Enter your 2nd number: "))#num2=10
num3=int(input("Enter your 3rd number: "))#num3=45
if (num1>num2) and (num1>num3):
    largest=num1
elif(num2>num1) and (num2>num3):
    largest=num2
else:
    largest=num3
    print("largest number is:",largest)

