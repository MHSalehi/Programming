


l = ["sword", "dagger"]

while True:

    user = input("What weapon?")

    userp = user.split(" ") #list


    for word in userp:
        if word in l and word == "sword":
            print("You do 123 damage.")
        elif word in l and word == "dagger":
            print ("You do 12 damage.")
        else:
            print("Please choose a weapon you are carrying.")



print (str(l.index(i)+1) + ")" + i)