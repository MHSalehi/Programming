# ----------------------------------------------------------------------------------------------------------------------
# Class 5 -  Dictionaries (Part 2)
# ----------------------------------------------------------------------------------------------------------------------

# my_dict = {"item1": 4, "item3": 5, "item2": 6}
# new_dict = {key: value*2 for key, value in my_dict.items()}
#
#
#
#
# try:
#     userInput = input("Enter number >0 and <10.")
# except userInput >= 10 and = 0:     #  or, except ZeroDivisionError:  or, except ValueError:
#     print("You can't do that.")
#

# ----------------------------------------------------------------------------------------------------------------------
# Class 5 -  Peer Programming
# ----------------------------------------------------------------------------------------------------------------------

# Player stats ---------------------------------------------------------------------------------------------------------

import random

FlyAbility = 0
StealthAbility = 0

invPlayer = {"Daggers": 0, "BluePotions": 0, "GoldenFeathers": 0, "Manuscripts": 0}

items = ["Daggers", "BluePotions", "GoldenFeathers", "Manuscripts", "Twig", "Bag of holding", "Sack of gold", "Elixir of eternal life"]
allowedItems = ["Daggers", "BluePotions" ,"GoldenFeathers", "Manuscripts"]

while True:
    while True:
        userInput = input ("Which direction to travel (n,s,e,w)?").lower()
        if userInput not in ["n","s","e","w"]:
            print("You can't go that way.")
            continue
        else:
            break
    randomItem = items[(random.randint (0,len(items)-1))]
    if randomItem not in ["Twig", "Bag of holding", "Sack of gold"]:
        print("You find " + str(randomItem))
    elif randomItem  in ["Elixir"]:
        print("You find an " + str(randomItem))
    else:
        print("You find a " + str(randomItem))


    if randomItem not in allowedItems:
        print("You don't think it's valuable and toss it aside.")

# Permitted items ------------------------------------------------------------------------------------------------------
    else:
        userInput = input("Do you wish to pick it up? ").lower()
        if userInput in ["y", "yes", "yeah"]:
            print("You stash it in your inventory.")
            for key, value in invPlayer.items():
                if key == randomItem:
                #    key: value += 1
                    invPlayer[key] += 1
                    print(invPlayer + "\t")
            if randomItem in ["BluePotions"]:
                if StealthAbility <= 5:
                    StealthAbility += 1
                    print("Your stealth ability has increased by +1.")
                    print("Stealth ability: " + str(StealthAbility))
                else:
                    print("Your stealth ability is already maxed.")
                    print("Stealth ability: " + str(StealthAbility))

            if randomItem in ["GoldenFeathers"]:
                if FlyAbility <= 5:
                    FlyAbility += 1
                    print("Your fly ability has increased by +1.")
                    print("Fly ability: " + str(FlyAbility))
                else:
                    print("Your fly ability is already maxed.")
                    print("Fly ability: " + str(FlyAbility))
        else:
            print("You toss it aside.")