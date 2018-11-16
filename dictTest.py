# ----------------------------------------------------------------------------------------------------------------------
# Define Player Stats
# ----------------------------------------------------------------------------------------------------------------------

# health = 80
# mana = 80
# sanity = 100
# encumberance = 45

statsPlayer = {"Health": 80, "Mana": 80, "Sanity": 100, "Encumberance": 45}


playerRest = False

#invDict = {}


# ----------------------------------------------------------------------------------------------------------------------
# Define Container Contents  (Nested dictionaries in use currently)
# ----------------------------------------------------------------------------------------------------------------------

# ----------- Legitimate player inventory ---(temp disabled)------------------------------------------------------------

# invPlayer = {"Weapons": {"Tarnished Sword": "Blunt", "Wooden Shield": "Damaged"},
#              "Consumables": {"Health potion": 1, "Water flask": "Empty"},
#              "Equipment": {"Torch": 1}}

# ----------- Chest01 contents -----------------------------------------------------------------------------------------

invChest01 = {"Equipment": {"Whetstone": 1, "Rope": 1, "Flint": 1},
              "Consumables": {"Mana potion": 2}}

# ----------- Cheat full player inventory ---(for testing)--------------------------------------------------------------

invPlayer = {"Weapons": {"Tarnished Sword": "Blunt", "Wooden Shield": "Damaged"},
             "Consumables": {"Health potion": 1, "Water flask": "Empty", "Mana potion": 2},
             "Equipment": {"Torch": 1, "Whetstone": 1, "Flint": 1}}


# ----------------------------------------------------------------------------------------------------------------------
# Determine active container
# ----------------------------------------------------------------------------------------------------------------------

# userChoice = None
# container = None

print("\nYou discover a chest. ")
while True:                         ###### YOU CAN USE int(input()) here and 'if userChoice == 1' later but I guess you don't because you allow the player to write 'Stats' too?
    userChoice = input("\nWhat do you wish to do?\n\n1) Access your backpack.\n2) Open the chest."
                            "\n3) Check your stats.\n4) Rest for the night.\nChoice: ")
    if userChoice not in ["1", "2", "3", "Stats", "4"]:
        print("That isn't a valid choice. Please try again.")
    else:
        break

# if userChoice == str(1):    # CHANGED HERE.The correct use is str(int) and int(str). You had str("1") which is str(str). Was not going to cause an issue as you asked to convert a string to string, but for coding practice.
#     container = invPlayer
if userChoice == str(2):       # Is this check needed??     - was thinking about having other containers available, probably not needed, could use 'else'.
    container = invChest01


# ----------------------------------------------------------------------------------------------------------------------
# Container invChest01 is active                                                                                    X
# ----------------------------------------------------------------------------------------------------------------------

if userChoice == str(2):   ########  WHY NOT USE 'if userChoice == str("1') directly and not do the previous if check? Why do you take an extra step to check?
    print("\n===== Chest Contents: =====")
    for category, details in invChest01.items():
        if category == "Weapons":               #### Not sure what you want to do here but giving some extra hints about presentation of dict items below:
            for weapon,det in details.items():  # to access the values of the nested dictionary (details is your second dictionary so you can do details.items())
                print(weapon + "\t", det)
            # print(category + "\t"*2, details)       # Better method to align items + quantities to their own columns?
        else:
            for weapon,det in details.items():  # to access the values of the nested dictionary (details is your second dictionary so you can do details.items())
                print(weapon + "\t", det)       
             


# ---------------------- Working Method --------------------------------------------------------------------------------

    print(invPlayer)
    userQuery = input("Which item do you want to take? ")

    for key,item in invChest01.items():
        for k in item:
            if k == userQuery: 
                invPlayer[key][userQuery] += item[k]    ##### THIS IS EASIER

            # invPlayer.update({category: {**invPlayer.get(category, {}),
            #                              **{userQuery: item[userQuery]}}
            #                   }
            #                  )

            print("\nAdding item to backpack.")
    print(invPlayer)
    


# ----------------------------------------------------------------------------------------------------------------------
# Delete chosen item from chest    # Not working properly - "Dictionary changed size during iteration"              X
# ----------------------------------------------------------------------------------------------------------------------
    for category, item in invChest01.items():
        if userQuery in item.keys():
            del item[userQuery]
            print("\nRemoving item from chest... ")


# ------------------------ Print updated inventories -------------------------------------------------------------------

    print("\n===== Backpack Contents: =====")
    for category, details in invPlayer.items():
        if category == "Weapons":
            print(category + "\t"*2, details)
        else:
            print(category + "\t", details)

    print("\n===== Chest Contents: =====")
    for category, details in invChest01.items():
        print(category + "\t", details)


# ----------------------------------------------------------------------------------------------------------------------
# Query to take another item
# ----------------------------------------------------------------------------------------------------------------------

#>>>>>>>>>>>>>>>>>

# ----------------------------------------------------------------------------------------------------------------------
# Container invPlayer is active
# ----------------------------------------------------------------------------------------------------------------------

if container == invPlayer:     
    print("\n===== Backpack Contents: =====")
    for category, details in container.items():
        if category == "Weapons":
            print(category + "\t"*2, details)       # Better method to align items + quantities to their own columns?
        else:
            print(category + "\t", details)

# ----------------------------------------------------------------------------------------------------------------------
# Query use backpack item
# ----------------------------------------------------------------------------------------------------------------------

    userQuery = input("\nWhich item do you want to use? ")
    for category, item in invPlayer.items():
        if userQuery in item:

# Whetstone ------------------------------------------------------------------------------------------------------------
            if userQuery == "Whetstone":
                print("\nYou use the whetstone to sharpen your sword.")
                invPlayer["Weapons"]["Tarnished Sword"] = "Sharp"

                print("\n===== Backpack Contents: =====")
                for category, details in container.items():
                    if category == "Weapons":
                        print(category + "\t" * 2,
                              details)  # Better method to align items + quantities to their own columns?
                    else:
                        print(category + "\t", details)
                break


# >>>>>>>>>>>>>>>>> Potion usage is not updating statsPlayer dictionary                                             X

# Health potion --------------------------------------------------------------------------------------------------------
        if userQuery == "Health potion":
            print("You drink the Health potion.")
            if statsPlayer["Health"] >= 80:
                statsPlayer["Health"] = 100
                break
            if statsPlayer["Health"] < 80:
                statsPlayer["Health"] += 20
                break

# Mana potion ----------------------------------------------------------------------------------------------------------
        if userQuery == "Mana potion":
            print("You drink the Mana potion.")
            if statsPlayer["Mana"] >= 80:
                statsPlayer["Mana"] = 100
                del invPlayer[category]
# Print updated player inventory ---------------------------------------------------------------------------------------
                for category, details in container.items():
                    if category == "Weapons":
                        print(category + "\t" * 2,
                              details)  # Better method to align items + quantities to their own columns?
                    else:
                        print(category + "\t", details)
                break
            if statsPlayer["Mana"] < 80:
                statsPlayer["Mana"] += 20
                break

# ----------------------------------------------------------------------------------------------------------------------
# Delete item from backpack    # Not working     "RuntimeError: Dictionary changed size during iteration"           X
# ----------------------------------------------------------------------------------------------------------------------
#           del invPlayer[category]

# ----------------------------------------------------------------------------------------------------------------------
# Print hero stats if potion used
# ----------------------------------------------------------------------------------------------------------------------

    if userQuery in ["Health potion", "Mana potion"]:
        print("\n===== Hero Stats: =====")
        for category, details in statsPlayer.items():
            if category not in "Encumberance":
                print(category + "\t" * 3, details)  # Better method to align items + quantities to their own columns?
            else:
                print(category + "\t", details)
                break


# ----------------------------------------------------------------------------------------------------------------------
# Player checks stats
# ----------------------------------------------------------------------------------------------------------------------

if userChoice in ["3", "Stats"]:
    print("\nYou take a moment to assess your condition:")
    print("\n===== Hero Stats: =====")
    for category, details in statsPlayer.items():
        if category not in "Encumberance":
            print(category + "\t"*3, details)       # Better method to align items + quantities to their own columns?
        else:
            print(category + "\t", details)


# ----------------------------------------------------------------------------------------------------------------------
# Player chooses to rest
# ----------------------------------------------------------------------------------------------------------------------

if userChoice in ["4"]:
    playerRest = True

# ----------------------------------------------------------------------------------------------------------------------
# End game (player rests)
# ----------------------------------------------------------------------------------------------------------------------

if playerRest:
    print("\n\nYou settle down for some much-earned rest.\n\nTo be continued...")

# ----------------------------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------------------------