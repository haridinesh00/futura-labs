# Write a Python program that takes order from the user, generates the bill according to the following guidance and
# displays it to the user.Create and automatic pizza order program.Based on a user 's order, work out their final bill.
# Small Pizza: Rs .150 , Medium Pizza: Rs. 200, Large Pizza: Rs 250
# Pepperoni for Small Pizza: Rs. 20
# Pepperoni for Medium or Large Pizza: Rs. 30
# Extra cheese for any size pizza: Rs. 10

total = 0
choice = ""
while choice != "stop":
    print("Welcome to Dominoes!!")
    print("Menus : ")
    print("Small Pizza: Rs .150 , Medium Pizza: Rs. 200, Large Pizza: Rs 250")
    print("Pepperoni for Small Pizza: Rs. 20")
    print("Pepperoni for Medium or Large Pizza: Rs. 30")
    print("Extra cheese for any size pizza: Rs. 10 \n")
    inp = input("Please enter the size of the pizza: S for small, M for medium, L for large : ").lower()
    if inp == 's':
        total = total + 150
        confirm = input("Do you wish to add pepperoni? Enter Yes or No : ").lower()
        if confirm == "yes":
            total = total + 20
        cheese = input("Do you like to add extra cheese? Enter Yes or No : ").lower()
        if cheese == "yes":
            total = total + 10
    elif inp == 'm':
        total = total + 200
        confirm = input("Do you wish to add pepperoni? Enter Yes or No : ").lower()
        if confirm == "yes":
            total = total + 30
        cheese = input("Do you like to add extra cheese? Enter Yes or No : ").lower()
        if cheese == "yes":
            total = total + 10
    elif inp == 'l':
        total = total + 250
        confirm = input("Do you wish to add pepperoni? Enter Yes or No : ").lower()
        if confirm == "yes":
            total = total + 30
        cheese = input("Do you like to add extra cheese? Enter Yes or No : ").lower()
        if cheese == "yes":
            total = total + 10
    else:
        print("\nWrong choice entered, choose again!!\n")
        continue
    choice = input("Do you wish to add another pizza? Enter Yes to continue and Stop to Stop : ").lower()
print("Total is : Rs", total)
