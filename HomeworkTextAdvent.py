weapons = ["sword", "dagger"]
fightMode = False

while True:

	usr=input("Where to? ")

	if usr in ["n", "north"]:
		print("Oh this looks like trouble!")
	elif usr in ["e", "east", "s", "south", "w", "west"]:
		print("Nothing there.")
		continue
	else:
		print("This is not a valid direction.")
		continue

	usr = input("Will you fight?").lower()
	if usr in ["yes", "y", "hell yeah"]:
		fightMode = True

		while True:
			if fightMode:
				usr = input("which weapon you want to use: ")
				usrp = usr.split(" ") #list

				for word in usrp:
					if word not in weapons:
						print("please choose a weapon you actually have")
						continue

			if word == "sword":
				print("With this you do 5 damage. On we go!")
				break
			elif word == "dagger":
				print("With this you do 3 damage. On we go!")
				break
			continue








# Further code for the fight ...





