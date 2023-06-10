NumOfWords=0
NumOfLetters=0
NumOfDigits=0

text=input("Enter your text: ")
for x in text:
    x=x.lower() #convert user input to lower case
    if x>='a' and x<='z':
        NumOfLetters=NumOfLetters+1
    elif x>='0' and x<='9':
        NumOfDigits=NumOfDigits+1
    elif x==" ":
        NumOfWords=NumOfWords+1
print("Number of letters:",NumOfLetters)
print("Number of Digits:",NumOfDigits)
print("Number of words:",NumOfWords+1)



