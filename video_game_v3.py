import random
self_hp=100
fight_counter=3
rand=(random.random())*100
attack_dmg=0
enemy_hp=100
crit_check=0
self_hp=100
stage=0
inventory=[]

def attack_dmg_rand(attack_dmg,crit_check):
    crit_check=0
    attack_dmg=int(rand)
    crit_check=rand
    if crit_check<=100:
        attack_dmg*=2
        crit_check=1
    return attack_dmg,crit_check

def get_enemy_hp(attack_dmg,enemy_hp):
    enemy_hp=int(enemy_hp-attack_dmg)

    return enemy_hp

def fight_sequence(self_hp):
    print("|   HP: {:.0f}  |     Enemy HP: {:.0f}    |".format(self_hp,enemy_hp))
    print("+-----------------------------------+")
    print("|    FIGHT   |    HEAL    |   RUN   |")
    print("+-----------------------------------+")
    print("")
    option=input("CHOOSE ACTION: ")

    print("-"*40)
    print(f"{player_name} chose to {option}")
    if crit_check==1 and option.lower()=="fight":
        print(f"A critical hit from {player_name}!")
    
    return self_hp,option

def fight_repeat(attack_dmg,enemy_hp):
    attack_dmg=attack_dmg_rand()
    enemy_hp-=attack_dmg
    return enemy_hp
    
    
#game start
player_name=input("Once upon a time, in the land of Far Far Away, there was an ogre named...? ")
path=input(f"This ogre, {player_name}, embarked on an epic journey for conquest. The path he took was that of...? Enter path1 or path2. ")
while True:
    if path.lower()=="path1" or path.lower()=="path2":
        print (f"{player_name} began his journey on {path}.")
        print ("All seemed well for the ogre, until danger struck.")
        break
    else:
        path=input(f"It seemed the ogre was lost. To which path did he take?")
        continue

#fights
#i cant figure out how to make the hp reset im dying
for i in range(3):
    stage+=1
    print(f"An enemy encounter! Battle {stage} of 3.")
    while True:
        enemy_hp=get_enemy_hp(attack_dmg,enemy_hp)
        attack_dmg,crit_check=attack_dmg_rand(attack_dmg,crit_check)
        self_hp,option=fight_sequence(self_hp)

        if option.lower()=="fight":
            enemy_hp=get_enemy_hp(attack_dmg,enemy_hp)

        if option.lower()=="heal" and self_hp<=91:
            self_hp+=10
            print(f"{player_name} eats an onion. Refreshing!")

        if option.lower()=="run":
            print("Bravery was not the ogre's strong suit.")
            if stage==2 and path.lower()=="path1":
                inventory.append("Letter")
                print("Despite running away, he spotted a letter on the ground. It read 'the princess is in this tower'.")
                print("Letter added to Inventory")
            break

        if enemy_hp<=0:
            print("The ogre basked in his victory.")
            if stage==1 and path.lower()=="path2":
                inventory.append("Key")
                print("He saw something sparkle in the distance. It was a key.")
                print("Key added to Inventory")
            if stage==3:
                print(f"{player_name} surpassed the tower's keep's minions. But was he to defeat the dragon guarding the castle's secrets?")
                print("Suddenly, a noble steed appeared out of thin air. He called himself 'Donkey'")
                donkey_trump_card=input(f"He wants to come with {player_name}. Is it a yes or a no?")
                if donkey_trump_card.lower()=="yes":
                    print(f"{player_name} decided to bring Donkey along the journey.")
                    inventory.append("Donkey")
                    print("Donkey added to Inventory")
                if donkey_trump_card.lower()=="no":
                    print(f"{player_name} decided to leave him be. He wondered if he could have helped.")

            break

#dragon/boss fight
while self_hp>0:
    if "Donkey" in inventory:
        print(f"To {player_name}'s surprise, Donkey and the dragon hit it off very well. A good distraction lead to the great defeat of the dragon.")
    else:
        #start boss fight
        print("")

    break

if self_hp<=0:
    print(f"{player_name} died taking {path}. Poor ogre.")
else:
    if "Key" in inventory:
        print (f"After defeating the dragon, {player_name} scoured the tower for any signs of treasure. As he climbed the stairs to the highest point of the tower," \
        f"he spotted a door nestled deep in the dark hallway. With the key in hand, {player_name} unlocked the door expecting a chest full of jewels. Yet, what lie" \
        " in his wake was a woman who called herself Fiona.")
        print("Ending 1 of 3: Happily Ever After?")
    elif "Letter" in inventory:
        print (f"After defeating the dragon, {player_name} scoured the tower for any signs of life. Alas, he was too late. " \
        "Unbeknownst to him, the princess had already escaped by herself, leaving none but her handkerchief signed 'Fiona of Far Far Away'")
        print("Ending 2 of 3: Rumpelstiltskin AU")
    else:
        print(f"The battle was won, but he felt as if something was missing. {player_name} returned to the kingdom emptyhanded.")
        print("Ending 3 of 3: No Star")