from random import randint

print("Welcome to this Game")
print("Guessing Game")
print("-----------------------")
for x in range(1,6):
   guessNumber=int(input("Enter your guess between 1 to 5 :"))
   randomNumber=randint(1,5)
   if guessNumber==randomNumber:
         print("You have won the game")
   else:
         print("You have loss the game")
         print("Random number was:",randomNumber)