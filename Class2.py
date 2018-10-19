'''
while  count < 3
    print (count)

    if count == 15:
        print ("Target reached.")
        breakaasdasfdssd
    else:
        print ("Counting up...")
        count += 1
        continue


word = "python"

for l in word:
    if l == "t":
        continue
    print(l, end='')

print()

###

listLength = 0
LucasFoods = []

while len(LucasFoods) <=4:
    userFood = input("\n Enter a food: ")
    LucasFoods.append(userFood)
    print(*LucasFoods, sep = "\n")
    continue
else:
    print("\n That's enough food items.")

changeList = input("Do you wish to change an item Y/N? ")
# if changeList == N:
#     continue
if changeList in ["Y", "y", "yes"]:
    changeItem = input("Which food do you want to replace?" )
    #Search for unwanted food in list
    for food in LucasFoods:
        if food == changeItem:
            replaceItem = input("What do you want to replace it with? ")
            LucasFoods[int(food)] = replaceItem
print(*LucasFoods)

'''

count = 0
symbol = ["*"]
while count < 11:
    print(*symbol)
    symbol.append("*")
    count += 1
