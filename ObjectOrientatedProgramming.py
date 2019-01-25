class Shark:
    kind = "mammal"

    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

    def move(self):
        self.x = self.x+1
        print(self.kind)


sharknado = Shark(13, 25)
print (sharknado.x)
sharknado.move()
print (sharknado.x)


class Enemy:
    weapons_list = {"guns": 4, "mo' guns": 6}

    def __init__(self, clan, name, special):
        self.clan = clan
        self.name = name
        self.special = special

    def descript(self, desc):
        self.desc = desc

    def status(self):
        print(self.desc)


Enemy1 = Enemy("Red Fins", "Sharkfin", "Flipper Cut")
Enemy2 = Enemy("Blue Shells", "Sharktale", "Tail Slap")
Enemy1.descript("Sharkfin is buffed.")

Enemy1.status()

print("\nName = %s, Clan = %s, Special Ability = %s, Gun list = %s" %(Enemy1.name, Enemy1.clan, Enemy1.special, Enemy1.weapons_list))

#print("\nName = ", Enemy1.name, "\nClan = ", Enemy1.clan, "\nSpecial = ", Enemy1.special, "Gun list = ", Enemy1.weapons_list)
#print("\nName = ", Enemy2.name, "\nClan = ", Enemy2.clan, "\nSpecial = ", Enemy2.special, "Gun list = ", Enemy1.weapons_list)




# for i in range(2):
#     sharkfin + str(i) = Enemy("Clan" + str(i), "Name" + str(i), "Special" + str(i))

class