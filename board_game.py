print("Welcome to the Board Game")

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

# map is used to create variable not function
map = [row1, row2, row3]
# to create 3 x 3 board
print(f"{row1}\n{row2}\n{row3}\n")

position = input("please enter your choice to place 'x' in the board:")

horizontal = int(position[0])
vertical = int(position[1])
horizontal_input = map[horizontal - 1]
horizontal_input[vertical - 1] = "x"

print(f"{row1}\n{row2}\n{row3}\n")