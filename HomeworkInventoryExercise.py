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

userChoice = None
container = None

print("\nYou discover a chest. ")
while True:
    userChoice = input("\nWhat do you wish to do?\n\n1) Access your backpack.\n2) Open the chest."
                            "\n3) Check your stats.\n4) Rest for the night.\nChoice: ")
    if userChoice not in ["1", "2", "3", "Stats", "4"]:
        print("That isn't a valid choice. Please try again.")
    else:
        break

if userChoice == str("1"):
    container = invPlayer
if userChoice == str("2"):
    container = invChest01


# ----------------------------------------------------------------------------------------------------------------------
# Container invChest01 is active                                                                                    X
# ----------------------------------------------------------------------------------------------------------------------

if container == invChest01:
    print("\n===== Chest Contents: =====")
    for category, details in container.items():
        if category == "Weapons":
            print(category + "\t"*2, details)       # Better method to align items + quantities to their own columns?
        else:
            print(category + "\t", details)


# ----------------------------------------------------------------------------------------------------------------------
# Query which item to take from invChest01 and add it to player backpack
# ----------------------------------------------------------------------------------------------------------------------

# ---------------------- Broken Method ---------------------------------------------------------------------------------

# invTest = []
#
# tempDict = {}
#
# if container == invChest01:
#     for key in container.keys():
#         invTest.append(key.lower())
#
#     print("\ninvTest = ", invTest)
#
# while True:
#     userChoice = input("\nDo you wish to select an item or move on? ")
#     if container == invChest01 and userChoice.lower() not in invTest:
#         print("That didn't make sense. Please try again.")
#     else:
#         print("Item found, transferring...")
#         invPlayer.update(invChest01[userChoice])
#         break
#
# print(invPlayer
      

# ---------------------- Working Method --------------------------------------------------------------------------------

    userQuery = input("Which item do you want to take? ")

    for category, item in invChest01.items():
        if userQuery in item:
            invPlayer.update({category: {**invPlayer.get(category, {}),
                                         **{userQuery: item[userQuery]}}
                              }
                             )

            print("\nAdding item to backpack.")
# ----------------------------------------------------------------------------------------------------------------------
# Delete chosen item from chest    # Not working properly - "Dictionary changed size during iteration"              X
# ----------------------------------------------------------------------------------------------------------------------
    for category, item in invChest01.items():
        if userQuery in item:
            del invChest01[category]
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
