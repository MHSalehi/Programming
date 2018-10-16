#Introduction
print ("\n")
p_name = input("What is your name? " )
input("\n\nWelcome to the Text Trials, " + p_name + "." " You must navigate the following challenges to earn your freedom. Good luck!" + "\n\nPress any key to begin...")

#Room 1
print ("\n\nYou wake in a damp, dimly lit cell. Rats scurry for cover through an open door as your rise to your feet.\n\nWhat do you do?")
#Room 1 Options d1
d1 = ["1) Examine your surroundings.", "2) Exit through the door."]
print (*d1, sep = "\n")
while True:
    choice = input("Choice: ")
    if choice.isdigit() and int(choice) <= len(d1) and choice != 0:
        break
    else:
        print("That isn't a valid choice. Please try again.")
        continue

#Examine Room 1 d1
if int(choice) == 1:
    print ("\nThe room is lit by a single low-burning torch, resting in its wall fixture. A tiny vertical window slit on one wall indicates that it is nightime outside. You spot a mouldy hunk of bread lying on the floor in the corner of the cell which appears to be what attracted the rats.\n\nWhat do you do?")
#Room 1 Options d2
    d2 = ["1) Take the torch.", "2) Pick up the mouldy bread.", "3) Exit the through the door."]
    print (*d2, sep = "\n")
    while True:
        choice = input("Choice: ")
        if choice.isdigit() and int(choice) <= len(d2) and choice != 0:
            break
        else:
            print("That isn't a valid choice. Please try again.")
            continue

#Exit Room 1 d1
if int(choice) == 2:
    print("\nYou step out into a stone hallway. To the East the way is lit by wall fixtures. To the West your view of the hallway disappears into darkness.\nWhat do you do?")
    d3 = ["1) Go East.", "2) Go West.", "3) Go back into your cell."]
    print(*d3, sep = "\n")
    while True:
        choice = input("Choice: ")
        if choice.isdigit() and int(choice) <= len(d3) and choice != 0:
            break
        else:
            print("That isn't a valid choice. Please try again.")
            continue



#Take torch
if int(choice) == 1:
    print ("\nYou reach up and pull the torch from its fixture. Light surrounds you.\nWhat do you do?")
    del d2[0]
    print (*d2, sep = "\n")
    choice = input("Choice: ")
    while True:
        if choice.isdigit() and int(choice) <= len(d2) and choice != 0:
            break
        else:
            print("That isn't a valid choice. Please try again.")
            continue

#Take Mouldy Bread
if int(choice) == 2:
    print ("\nYou pick up the bread and stow it in your pocket.")
    del d2[1]
    print (*d2, sep = "\n")

#Defining Choice Checker Function
def choice_check(var):
    while True:
        if var.isdigit() and int(var) <= len(d2) and var != 0:
            break
        else:
            print("That isn't a valid choice. Please try again.")
            continue
