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

def nameSetup():
    userInput = input("What is your name? ")
    while True:
        userInput = input("So your name is \'Rainbow Unicorn\' [Y/N]? ")
        if userInput.lower() not in ["y", "n"]:
            print("That isn't a valid answer.")
        elif userInput.lower() == "y":
            print("Good luck in your adventuring, noble Rainbow Unicorn.")
            break
        else:
            print("Good luck in your adventuring, NOT noble Rainbow Unicorn")
            break

def killPlayer():
    while True:
        userInput = input("That last feather broke your back. So sad. \n==== GAME OVER ====\nTry again [Y/N]?")
        if userInput.lower() not in ["y", "n"]:
            print("That isn't a valid answer.")
        elif userInput.lower() == "y":
            print("Better luck this time.")
            global FlyAbility
            FlyAbility = 0
            break
        else:
            print("Goodbye.")
            exit()

def encounter():

    while True:
        userInput = input("You come across 3 doors. Which one do you want to open [1,2,3]? ")
        if userInput not in ["1","2","3"]:
            print("That isn't a valid response. Please try again.")
        elif userInput in ["2"]:
            killPlayer()
        elif userInput in ["3"]:
            while True:
                userInput = input("You meet Cthulu. Do you:\n1.) Flee.\n2.) Eat your head.")
                if userInput not in ["1", "2"]:
                    print("That isn't a valid response. Please try again.")
                elif userInput == "1":
                    print("You are devoured as you run away.")
                    killPlayer()
                    break
                else:
                    print("You feel a strange sensation.")
                    break

FlyAbility = 0
StealthAbility = 0

invPlayer = {"Daggers": 0, "BluePotions": 0, "GoldenFeathers": 0, "Manuscripts": 0}

items = ["Daggers", "BluePotions", "GoldenFeathers", "Manuscripts", "Twig", "Bag of holding", "Sack of gold", "Elixir of eternal life"]
allowedItems = ["Daggers", "BluePotions" ,"GoldenFeathers", "Manuscripts"]

while True:                                 # Game running Loop
    nameSetup()
    encounter()
    while FlyAbility < 1:                   # Game over check loop
        while True:
            userInput = input ("\nWhich direction to travel (n,s,e,w)?").lower()
            if userInput not in ["n","s","e","w"]:
                print("You can't go that way.")
                continue
            else:
                break
        randomItem = items[(random.randint (0,len(items)-1))]
        if randomItem not in ["Twig", "Bag of holding", "Sack of gold"]:
            print("\nYou find " + str(randomItem))
        elif randomItem  in ["Elixir"]:
            print("\nYou find an " + str(randomItem))
        else:
            print("\nYou find a " + str(randomItem))


        if randomItem not in allowedItems:
            print("You don't think it's valuable and toss it aside.")

    # Permitted items ------------------------------------------------------------------------------------------------------
        else:
            userInput = input("Do you wish to pick it up? ").lower()
            if userInput in ["y", "yes", "yeah"]:
                print("\nYou stash it in your inventory.")
                for key, value in invPlayer.items():
                    if key == randomItem:
                        invPlayer[key] += 1

    # Print player inventory -----------------------------------------------------------------------------------------------
                        print("\n===== Player inventory: =====")
                        for k, v in invPlayer.items():  # to access the values of the nested dictionary (details is your second dictionary so you can do details.items())
                            print(k + "\t", v)

                if randomItem in ["BluePotions"]:
                    if StealthAbility < 5:
                        StealthAbility += 1
                        print("\nYour stealth ability has increased by +1.")
                        print("Stealth ability: " + str(StealthAbility))
                    else:
                        print("\nYour stealth ability is already maxed.")
                        print("Stealth ability: " + str(StealthAbility))

                if randomItem in ["GoldenFeathers"]:
                    if FlyAbility < 5:
                        FlyAbility += 1
                        print("\nYour fly ability has increased by +1.")
                        print("Fly ability: " + str(FlyAbility))
                    else:
                        print("\nYour fly ability is already maxed.")
                        print("Fly ability: " + str(FlyAbility))
            else:
                print("\nYou toss it aside.")
    killPlayer()


 #
 # if randomItem in ["GoldenFeathers"]:
 #                if FlyAbility < 5:
 #                    FlyAbility += 1
 #                    print("\nYour fly ability has increased by +1.")
 #                    print("Fly ability: " + str(FlyAbility))
 #                else:
 #                    print("\nYour fly ability is already maxed.")
 #                    print("Fly ability: " + str(FlyAbility))
 #        else:
 #            print("\nYou toss it aside.")
