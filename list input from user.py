n=input("Enter a text of numbers for addition:") #10 20 30 40 50
list=n.split() # 10 ,20 ,30 ,40 ,50
# split is use for separate the number from string input
sum=0
for num in list:
    sum=sum+int(num)
print("Your sum is :",sum)