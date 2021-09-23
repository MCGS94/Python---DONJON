from pprint import pprint
import random
import math

def enemyAttack(hitChance, attackValue, name, defense):
    print(name, "se prepare pour une attaque...")
    hit = random.randint(0,10)
    if hitChance >= hit:
        print("\nl'enemie vous a touché!")
        loss = attackValue - defense
        print(f'Vous avez perdu {loss} health')
        return math.ceil(loss)
    else:
        print("\nL'enemie a raté!!")
        return 0

def hitChance(luck):
    hit = random.randint(0,5)
    if luck < hit:
        print("Raté")
        return False
    else:
        print ("Touché")
        return True

def isDead(health):
    if health < 1:
        return True
    else:
        return False

def gameOver(enemyDead):
    if enemyDead == True:
        print("\nLet's go mes amis!\n")
    else:
        print("\nVous n'avez plus d'HP")
        print("Une prochaine fois peut_etre!! Bye!")

def battle(genEnemy, genCharacter):
    print("\nQu'est ce que c'est?")
    print("\nC'est un(e) ", genEnemy.getName(), "!\n")
    print("Voici ses stats\n")
    pprint(vars(genEnemy))

    battle = True

    while battle == True:

        print("\n1.Attack Normal \n2.Atack Magique")
        choice = input()

        while choice != "1" and choice != "2":
            print("Erreur, recommencez!")
            print("\n1.Attack Normal \n2.Attack Magique")
            choice = input()

        if choice == "1":
            damage = genCharacter.getAttack()

        elif choice == "2":
            damage = genCharacter.getMagic()

        print(".............")

        hit = hitChance(genCharacter.getLuck())

        if hit == True:
            genEnemy.setHealth(genEnemy.getHealth() - damage)
            print("Tu as attaqué l'ennemie!!!")
            print("Pv ennemie....", genEnemy.getHealth())

        else:
            print("Tu as raté!")

        enemyDead = isDead(genEnemy.getHealth())

        if enemyDead == False:
            genCharacter.setHealth(
                genCharacter.getHealth() - enemyAttack(genEnemy.getChance(), genEnemy.getAttack(), genEnemy.getName(),
                                                       genCharacter.getDefense()))

            characterDead = isDead(genCharacter.getHealth())

            if characterDead == True:
                battle = False
                return False

            else:
                print("Il te reste", genCharacter.getHealth()," Hp")

        else:
            battle = False
            print("\nTu as vaincu l'ennemie!")

            return True