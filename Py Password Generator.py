#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

l = 0
let = 0
n = 0
num = 0
s = 0
sym = 0 

for letter in letters:
  if nr_letters == 1:
    l = random.sample(letters, 0)
    
  elif nr_letters == 2:
    l = random.sample(letters, 1)

  elif nr_letters == 3:
    l = random.sample(letters, 2)

  elif nr_letters == 4:
    l = random.sample(letters, 3)

  elif nr_letters == 5:
    l = random.sample(letters, 4)

  elif nr_letters == 6:
    l = random.sample(letters, 5)

  elif nr_letters == 7:
    l = random.sample(letters, 6)

  elif nr_letters == 8:
    l = random.sample(letters, 7)

  elif nr_letters == 9:
    l = random.sample(letters, 8)

  elif nr_letters == 10:
    l = random.sample(letters, 9)

  elif nr_letters == 11:
    l = random.sample(letters, 10)

  elif nr_letters == 12:
    l = random.sample(letters, 11)

  elif nr_letters == 13:
    l = random.sample(letters, 12)

  elif nr_letters == 14:
    l = random.sample(letters, 13)

  elif nr_letters == 15:
    l = random.sample(letters, 14)

  elif nr_letters == 16:
    l = random.sample(letters, 15)

  elif nr_letters == 17:
    l = random.sample(letters, 16)

  elif nr_letters == 18:
    l = random.sample(letters, 17)

  elif nr_letters == 19:
    l = random.sample(letters, 18)

  elif nr_letters == 20:
    l = random.sample(letters, 19)

  elif nr_letters == 21:
    l = random.sample(letters, 20)

  elif nr_letters == 22:
    l = random.sample(letters, 21)

  elif nr_letters == 23:
    l = random.sample(letters, 22)

  elif nr_letters == 24:
    l = random.sample(letters, 23)

  elif nr_letters == 25:
    l = random.sample(letters, 24)

  elif nr_letters == 26:
    l = random.sample(letters, 25)

  elif nr_letters == 27:
    l = random.sample(letters, 26)

  elif nr_letters == 28:
    l = random.sample(letters, 27)

  elif nr_letters == 29:
    l = random.sample(letters, 28) 

  elif nr_letters == 30:
    l = random.sample(letters, 29)

  elif nr_letters == 31:
    l = random.sample(letters, 30)

  elif nr_letters == 32:
    l = random.sample(letters, 31)

  elif nr_letters == 33:
    l = random.sample(letters, 32)

  elif nr_letters == 34:
    l = random.sample(letters, 33)

  elif nr_letters == 35:
    l = random.sample(letters, 34)

  elif nr_letters == 36:
    l = random.sample(letters, 35)

  elif nr_letters == 37:
    l = random.sample(letters, 36)

  elif nr_letters == 38:
    l = random.sample(letters, 37)

  elif nr_letters == 39:
    l = random.sample(letters, 38)

  elif nr_letters == 40:
    l = random.sample(letters, 39)

  elif nr_letters == 41:
    l = random.sample(letters, 40)

  elif nr_letters == 42:
    l = random.sample(letters, 41)

  elif nr_letters == 43:
    l = random.sample(letters, 42)

  elif nr_letters == 44:
    l = random.sample(letters, 43)

  elif nr_letters == 45:
    l = random.sample(letters, 44)

  elif nr_letters == 46:
    l = random.sample(letters, 45)

  elif nr_letters == 47:
    l = random.sample(letters, 46)

  elif nr_letters == 48:
    l = random.sample(letters, 47)

  elif nr_letters == 49:
    l = random.sample(letters, 48)

  elif nr_letters == 50:
    l = random.sample(letters, 49)

  elif nr_letters == 51:
    l = random.sample(letters, 50)

  elif nr_letters == 52:
    l = random.sample(letters, 51)                
  
  let = ''.join(l)
# print(let)

for symbol in symbols:
  if nr_symbols == 1:
    s = random.sample(symbols, 0)
    
  elif nr_symbols == 2:
    s = random.sample(symbols, 1)

  elif nr_symbols == 3:
    s = random.sample(symbols, 2)

  elif nr_symbols == 4:
    s = random.sample(symbols, 3)

  elif nr_symbols == 5:
    s = random.sample(symbols, 4)

  elif nr_symbols == 6:
    s = random.sample(symbols, 5)

  elif nr_symbols == 7:
    s = random.sample(symbols, 6)

  elif nr_symbols == 8:
    s = random.sample(symbols, 7)

  elif nr_symbols == 9:
    s = random.sample(symbols, 8)

  elif nr_symbols == 10:
    s = random.sample(symbols, 9)

  sym = ''.join(s)
# print(sym)

for number in numbers:
  if nr_numbers == 1:
    n = random.sample(numbers, 0)
    
  elif nr_numbers == 2:
    n = random.sample(numbers, 1)

  elif nr_numbers == 3:
    n = random.sample(numbers, 2)

  elif nr_numbers == 4:
    n = random.sample(numbers, 3)

  elif nr_numbers == 5:
    n = random.sample(numbers, 4)

  elif nr_numbers == 6:
    n = random.sample(numbers, 5)

  elif nr_numbers == 7:
    n = random.sample(numbers, 6)

  elif nr_numbers == 8:
    n = random.sample(numbers, 7)

  elif nr_numbers == 9:
    n = random.sample(numbers, 8)


  num = ''.join(n)
# print(num)
print(let + sym + num )


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2