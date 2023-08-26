rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


print("Welcome to Rock, Paper, Scissors game!")
Playerschoice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

p_choice = 0

if Playerschoice == 0:
  p_choice = rock
  
elif Playerschoice == 1:
  p_choice = paper
  
else:
  p_choice = scissors
  
  Player = p_choice

print(f"You chose: \n {Player}")

import random

com_choice = 0 
com_pick = random.randint(0,2)
if com_pick == 0:
  com_choice = rock
  
elif com_pick == 1:
  com_choice = paper

else:
  com_choice = scissors

Computer = com_choice
print(f"Computer Chose: \n {Computer}") 

if Player == rock:
  if Computer == paper:
    print("You Win.")

  elif Computer == scissors:
    print("You Win.")
  
  else:
    print("You Draw.")

if Player == paper:
  if Computer == paper:
      print("You Draw.")
  
  elif Computer == rock:
    print("You Win.")
  
  else:
    print("You Loose.")
  
if Player == scissors:
  if Computer == rock:
    print("You Loose.")

  elif Computer == paper:
    print("You Win.")

else:
  print("You Win.")

