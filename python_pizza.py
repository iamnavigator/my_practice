print("Welcome to PythonPizza")
bill = 0
pizza = input("Which pizza size would you like to order: 's', 'm', 'l' \n").lower()
if pizza == "s":
    bill = 15
    pepperoni = input("Would you like to add pepperoni: 'y' or 'n' \n").lower()
    if pepperoni == "y":
        bill += 1
    cheese = input("would you like extra cheese: 'y' or 'no' \n").lower()
    if cheese == "y":
        bill += 1
        print(f"your final bill is {bill}")
    else:
        print(f"your final bill is {bill}")
elif pizza == "m":
    bill = 20
    pepperoni = input("Would you like to add pepperoni: 'y' or 'n' \n").lower()
    if pepperoni == "y":
        bill += 3
    cheese = input("would you like extra cheese: 'y' or 'n' \n").lower()
    if cheese == "y":
        bill += 1
        print(f"your final bill is {bill}")
    else:
        print(f"your final bill is {bill}")
elif pizza == "l":
    bill = 25
    pepperoni = input("Would you like to add pepperoni: 'y' or 'n' \n").lower()
    if pepperoni == "y":
        bill += 3
    cheese = input("would you like extra cheese: 'y' or 'n' \n").lower()
    if cheese == "y":
        bill += 1
        print(f"your final bill is {bill}")
    else:
        print(f"your final bill is {bill}")
