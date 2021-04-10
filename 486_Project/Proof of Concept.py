import random

# Player and Enemy Stats
# Not all stats are currently being used
Player_HP = 20
Max_Player_HP = Player_HP
p_strength = 7
p_dexterity = 5
p_intelligence = 5
p_constitution = 7
p_armor = 3
p_attack_mod = random.uniform(1.2, 1.6)

Enemy_HP = 20
Max_Enemy_HP = Enemy_HP
e_strength = 10
e_dexterity = 5
e_intelligence = 5
e_constitution = 7
e_armor = 3
e_attack_mod = random.uniform(1.2, 1.6)

# player attack stuff
# p_attack = round(p_strength * p_attack_mod)
# p_damage = p_attack - e_armor
# print("You deal" + " " + str(p_damage) + " " + "damage")

# enemy attack stuff
# e_attack = round(e_strength * e_attack_mod)
# e_damage = e_attack - p_armor
# print("Enemy deals" + " " + str(e_damage) + " " + "damage")

# player defend stuff
# make this a boolean
# p_defend = e_damage / 2

# enemy defend stuff
# e_defend = p_damage / 2

# Player skill list
p_skill_list = '''
[1]Big Swing 
[2]Double Swing
'''

# Enemy skill list
e_skill_list = ["Big Swing", "Double Swing"]

# Player item list
p_item_list = []

# Player menu
p_menu = '''
[1]Attack
[2]Defend
[3]Skills
[4]Items
'''

# Enemy menu
e_menu = ["attack", "defend", "skills"]


combat = True

# Combat loop
while combat:

    # Resets so player and enemy are no longer defending
    e_defence = False
    p_defence = False

    # Player's Turn
    p_attack_mod = random.uniform(1.2, 1.6)

    # HP display
    print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
    print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))

    print(p_menu)
    choice = input("pick one")

    if choice == "attack":
        p_attack = round(p_strength * p_attack_mod)
        p_damage = p_attack - e_armor

        # checks if enemy is defending
        if e_defence is True:
            p_damage = p_damage//2

        Enemy_HP = Enemy_HP - p_damage
        print("You deal" + " " + str(p_damage) + " " + "damage")

        combat = True
        if Player_HP <= 0:
            print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
            print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
            print("You Lose")
            quit()
        elif Player_HP <= 0 and Enemy_HP <= 0:
            print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
            print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
            print("You Lose")
            quit()
        elif Enemy_HP <= 0:
            print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
            print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
            print("You Win")
            combat = False
            break
        print("end turn")
    elif choice == "attack?":
        print("You deal" + " " + str(round(p_strength * 1.2)) + "-" + str(round(p_strength * 1.6)) + " " + "attack damage")
        continue

    elif choice == "defend":
        p_defence = True
        combat = True
        if Player_HP <= 0:
            # HP management
            print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
            print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
            print("You Lose")
            quit()
        elif Player_HP <= 0 and Enemy_HP <= 0:
            # HP management
            print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
            print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
            print("You Lose")
            quit()
        elif Enemy_HP <= 0:
            # HP management
            print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
            print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
            print("You Win")
            combat = False
        print("end turn")

    elif choice == "skills":
        # while combat:
            print(p_skill_list)
            choice2 = input()
            if choice2 == "big swing":
                p_attack_mod = random.uniform(2.1, 2.5)
                p_attack = round(p_strength * p_attack_mod)
                p_damage = p_attack - e_armor

                # checks if enemy is defending
                if e_defence is True:
                    p_damage = p_damage//2

                Enemy_HP = Enemy_HP - p_damage
                print("You deal" + " " + str(p_damage) + " " + "damage")
                combat = True
                if Player_HP <= 0:
                    # HP management
                    print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
                    print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
                    print("You Lose")
                    quit()
                elif Player_HP <= 0 and Enemy_HP <= 0:
                    # HP management
                    print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
                    print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
                    print("You Lose")
                    quit()
                elif Enemy_HP <= 0:
                    # HP management
                    print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
                    print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
                    print("You Win")
                    combat = False
                    break
                print("end turn")
            elif choice2 == "double swing":
                for i in range(2):
                    p_attack_mod = random.uniform(1.2, 1.6)
                    p_attack = round(p_strength * p_attack_mod)
                    p_damage = p_attack - e_armor

                    # checks if enemy is defending
                    if e_defence is True:
                        p_damage = p_damage//2

                    Enemy_HP = Enemy_HP - p_damage
                    print("You deal" + " " + str(p_damage) + " " + "damage")
                combat = True
                if Player_HP <= 0:
                    # HP management
                    print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
                    print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
                    print("You Lose")
                    quit()
                elif Player_HP <= 0 and Enemy_HP <= 0:
                    # HP management
                    print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
                    print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
                    print("You Lose")
                    quit()
                elif Enemy_HP <= 0:
                    # HP management
                    print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
                    print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
                    print("You Win")
                    combat = False
                    break
                print("end turn")
            elif choice2 == "back":
                continue
            else:
                print("try again")
                continue

    elif choice == "items":
        # while combat:
        if len(p_item_list) == 0:
            print("no items")
            choice2 = input()
            if choice2 == "back":
                continue
            else:
                print("try again")
                continue
        else:
            while combat:
                print(p_item_list)
                choice2 = input()
                if choice2 == "back":
                    break
                else:
                    print("try again")
                    continue
    else:
        print("try again")
        continue

    # Enemy's Turn

    # Determines enemy's action for their turn
    e_choice = random.choice(e_menu)

    if e_choice == "attack":
        e_attack_mod = random.uniform(1.2, 1.6)
        e_attack = round(e_strength * e_attack_mod)
        e_damage = e_attack - p_armor

        # checks if player is defending
        if p_defence is True:
            e_damage = e_damage//2

        Player_HP = Player_HP - e_damage
        print("Enemy deals" + " " + str(e_damage) + " " + "damage")
        combat = True
        if Player_HP <= 0:
            print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
            print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
            print("You Lose")
            quit()
        elif Player_HP <= 0 and Enemy_HP <= 0:
            print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
            print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
            print("You Lose")
            quit()
        elif Enemy_HP <= 0:
            print("Player HP:" + " " + str(Player_HP) + "/" + str(Max_Player_HP))
            print("Enemy HP:" + " " + str(Enemy_HP) + "/" + str(Max_Enemy_HP))
            print("You Win")
            combat = False
            break
        print("end turn")
    elif e_choice == "skills":
        e_choice2 = random.choice(e_skill_list)
        if e_choice2 == "Big Swing":
            e_attack_mod = random.uniform(2.1, 2.5)
            e_attack = round(e_strength * e_attack_mod)
            e_damage = e_attack - p_armor

            # checks if player is defending
            if p_defence is True:
                e_damage = e_damage//2

            Player_HP = Player_HP - e_damage
            print("Enemy deals" + " " + str(e_damage) + " " + "damage")
            combat = True
            if Player_HP <= 0:
                print("You Lose")
                quit()
            elif Player_HP <= 0 and Enemy_HP <= 0:
                print("You Lose")
                quit()
            elif Enemy_HP <= 0:
                print("You Win")
                combat = False
                break
            print("end turn")
        elif e_choice2 == "Double Swing":
            for i in range(2):
                e_attack_mod = random.uniform(1.2, 1.6)
                e_attack = round(e_strength * e_attack_mod)
                e_damage = e_attack - p_armor

                # checks if player is defending
                if p_defence is True:
                    e_damage = e_damage//2

                Player_HP = Player_HP - e_damage
                print("Enemy deals" + " " + str(e_damage) + " " + "damage")
            combat = True
            if Player_HP <= 0:
                print("You Lose")
                quit()
            elif Player_HP <= 0 and Enemy_HP <= 0:
                print("You Lose")
                quit()
            elif Enemy_HP <= 0:
                print("You Win")
                combat = False
                break
            print("end turn")
    else:
        e_defence = True
        combat = True
        if Player_HP <= 0:
            print("You Lose")
            quit()
        elif Player_HP <= 0 and Enemy_HP <= 0:
            print("You Lose")
            quit()
        elif Enemy_HP <= 0:
            print("You Win")
            combat = False
            break
        print("enemy defend")
        print("end turn")
