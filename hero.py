import random
import time

class hero:
    def __init__(self, Hname, Hhealth, Hattack, Hdefense, Hmagic, Hluck,):
        self.name = Hname
        self.health = Hhealth
        self.attack = Hattack
        self.defense = Hdefense
        self.magic =Hmagic
        self.luck =Hluck

    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getDefense(self):
        return self.defense
    def getMagic(self):
        return self.magic
    def getLuck(self):
        return self.luck


    def setName(self, newHealth):
        self.health = newHealth
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setDefense(self, newDefense):
        self.defense = newDefense
    def setMagic(self, newMagic):
        self.magic = newMagic
    def setLuck(self, newLuck):
        self.luck = newLuck


def createChar():

    heroName = input("Wesh! Wesh! D'abord comment tu t'appelles toi??\n")
    print("Bienvenue à toi, notre sauveur,", heroName, "!!!!")

    a = input("\nBon, tu es plutot Guerrier (1) ou Mage(2)?...\n")
    while a != "1" and a != "2":
        print("Tu te fou de moi?!!! Choisi bien...")
        a = input("Bon, tu es Guerrier (1) ou Mage(2)?...")

    if a == "1":
        heroAttack = 10
        heroMagic = 5
        heroDefense = 3
        heroHealth = 120

    elif a == "2":
        heroAttack = 5
        heroMagic = 10
        heroDefense = 3
        heroHealth = 100

    print("Voyons voir si tu as de la chance!")
    print("La chance permet de determiner ta chance de toucher l'enemie et d'avoir du loot.")
    b = input("\nAppuie sur Entrer!")
    print("\nKarma...")
    time.sleep(0.4)
    print("Karma...")
    time.sleep(0.4)
    print("Karma...")
    time.sleep(0.4)
    heroLuck = random.randint(0, 10)
    print("\nTu as", heroLuck, "chance(s) sur 10.\n")
    if heroLuck < 5:
        print("HAHA t'es dans la merde.")
    else:
        print("Peux faire mieu.")
    time.sleep(1.2)
    string = "\nNotre sauveur, votre role est de tuer le boss dans la salle du Boss."

    for char in string:
        print(char, end='')
        time.sleep(0.25)

    return (heroName,heroHealth, heroAttack,heroDefense, heroMagic, heroLuck)

