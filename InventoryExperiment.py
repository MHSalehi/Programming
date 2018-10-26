'''while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
'''
'''
print ("1 2 or 3")
while True:
    choice = (input("Choice: "))
    try:
        if choice.isdigit() == True:
            break
        # ValueError:
        #    print ("That isn't a valid choice.")
        #    continue
    except choice.isalpha() == True:
        print ("Repeat.")
        continue

 #and choice != 0:
'''

# Defining Choice Checker Function

#def choice_check(choice):
playerInv = ["Sword", "Shield", "Health potion", "Water flask", "Torch"]
chestInv = ["Whetstone", "Rope", "Flint"]

choice = None

while True:
    choice = input("Select active array ('1' or '2'): ")
    if choice not in ["1","2"]:
        print("That isn't a valid choice. Please try again.")
    else:
        break

# if choice == str("1"):
#     arrayLength = len(arr1)
# if choice == str("2"):
#     arrayLength = len(arr2)
if choice == str("1"):
    activeArray = playerInv
if choice == str("2"):
    activeArray = chestInv

print("\r",*activeArray, sep="\n")

selectItem = input("\nSelect a list item: ")
if len(activeArray) < len(selectItem) and selectItem != 0:
    print(activeArray)

# choice = input("Choice? ")
# choice_check(choice)
# print ("Passed.")
