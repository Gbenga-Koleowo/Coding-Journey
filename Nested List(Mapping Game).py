row1 = ["⬜️","️⬜️","️⬜️"] 
row2 = ["⬜️","️⬜️","️⬜️"]
row3 = ["⬜️","️⬜️","️⬜️"]

map = [row1, row2, row3]

position = input("what position")
split_position = list(str(position))

a = 0
b = 0

a = int(split_position[0])
b = int(split_position[1])


if a == 1:
    if b == 1:
        row1[0]= "X"
    elif b == 2:
        row2[0] = "X" 
    else:
        row3[0] = "X"

if a == 2:
    if b == 1:
        row1[1] = "X"
    elif b == 2:
        row2[1] = "X"
    else:
        row3[1] = "X"
    
if a == 3:
    if b == 1:
        row1[2] = "X"
    elif b == 2:
        row2[2] = "X"
    else:
        row3[2] = "X"


     

print(f"{row1}\n{row2}\n{row3}\n")
