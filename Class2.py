# count = 0
# while  count < 9:
#     print (count)
#
#     if count == 15:
#         print ("Target reached.")
#         break
#     else:
#         print ("Counting up...")
#         count += 1
#         continue



# word = "python"
#
# for l in word:
#     if l == "t":
#         continue
#     print(l, end='')
#
# print()



listLength = 0
LucasFoods = []

while len(LucasFoods) <=3:
    userFood = input("\nEnter a food: ")
    LucasFoods.append(userFood)
    print("\nCurrent food list:\r", *LucasFoods, sep = "\n")
    continue
else:
    print("\nThat's enough food items.")

# Query final list
changeList = input("Do you wish to change an item Y/N? ")
if changeList in ["Y", "y", "yes", "Yes"]:
    while True:
        changeItem = input("Which item do you want to change? ")
        if changeItem not in LucasFoods:
            print("That isn't on the list. please try again.")
        else:
            break
# Search for unwanted food in list
for food in LucasFoods:
    if food == changeItem:
# Delete item/replace?
        while True:
            itemQuery = input("Do you wish to remove or replace the item? ")
            if itemQuery not in ["Remove", "remove", "Replace", "replace"]:
                print("Invalid response. Please try again. ")
            else:
                break
if itemQuery in ["Remove", "remove"]:
    LucasFoods.remove(changeItem)
if  itemQuery in ["Replace", "replace"]:
    newItem = input("What do you want to replace it with? ")
    LucasFoods[LucasFoods.index(changeItem)] = newItem

# Print final list
print("\nFinal food list:\r", *LucasFoods, sep="\n")

# if changeItem


# count = 0
# symbol = ["*"]
# while count < 11:
#     print(*symbol)
#     symbol.append("*")
#     count += 1