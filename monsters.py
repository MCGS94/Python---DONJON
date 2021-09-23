
import random
import math

class enemy:
    def __init__(self, Ehealth, Eattack, Echance, Ename):
        self.health = Ehealth
        self.attack = Eattack
        self.chance = Echance
        self.name = Ename

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getChance(self):
        return self.chance

    def getName(self):
        return self.name

    def setHealth(self, newHealth):
        self.health = newHealth

    def setAttack(self, newAttack):
        self.attack = newAttack

    def setChance(self, newChance):
        self.chance = newChance

    def setName(self, newName):
        self.name = newName


class boss(enemy):
    def __init__(self, Ehealth, Eattack, Echance, Ename,):
        super().__init__(Ehealth, Eattack, Echance, Ename)



def enemyGen(levelBoss):
    temp = []
    file = open("MONSTERS")
    lines = file.readlines()
    monster = lines[random.randint(0, len(lines) - 1)][:-1]
    file.close

    if levelBoss == False:
        health = random.randint(50, 100)
        attack = random.randint(5, 10)
        chance = random.randint(1, 10)

        return enemy(health, attack, chance, monster)

    else:
        health = random.randint(200, 250)
        attack = random.randint(20, 40)
        chance = random.randint(1, 8)

        return boss(health, attack, chance, "Boss " + monster)


