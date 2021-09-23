import random

def loot(luck, genCharacter):
    lootChance = random.randint(0, 5)
    if luck < lootChance:
        print("\n ******LOOT********")
        print("HAHA Pas de bol! Aucun loot!")

    else:
        tableNum = random.randint(0, 3)
        lootTableList = ["items", "defense", "magic", "attack"]
        itemType = lootTableList[tableNum]
        file = open(itemType)
        lines = file.readlines()

        print("\n ****** LOOT ******")
        print("L'enemie a laisse un(e)....")

        item = random.randint(0, len(lines) - 1)

        itemLine = lines[item]
        splitItemLine = itemLine.split(",")

        name = splitItemLine[0]
        value = int(splitItemLine[1])

        print(name)

        if itemType == "attack":
            genCharacter.setAttack(genCharacter.getAttack() + value)
            print("Attack augmente...")
            print(genCharacter.getAttack())

        elif itemType == "defense":
            genCharacter.setDefense(genCharacter.getDefense() + value)
            print("Defense augmente...")
            print(genCharacter.getDefense())

        elif itemType == "magic":
            genCharacter.setMagic(genCharacter.getMagic() + value)
            print("Attaque magique augmente...")
            print(genCharacter.getMagic())

        else:

            if splitItemLine[2] == "luck":
                genCharacter.setLuck(genCharacter.getLuck() + value)
                print("Chance augmente...")
                print(genCharacter.getLuck())

            elif splitItemLine[2] == "health":
                genCharacter.setHealth(genCharacter.getHealth() + value)
                print("Hp augmente...")
                print(genCharacter.getHealth())


