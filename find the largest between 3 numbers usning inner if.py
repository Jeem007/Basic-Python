num1=int(input("Enter your 1st number: "))
num2=int(input("Enter your 2nd number: "))
num3=int(input("Enter your 3rd number: "))
if(num1>num2):
    if(num1>num3):
        print("Largest number is: ",num1)
    else:
        print("Largest number is: ",num3)
if(num2>num1): #we can use here else: also.The result will be remain same
    if(num2>num3):
        print("Largest number is: ",num2)
    else:
        print("Largest number is: ",num3)

