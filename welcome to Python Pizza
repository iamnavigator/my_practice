print("welcome to Python Pizza")
size = input("which size of pizza would you like s,m or l: ").lower()
if size == "s":
    bill = 15

elif size == "m":
    bill = 20

else:
    bill = 25

add_pepperoni = input("would you like to add pepperoni: y or n\n").lower()
if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
    
extra_cheese = input("would you like to add extra cheese: y or n\n").lower()
if extra_cheese == "y":
    bill += 1
    print(f"please pay {bill}")
else:
    print(f"please pay {bill}")
