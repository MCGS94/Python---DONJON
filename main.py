from pprint import pprint
import time
import Fight
import hero
import monsters
import loot
import map

dirs = (0,0,0,0) #un tuple (ordonné et immuable) avec un valeur par défaut

#dictionnaire 2 propriétés
entree = { 'name':'Entree du Donjon','directions':dirs}
salle1 = {'name':'Salle1','directions':dirs}
salle2 = {'name':'Salle2','directions':dirs}
salle3 = {'name':'Salle3','directions':dirs}
couloir = {'name':'Couloir','directions':dirs}
salleBoss = {'name':'Salle du boss','directions':dirs}

#determiné le direction pour chaque salle
entree['directions'] = (salle3,salle1,0,0)
salle1['directions'] = (salle2,0,0,entree)
salle2['directions'] = (0,0,salle1,salle3)
salle3['directions'] = (0,salle2,entree,couloir)
couloir['directions'] = (0,salle3,0,salleBoss)
salleBoss['directions'] = (0,couloir,0,0)


def get_choice(room,dir):

    if dir=='N':
        choice = 0
    elif dir=='E':
        choice = 1
    elif dir=='S':
        choice = 2
    elif dir=='O':
        choice = 3
    else:
        return -1

    if room['directions'][choice] == 0:
        return 4

    else:
        return choice

def combat (genCharacter) :
    print("\n****** BATTAILLE ******")
    print("\nVoici vos stats\n")
    pprint(vars(genCharacter))
    whoDied = Fight.battle(monsters.enemyGen(levelBoss), genCharacter)
    Fight.gameOver(whoDied)

    if genCharacter.health > 0:
        loot.loot(genCharacter.luck, genCharacter)
        print("\nVoici vos nouveaux stats\n")
        pprint(vars(genCharacter))
    else:
        None

def Choice() :
    a = input("Combattre (1) ou Fuire(2)?...\n")

    while a != "1" and a != "2":
        print("Tu te fou de moi?!!! Choisi bien...")
        a = input("Combattre (1) ou Fuire(2)?...\n")

    if a == "1":
        combat(genCharacter)
    elif a == "2":
        None




while True:

    print("""
    
        ########        ##     #######    #####    #######     ##   
        ##     ##       ##    ##     ##  ##   ##  ##     ##  ####   
        ##     ##       ##           ## ##     ##        ##    ##   
        ##     ##       ##     #######  ##     ##  #######     ##   
        ##     ## ##    ##    ##        ##     ## ##           ##   
        ##     ## ##    ##    ##         ##   ##  ##           ##   
        ########   ######     #########   #####   #########  ######
         
        """)

    print("Bienvenue au DJ 2021!")


    room = entree
    playing = True
    roomValid = True

    classData = hero.createChar()
    genCharacter = hero.hero(classData[0], classData[1], classData[2], classData[3], classData[4], classData[5])
    time.sleep(1)
    print("\n\n=================================================")
    print("\nVoici la carte du donjon.")
    print("\nVous etes actuellement à l'entree du donjon")
    print(map.mapEntree)

    while playing:
        print("\n=================================================")
        dir = input("\nOu voulez vous aller : N,E,S ou O?\n")

        choice = get_choice(room, dir)

        if choice == -1:
            dir = print("\nMais qu'est ce que tu raconte. Recommence!\n")

        elif choice == 4:
            dir = print ("\nVous ne pouvez pas aller la bas!\n")
        else:
            room = room['directions'][choice]


        if room == entree and choice not in (-1,4):
            print("*Vous êtes à l'entree*")
            None
        elif room == salle1 and choice not in (-1,4):
            print("*Vous êtes à la salle1*")
            print("Un monstre sauvage est apparu dans la salle")
            levelBoss = False
            Choice()
        elif room == salle2 and choice not in (-1,4):
            print("*Vous êtes à la salle2*")
            print("Un monstre sauvage est apparu dans la salle")
            Choice()
        elif room == salle3 and choice not in (-1,4):
            print("*Vous êtes à la salle3*")
            print("Un monstre sauvage est apparu dans la salle")
            levelBoss = False
            Choice()
        elif room == couloir and choice not in (-1,4):
            print("Vous etes dans un couloir")
            print("Le boss est à l'ouest! Attention!")
            print("Soyez sur d'avoir assez de stats avant d'y aller!")
        elif room == salleBoss:

            print("""\n
            +-+-+-+-+-+-+-+-+
            | B | O | S | S |
            +-+-+-+-++-+-+-+-
            \n""")

            time.sleep(1.5)
            levelBoss = True
            combat(genCharacter)
            break

    if genCharacter.health > 0:
        print("Vous avez gagné!")

    new_game = input("\nVoulez vous rejouer? 'O' ou 'N': ")

    if new_game[0].lower() == 'o':
        playing = True
        continue
    else:
        print("\nA bientôt!")
        break











































































