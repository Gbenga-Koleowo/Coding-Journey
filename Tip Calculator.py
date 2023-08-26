# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

l = len(names)

bill_payer = random.randrange(0,l)
print(names[bill_payer] + " is going to buy the meal today!")

