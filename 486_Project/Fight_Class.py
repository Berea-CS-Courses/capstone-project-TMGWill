from Characters_Class import *
from time import *
import random


class warrior_fight:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Bad_warrior()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        self.combat = True

        self.player_defence = False
        self.enemy_defence = False

        self.warrior_attack = 0
        self.warrior_damage = 0
        self.enemy_attack = 0
        self.enemy_damage = 0

    def warrior_first_vs_bad_warrior(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False
            sleep(0.35)
            attack_mod = random.uniform(1.2, 1.6)

            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = input("Select your action.")

            if action_choice == "attack":
                self.warrior_attack = round(self.fighting_player.stats[0] * attack_mod)
                self.warrior_damage = self.warrior_attack - self.fighting_enemy.bad_warrior_armor

                if self.enemy_defence is True:
                    self.warrior_damage = self.warrior_damage//2

                self.fighting_enemy.bad_warrior_hp = self.fighting_enemy.bad_warrior_hp - self.warrior_damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.warrior_damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.bad_warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break

                print("End Turn")
            elif action_choice == "attack?":
                print("With " + self.fighting_player.weapon[4] + " you deal " + str(round(self.fighting_player.stats[0] * 1.2)) + "-" + str(round(self.fighting_player.stats[0] * 1.6)) + " attack damage.")
                continue

            elif action_choice == "defend":
                self.player_defence = True
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.bad_warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = input()
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("nope")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.warrior_attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.warrior_damage = self.warrior_attack - self.fighting_enemy.bad_warrior_armor

                    if self.enemy_defence is True:
                        self.warrior_damage = self.warrior_damage//2

                    self.fighting_enemy.bad_warrior_hp = self.fighting_enemy.bad_warrior_hp - self.warrior_damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.warrior_damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break

                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("nope")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.warrior_attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.warrior_damage = self.warrior_attack - self.fighting_enemy.bad_warrior_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.warrior_damage = self.warrior_damage//2

                        self.fighting_enemy.bad_warrior_hp = self.fighting_enemy.bad_warrior_hp - self.warrior_damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.warrior_damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "double swing?":
                    print("Deal two attacks in one move." + "\n" + "Cooldown Time: " + str(self.fighting_player.double_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.double_cd))
                    continue

                elif skill_choice == "back":
                    continue

                else:
                    print("Try Again")
                    continue
            elif action_choice == "items":
                if len(self.fighting_player.player_items) == 0:
                    print("No Items")
                    item_choice = input()
                    if item_choice == "back":
                        continue
                else:
                    print(self.fighting_player.player_items)
                    item_choice = input()
                    if item_choice == "shp" and "Small Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.warrior_hp += 10
                        if self.fighting_player.warrior_hp > self.fighting_player.warrior_max_hp:
                            self.fighting_player.warrior_hp = self.fighting_player.warrior_max_hp
                        self.fighting_player.player_items.remove('Small Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "mhp" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.warrior_hp += 20
                        if self.fighting_player.warrior_hp > self.fighting_player.warrior_max_hp:
                            self.fighting_player.warrior_hp = self.fighting_player.warrior_max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "lhp" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.warrior_hp += 30
                        if self.fighting_player.warrior_hp > self.fighting_player.warrior_max_hp:
                            self.fighting_player.warrior_hp = self.fighting_player.warrior_max_hp
                        self.fighting_player.player_items.remove('Large Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "back":
                        continue
                    else:
                        print("Try Again")
                        continue
            else:
                print("Try Again")
                continue
            sleep(0.5)

            while self.combat:
                enemy_action = random.choice(self.fighting_enemy.bad_warrior_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.warrior_armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.warrior_hp = self.fighting_player.warrior_hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " swings their crude weapon and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_big_cd != 0:
                        self.fighting_enemy.enemy_big_cd -= 1
                    if self.fighting_enemy.enemy_double_cd != 0:
                        self.fighting_enemy.enemy_double_cd -= 1

                    if self.fighting_player.warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.bad_warrior_skills)
                    if enemy_skill == "big swing":
                        if self.fighting_enemy.enemy_big_cd != 0:
                            print("enemy big nope")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.enemy_attack = round(self.fighting_enemy.stats[0] * big_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.warrior_armor

                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.warrior_hp = self.fighting_player.warrior_hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " lifts their weapon for a strong blow and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_big_cd = 4
                        if self.fighting_enemy.enemy_double_cd != 0:
                            self.fighting_enemy.enemy_double_cd -= 1

                        if self.fighting_player.warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.bad_warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "double swing":
                        if self.fighting_enemy.enemy_double_cd != 0:
                            print("enemy double nope")
                            continue
                        print("The " + self.fighting_enemy.name + " manages to strike twice.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.enemy_attack = round(self.fighting_enemy.stats[0] * double_attack_mod)
                            self.enemy_damage = self.enemy_attack - self.fighting_player.warrior_armor

                            # checks if enemy is defending
                            if self.player_defence is True:
                                self.enemy_damage = self.enemy_damage//2

                            self.fighting_player.warrior_hp = self.fighting_player.warrior_hp - self.enemy_damage
                            sleep(0.5)
                            print(self.fighting_enemy.name + " deals " + str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_double_cd = 3
                        if self.fighting_enemy.enemy_big_cd != 0:
                            self.fighting_enemy.enemy_big_cd -= 1

                        if self.fighting_player.warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.bad_warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_big_cd != 0:
                        self.fighting_enemy.enemy_big_cd -= 1
                    if self.fighting_enemy.enemy_double_cd != 0:
                        self.fighting_enemy.enemy_double_cd -= 1

                    if self.fighting_player.warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break

    def warrior_second_vs_bad_warrior(self):
        self.combat = True

        while self.combat:
            # print("big cd:" + str(self.fighting_player.big_cd))
            # print("double cd:" + str(self.fighting_player.double_cd))
            self.player_defence = False
            self.enemy_defence = False

            enemy_action = random.choice(self.fighting_enemy.bad_warrior_menu)

            if enemy_action == "attack":
                enemy_attack_mod = random.uniform(1.2, 1.6)
                self.enemy_attack = round(self.fighting_enemy.stats[0] * enemy_attack_mod)
                self.enemy_damage = self.enemy_attack - self.fighting_player.warrior_armor

                if self.player_defence is True:
                    self.enemy_damage = self.enemy_damage//2

                self.fighting_player.warrior_hp = self.fighting_player.warrior_hp - self.enemy_damage
                print("Enemy deals" + " " + str(self.enemy_damage) + " " + "damage")
                self.combat = True

                if self.fighting_player.warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.bad_warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("End Turn")

            elif enemy_action == "skills":
                enemy_skill = random.choice(self.fighting_enemy.bad_warrior_skills)
                if enemy_skill == "big swing":
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * big_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.warrior_armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.warrior_hp = self.fighting_player.warrior_hp - self.enemy_damage
                    print("Enemy deals" + " " + str(self.enemy_damage) + " " + "damage")
                    self.combat = True
                    if self.fighting_player.warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                elif enemy_skill == "double swing":
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.enemy_attack = round(self.fighting_enemy.stats[0] * double_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.warrior_armor

                        # checks if enemy is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.warrior_hp = self.fighting_player.warrior_hp - self.enemy_damage
                        print("Enemy deals" + " " + str(self.enemy_damage) + " " + "damage")
                    self.combat = True
                    if self.fighting_player.warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

            else:
                self.enemy_defence = True
                self.combat = True
                if self.fighting_player.warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.bad_warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("Enemy Defends")
                print("End Turn")

            # player turn
            while self.combat:
                attack_mod = random.uniform(1.2, 1.6)

                print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))

                print(self.fighting_player.player_menu)
                action_choice = input("Select your action.")

                if action_choice == "attack":
                    self.warrior_attack = round(self.fighting_player.stats[0] * attack_mod)
                    self.warrior_damage = self.warrior_attack - self.fighting_enemy.bad_warrior_armor

                    if self.enemy_defence is True:
                        self.warrior_damage = self.warrior_damage//2

                    self.fighting_enemy.bad_warrior_hp = self.fighting_enemy.bad_warrior_hp - self.warrior_damage
                    print("You deal" + " " + str(self.warrior_damage) + " " + "damage")
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    break

                elif action_choice == "attack?":
                    print("You deal" + " " + str(round(self.fighting_player.stats[0] * 1.2)) + "-" + str(round(self.fighting_player.stats[0] * 1.6)) + " " + "attack damage")
                    continue

                elif action_choice == "defend":
                    self.player_defence = True
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.bad_warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break

                    print("End Turn")
                    break

                elif action_choice == "skills":
                    print(self.fighting_player.player_skills)
                    skill_choice = input()
                    if skill_choice == "big swing":
                        if self.fighting_player.big_cd != 0:
                            print("nope")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.warrior_attack = round(self.fighting_player.stats[0] * big_attack_mod)
                        self.warrior_damage = self.warrior_attack - self.fighting_enemy.bad_warrior_armor

                        if self.enemy_defence is True:
                            self.warrior_damage = self.warrior_damage//2

                        self.fighting_enemy.bad_warrior_hp = self.fighting_enemy.bad_warrior_hp - self.warrior_damage
                        print("You deal" + " " + str(self.warrior_damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.big_cd = 4
                        if self.fighting_player.double_cd != 0:
                            self.fighting_player.double_cd -= 1

                        if self.fighting_player.warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.bad_warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break

                        print("End Turn")
                        break

                    elif skill_choice == "big swing?":
                        print("Deal two attacks in one move." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                        continue

                    elif skill_choice == "double swing":
                        if self.fighting_player.double_cd != 0:
                            print("nope")
                            continue
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.warrior_attack = round(self.fighting_player.stats[0] * double_attack_mod)
                            self.warrior_damage = self.warrior_attack - self.fighting_enemy.bad_warrior_armor

                            # checks if enemy is defending
                            if self.enemy_defence is True:
                                self.warrior_damage = self.warrior_damage//2

                            self.fighting_enemy.bad_warrior_hp = self.fighting_enemy.bad_warrior_hp - self.warrior_damage
                            print("You deal" + " " + str(self.warrior_damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.double_cd = 3
                        if self.fighting_player.big_cd != 0:
                            self.fighting_player.big_cd -= 1

                        if self.fighting_player.warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.bad_warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.bad_warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.bad_warrior_hp) + "/" + str(self.fighting_enemy.bad_warrior_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        break

                    elif skill_choice == "double swing?":
                        print("Deal two attacks in one move." + "\n" + "Cooldown Time: " + str(self.fighting_player.double_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.double_cd))
                        continue

                    elif skill_choice == "back":
                        continue

                    else:
                        print("Try Again")
                        continue
                elif action_choice == "items":
                    # show_items()
                    if len(self.fighting_player.player_items) == 0:
                        print("No Items")
                        item_choice = input()
                        if item_choice == "back":
                            continue
                    else:
                        # while self.combat:
                        print(self.fighting_player.player_items)
                        item_choice = input()
                        if item_choice == "shp":
                            # change to functions
                            self.fighting_player.warrior_hp += 10
                            if self.fighting_player.warrior_hp > self.fighting_player.warrior_max_hp:
                                self.fighting_player.warrior_hp = self.fighting_player.warrior_max_hp
                                self.fighting_player.player_items.remove('Small Health Potion')
                                break
                                # continue
                        elif item_choice == "back":
                            # break
                            continue
                        else:
                            print("Try Again")
                            continue
                else:
                    print("Try Again")
                    continue


class Wolf_fight:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Wolf()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        # self.attack_mod = random.uniform(1.2, 1.6)
        # self.attack = round(self.fighting_player.stats[0] * self.attack_mod)
        self.combat = True

        self.player_defence = False
        self.enemy_defence = False

        self.warrior_attack = 0
        self.warrior_damage = 0
        self.enemy_attack = 0
        self.enemy_damage = 0

        # self.big_cdt = 4
        # self.big_cd = 0
        # self.double_cdt = 3
        # self.double_cd = 0

    def warrior_first_vs_wolf(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False
            sleep(0.35)
            attack_mod = random.uniform(1.2, 1.6)

            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = input("Select your action.")

            if action_choice == "attack":
                self.warrior_attack = round(self.fighting_player.stats[0] * attack_mod)
                self.warrior_damage = self.warrior_attack - self.fighting_enemy.wolf_armor

                if self.enemy_defence is True:
                    self.warrior_damage = self.warrior_damage//2

                self.fighting_enemy.wolf_hp = self.fighting_enemy.wolf_hp - self.warrior_damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.warrior_damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.wolf_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.wolf_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break

                print("End Turn")
            elif action_choice == "attack?":
                print("With " + self.fighting_player.weapon[4] + " you deal " + str(round(self.fighting_player.stats[0] * 1.2)) + "-" + str(round(self.fighting_player.stats[0] * 1.6)) + " attack damage.")
                continue

            elif action_choice == "defend":
                self.player_defence = True
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.warrior_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.wolf_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.wolf_hp <= 0:
                    print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = input()
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("nope")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.warrior_attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.warrior_damage = self.warrior_attack - self.fighting_enemy.wolf_armor

                    if self.enemy_defence is True:
                        self.warrior_damage = self.warrior_damage//2

                    self.fighting_enemy.wolf_hp = self.fighting_enemy.wolf_hp - self.warrior_damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.warrior_damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.wolf_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.wolf_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("nope")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.warrior_attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.warrior_damage = self.warrior_attack - self.fighting_enemy.wolf_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.warrior_damage = self.warrior_damage//2

                        self.fighting_enemy.wolf_hp = self.fighting_enemy.wolf_hp - self.warrior_damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.warrior_damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.wolf_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.wolf_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "double swing?":
                    print("Deal two attacks in one move." + "\n" + "Cooldown Time: " + str(self.fighting_player.double_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.double_cd))
                    continue

                elif skill_choice == "back":
                    continue

                else:
                    print("Try Again")
                    continue

            elif action_choice == "items":
                if len(self.fighting_player.player_items) == 0:
                    print("No Items")
                    item_choice = input()
                    if item_choice == "back":
                        continue
                else:
                    # while self.combat:
                    print(self.fighting_player.player_items)
                    item_choice = input()
                    if item_choice == "shp":
                        # change to functions
                        self.fighting_player.warrior_hp += 10
                        if self.fighting_player.warrior_hp > self.fighting_player.warrior_max_hp:
                            self.fighting_player.warrior_hp = self.fighting_player.warrior_max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                    elif item_choice == "mhp" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.warrior_hp += 20
                        if self.fighting_player.warrior_hp > self.fighting_player.warrior_max_hp:
                            self.fighting_player.warrior_hp = self.fighting_player.warrior_max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "lhp" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.warrior_hp += 30
                        if self.fighting_player.warrior_hp > self.fighting_player.warrior_max_hp:
                            self.fighting_player.warrior_hp = self.fighting_player.warrior_max_hp
                        self.fighting_player.player_items.remove('Large Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "back":
                        # break
                        continue
                    else:
                        print("Try Again")
                        continue
            else:
                print("Try Again")
                continue
            sleep(0.5)

            while self.combat:
                enemy_action = random.choice(self.fighting_enemy.wolf_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.warrior_armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.warrior_hp = self.fighting_player.warrior_hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " rabidly attacks and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_maul_cd != 0:
                        self.fighting_enemy.enemy_maul_cd -= 1
                    if self.fighting_enemy.enemy_rend_cd != 0:
                        self.fighting_enemy.enemy_rend_cd -= 1

                    if self.fighting_player.warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.wolf_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.wolf_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.wolf_skills)
                    if enemy_skill == "rend":
                        if self.fighting_enemy.enemy_rend_cd != 0:
                            print("enemy rend nope")
                            continue
                        rend_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * rend_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.warrior_armor

                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.warrior_hp = self.fighting_player.warrior_hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " lunges with their claws and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_rend_cd = 3
                        if self.fighting_enemy.enemy_maul_cd != 0:
                            self.fighting_enemy.enemy_maul_cd -= 1

                        if self.fighting_player.warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.wolf_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.wolf_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "maul":
                        if self.fighting_enemy.enemy_maul_cd != 0:
                            print("enemy maul nope")
                            continue
                        print("The " + self.fighting_enemy.name + " bites you with a savage grip.")
                        for i in range(3):
                            maul_attack_mod = random.uniform(1.2, 1.3)
                            self.enemy_attack = round(self.fighting_enemy.stats[1] * maul_attack_mod)
                            self.enemy_damage = self.enemy_attack - self.fighting_player.warrior_armor

                            # checks if enemy is defending
                            if self.player_defence is True:
                                self.enemy_damage = self.enemy_damage//2

                            self.fighting_player.warrior_hp = self.fighting_player.warrior_hp - self.enemy_damage
                            sleep(0.5)
                            print(self.fighting_enemy.name + " deals " + str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_maul_cd = 3
                        if self.fighting_enemy.enemy_rend_cd != 0:
                            self.fighting_enemy.enemy_rend_cd -= 1

                        if self.fighting_player.warrior_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.wolf_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.wolf_hp <= 0:
                            print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_maul_cd != 0:
                        self.fighting_enemy.enemy_maul_cd -= 1
                    if self.fighting_enemy.enemy_rend_cd != 0:
                        self.fighting_enemy.enemy_rend_cd -= 1

                    if self.fighting_player.warrior_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.warrior_hp <= 0 and self.fighting_enemy.wolf_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.wolf_hp <= 0:
                        print("Player HP:" + " " + str(self.fighting_player.warrior_hp) + "/" + str(self.fighting_player.warrior_max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.wolf_hp) + "/" + str(self.fighting_enemy.wolf_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break
