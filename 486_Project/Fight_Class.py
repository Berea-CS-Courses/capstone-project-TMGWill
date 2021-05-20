from Characters_Class import *
from time import *
import random


class Warrior_vs_wolf_fight:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Wolf()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        # self.attack_mod = random.uniform(1.2, 1.6)
        # self.attack = round(self.fighting_player.stats[0] * self.attack_mod)
        self.combat = True
        self.fight = None

        self.player_defence = False
        self.enemy_defence = False

        self.attack = 0
        self.damage = 0
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

            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = str.lower(input("Select your action."))

            if action_choice == "attack":
                self.attack = round(self.fighting_player.stats[0] * attack_mod)
                self.damage = self.attack - self.fighting_enemy.enemy_armor

                if self.enemy_defence is True:
                    self.damage = self.damage//2

                self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = str.lower(input())
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                    item_choice = str.lower(input())
                    if item_choice == "back":
                        continue
                else:
                    # while self.combat:
                    print(self.fighting_player.player_items)
                    item_choice = str.lower(input())
                    if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                    elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 20
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 30
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
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
                enemy_action = random.choice(self.fighting_enemy.enemy_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " rabidly attacks and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_maul_cd != 0:
                        self.fighting_enemy.enemy_maul_cd -= 1
                    if self.fighting_enemy.enemy_rend_cd != 0:
                        self.fighting_enemy.enemy_rend_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                    if enemy_skill == "rend":
                        if self.fighting_enemy.enemy_rend_cd != 0:
                            continue
                        rend_attack_mod = random.uniform(1.4, 1.6)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * rend_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " lunges with their claws and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_rend_cd = 3
                        if self.fighting_enemy.enemy_maul_cd != 0:
                            self.fighting_enemy.enemy_maul_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "maul":
                        if self.fighting_enemy.enemy_maul_cd != 0:
                            continue
                        print("The " + self.fighting_enemy.name + " bites you with a savage grip.")
                        for i in range(3):
                            maul_attack_mod = random.uniform(1.2, 1.4)
                            self.enemy_attack = round(self.fighting_enemy.stats[1] * maul_attack_mod)
                            self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                            # checks if enemy is defending
                            if self.player_defence is True:
                                self.enemy_damage = self.enemy_damage//2

                            self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                            sleep(0.5)
                            print(self.fighting_enemy.name + " deals " + str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_maul_cd = 3
                        if self.fighting_enemy.enemy_rend_cd != 0:
                            self.fighting_enemy.enemy_rend_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break

    def warrior_second_vs_wolf(self):
        self.combat = True
        while self.combat:
            self.player_defence = False
            self.enemy_defence = False

            enemy_action = random.choice(self.fighting_enemy.enemy_menu)

            if enemy_action == "attack":
                enemy_attack_mod = random.uniform(1.2, 1.6)
                self.enemy_attack = round(self.fighting_enemy.stats[1] * enemy_attack_mod)
                self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                if self.player_defence is True:
                    self.enemy_damage = self.enemy_damage//2

                self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                print("The enemy, " + self.fighting_enemy.name + " rabidly attacks and deals ", end="")
                sleep(0.5)
                print(str(self.enemy_damage) + " damage")
                self.combat = True

                if self.fighting_enemy.enemy_maul_cd != 0:
                    self.fighting_enemy.enemy_maul_cd -= 1
                if self.fighting_enemy.enemy_rend_cd != 0:
                    self.fighting_enemy.enemy_rend_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("End Turn")
                sleep(0.5)

            elif enemy_action == "skills":
                enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                if enemy_skill == "rend":
                    if self.fighting_enemy.enemy_rend_cd != 0:
                        continue
                    rend_attack_mod = random.uniform(1.4, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * rend_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " lunges with their claws and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_rend_cd = 3
                    if self.fighting_enemy.enemy_maul_cd != 0:
                        self.fighting_enemy.enemy_maul_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                elif enemy_skill == "maul":
                    if self.fighting_enemy.enemy_maul_cd != 0:
                        continue
                    print("The " + self.fighting_enemy.name + " bites you with a savage grip.")
                    for i in range(3):
                        maul_attack_mod = random.uniform(1.2, 1.4)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * maul_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if enemy is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        sleep(0.5)
                        print(self.fighting_enemy.name + " deals " + str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_maul_cd = 3
                    if self.fighting_enemy.enemy_rend_cd != 0:
                        self.fighting_enemy.enemy_rend_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
            else:
                self.enemy_defence = True
                self.combat = True

                if self.fighting_enemy.enemy_maul_cd != 0:
                    self.fighting_enemy.enemy_maul_cd -= 1
                if self.fighting_enemy.enemy_rend_cd != 0:
                    self.fighting_enemy.enemy_rend_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("The " + self.fighting_enemy.name + " readies for your next attack.")
                print("End Turn")
                sleep(0.5)

            # player turn
            while self.combat:
                sleep(0.35)
                attack_mod = random.uniform(1.2, 1.6)

                print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

                print(self.fighting_player.player_menu)
                action_choice = str.lower(input("Select your action."))

                if action_choice == "attack":
                    self.attack = round(self.fighting_player.stats[0] * attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " damage")
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("You ready yourself for the enemy's next attack.")
                    sleep(0.5)
                    print("End Turn")

                elif action_choice == "skills":
                    print(self.fighting_player.player_skills)
                    skill_choice = str.lower(input())
                    if skill_choice == "big swing":
                        if self.fighting_player.big_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                        sleep(0.5)
                        print(str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.big_cd = 4
                        if self.fighting_player.double_cd != 0:
                            self.fighting_player.double_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break

                        print("End Turn")

                    elif skill_choice == "big swing?":
                        print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                        continue

                    elif skill_choice == "double swing":
                        if self.fighting_player.double_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                            self.damage = self.attack - self.fighting_enemy.enemy_armor

                            # checks if enemy is defending
                            if self.enemy_defence is True:
                                self.damage = self.damage//2

                            self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                            sleep(0.5)
                            print("You deal" + " " + str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.double_cd = 3
                        if self.fighting_player.big_cd != 0:
                            self.fighting_player.big_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                        item_choice = str.lower(input())
                        if item_choice == "back":
                            continue
                    else:
                        print(self.fighting_player.player_items)
                        item_choice = str.lower(input())
                        if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 20
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Medium Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 30
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
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
                break

    def decide_warrior_vs_wolf_fight(self):
        fight_list = [self.warrior_first_vs_wolf, self.warrior_second_vs_wolf]
        if self.fighting_player.stats[1] > self.fighting_enemy.stats[1]:
            self.fight = fight_list[0]
        elif self.fighting_player.stats[1] < self.fighting_enemy.stats[1]:
            self.fight = fight_list[1]
        elif self.fighting_player.stats[1] == self.fighting_enemy.stats[1]:
            self.fight = random.choice(fight_list)

        return self.fight()


class Warrior_vs_giant_lizard_fight:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Giant_lizard()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        # self.attack_mod = random.uniform(1.2, 1.6)
        # self.attack = round(self.fighting_player.stats[0] * self.attack_mod)
        self.combat = True

        self.player_defence = False
        self.enemy_defence = False

        self.attack = 0
        self.damage = 0
        self.enemy_attack = 0
        self.enemy_damage = 0

        # self.big_cdt = 4
        # self.big_cd = 0
        # self.double_cdt = 3
        # self.double_cd = 0

    def warrior_first_vs_giant_lizard(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False
            sleep(0.35)
            attack_mod = random.uniform(1.2, 1.6)

            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = str.lower(input("Select your action."))

            if action_choice == "attack":
                self.attack = round(self.fighting_player.stats[0] * attack_mod)
                self.damage = self.attack - self.fighting_enemy.enemy_armor

                if self.enemy_defence is True:
                    self.damage = self.damage//2

                self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = str.lower(input())
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                    item_choice = str.lower(input())
                    if item_choice == "back":
                        continue
                else:
                    # while self.combat:
                    print(self.fighting_player.player_items)
                    item_choice = str.lower(input())
                    if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                    elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 20
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 30
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
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
                enemy_action = random.choice(self.fighting_enemy.enemy_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " rabidly attacks and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_tail_cd != 0:
                        self.fighting_enemy.enemy_tail_cd -= 1
                    if self.fighting_enemy.enemy_ram_cd != 0:
                        self.fighting_enemy.enemy_ram_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                    if enemy_skill == "tail whip":
                        if self.fighting_enemy.enemy_tail_cd != 0:
                            continue
                        tail_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * tail_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " whips you with their might tail and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_tail_cd = 3
                        if self.fighting_enemy.enemy_ram_cd != 0:
                            self.fighting_enemy.enemy_ram_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "ram":
                        if self.fighting_enemy.enemy_ram_cd != 0:
                            continue
                        print("The " + self.fighting_enemy.name + " bites you with a savage grip.")
                        ram_attack_mod = random.uniform(1.2, 1.3)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * ram_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if enemy is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " throws their weight at you and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_ram_cd = 3
                        if self.fighting_enemy.enemy_tail_cd != 0:
                            self.fighting_enemy.enemy_tail_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_tail_cd != 0:
                        self.fighting_enemy.enemy_tail_cd -= 1
                    if self.fighting_enemy.enemy_ram_cd != 0:
                        self.fighting_enemy.enemy_ram_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break

    def warrior_second_vs_giant_lizard(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False

            enemy_action = random.choice(self.fighting_enemy.enemy_menu)

            if enemy_action == "attack":
                enemy_attack_mod = random.uniform(1.2, 1.6)
                self.enemy_attack = round(self.fighting_enemy.stats[1] * enemy_attack_mod)
                self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                if self.player_defence is True:
                    self.enemy_damage = self.enemy_damage//2

                self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                print("The enemy, " + self.fighting_enemy.name + " rabidly attacks and deals ", end="")
                sleep(0.5)
                print(str(self.enemy_damage) + " damage")
                self.combat = True

                if self.fighting_enemy.enemy_tail_cd != 0:
                    self.fighting_enemy.enemy_tail_cd -= 1
                if self.fighting_enemy.enemy_ram_cd != 0:
                    self.fighting_enemy.enemy_ram_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("End Turn")
                sleep(0.5)

            elif enemy_action == "skills":
                enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                if enemy_skill == "tail whip":
                    if self.fighting_enemy.enemy_tail_cd != 0:
                        continue
                    tail_attack_mod = random.uniform(1.6, 1.8)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * tail_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " whips you with their mighty tail and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_tail_cd = 3
                    if self.fighting_enemy.enemy_ram_cd != 0:
                        self.fighting_enemy.enemy_ram_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

                elif enemy_skill == "ram":
                    if self.fighting_enemy.enemy_ram_cd != 0:
                        continue
                    ram_attack_mod = random.uniform(1.2, 1.3)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * ram_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    # checks if enemy is defending
                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " throws their weight at you and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_ram_cd = 3
                    if self.fighting_enemy.enemy_tail_cd != 0:
                        self.fighting_enemy.enemy_tail_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

            else:
                self.enemy_defence = True
                self.combat = True

                if self.fighting_enemy.enemy_tail_cd != 0:
                    self.fighting_enemy.enemy_tail_cd -= 1
                if self.fighting_enemy.enemy_ram_cd != 0:
                    self.fighting_enemy.enemy_ram_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("The " + self.fighting_enemy.name + " readies for your next attack.")
                print("End Turn")
                sleep(0.5)


            # player turn
            while self.combat:
                sleep(0.35)
                attack_mod = random.uniform(1.2, 1.6)

                print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

                print(self.fighting_player.player_menu)
                action_choice = str.lower(input("Select your action."))

                if action_choice == "attack":
                    self.attack = round(self.fighting_player.stats[0] * attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " damage")
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("You ready yourself for the enemy's next attack.")
                    sleep(0.5)
                    print("End Turn")

                elif action_choice == "skills":
                    print(self.fighting_player.player_skills)
                    skill_choice = str.lower(input())
                    if skill_choice == "big swing":
                        if self.fighting_player.big_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                        sleep(0.5)
                        print(str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.big_cd = 4
                        if self.fighting_player.double_cd != 0:
                            self.fighting_player.double_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break

                        print("End Turn")

                    elif skill_choice == "big swing?":
                        print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                        continue

                    elif skill_choice == "double swing":
                        if self.fighting_player.double_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                            self.damage = self.attack - self.fighting_enemy.enemy_armor

                            # checks if enemy is defending
                            if self.enemy_defence is True:
                                self.damage = self.damage//2

                            self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                            sleep(0.5)
                            print("You deal" + " " + str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.double_cd = 3
                        if self.fighting_player.big_cd != 0:
                            self.fighting_player.big_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                        item_choice = str.lower(input())
                        if item_choice == "back":
                            continue
                    else:
                        print(self.fighting_player.player_items)
                        item_choice = str.lower(input())
                        if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 20
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Medium Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 30
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
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
                break

    def decide_warrior_vs_giant_lizard(self):
        fight_list = [self.warrior_first_vs_giant_lizard, self.warrior_second_vs_giant_lizard]
        if self.fighting_player.stats[1] > self.fighting_enemy.stats[1]:
            self.fight = fight_list[0]
        elif self.fighting_player.stats[1] < self.fighting_enemy.stats[1]:
            self.fight = fight_list[1]
        elif self.fighting_player.stats[1] == self.fighting_enemy.stats[1]:
            self.fight = random.choice(fight_list)

        return self.fight()


class Warrior_vs_giant_eagle_fight:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Giant_eagle()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        # self.attack_mod = random.uniform(1.2, 1.6)
        # self.attack = round(self.fighting_player.stats[0] * self.attack_mod)
        self.combat = True

        self.player_defence = False
        self.enemy_defence = False

        self.attack = 0
        self.damage = 0
        self.enemy_attack = 0
        self.enemy_damage = 0

        # self.big_cdt = 4
        # self.big_cd = 0
        # self.double_cdt = 3
        # self.double_cd = 0

    def warrior_first_vs_giant_eagle(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False
            sleep(0.35)
            attack_mod = random.uniform(1.2, 1.6)

            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = str.lower(input("Select your action."))

            if action_choice == "attack":
                self.attack = round(self.fighting_player.stats[0] * attack_mod)
                self.damage = self.attack - self.fighting_enemy.enemy_armor

                if self.enemy_defence is True:
                    self.damage = self.damage//2

                self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = str.lower(input())
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                    item_choice = str.lower(input())
                    if item_choice == "back":
                        continue
                else:
                    # while self.combat:
                    print(self.fighting_player.player_items)
                    item_choice = str.lower(input())
                    if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                    elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 20
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 30
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
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
                enemy_action = random.choice(self.fighting_enemy.enemy_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " rabidly attacks and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_dive_cd != 0:
                        self.fighting_enemy.enemy_dive_cd -= 1
                    if self.fighting_enemy.enemy_talons_cd != 0:
                        self.fighting_enemy.enemy_talons_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                    if enemy_skill == "dive bomb":
                        if self.fighting_enemy.enemy_dive_cd != 0:
                            continue
                        dive_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * dive_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " flies high and races toward you with it's beak like a spear and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_dive_cd = 3
                        if self.fighting_enemy.enemy_talons_cd != 0:
                            self.fighting_enemy.enemy_talons_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "talons":
                        if self.fighting_enemy.enemy_talons_cd != 0:
                            continue
                        print("The " + self.fighting_enemy.name + " rakes you with it's talons.")
                        for i in range(2):
                            talons_attack_mod = random.uniform(1.2, 1.3)
                            self.enemy_attack = round(self.fighting_enemy.stats[1] * talons_attack_mod)
                            self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                            # checks if enemy is defending
                            if self.player_defence is True:
                                self.enemy_damage = self.enemy_damage//2

                            self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                            sleep(0.5)
                            print(self.fighting_enemy.name + " deals " + str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_talons_cd = 3
                        if self.fighting_enemy.enemy_dive_cd != 0:
                            self.fighting_enemy.enemy_dive_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_dive_cd != 0:
                        self.fighting_enemy.enemy_dive_cd -= 1
                    if self.fighting_enemy.enemy_talons_cd != 0:
                        self.fighting_enemy.enemy_talons_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break

    def warrior_second_vs_giant_eagle(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False

            enemy_action = random.choice(self.fighting_enemy.enemy_menu)

            if enemy_action == "attack":
                enemy_attack_mod = random.uniform(1.2, 1.6)
                self.enemy_attack = round(self.fighting_enemy.stats[1] * enemy_attack_mod)
                self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                if self.player_defence is True:
                    self.enemy_damage = self.enemy_damage//2

                self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                print("The enemy, " + self.fighting_enemy.name + " rabidly attacks and deals ", end="")
                sleep(0.5)
                print(str(self.enemy_damage) + " damage")
                self.combat = True

                if self.fighting_enemy.enemy_dive_cd != 0:
                    self.fighting_enemy.enemy_dive_cd -= 1
                if self.fighting_enemy.enemy_talons_cd != 0:
                    self.fighting_enemy.enemy_talons_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("End Turn")
                sleep(0.5)

            elif enemy_action == "skills":
                enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                if enemy_skill == "dive bomb":
                    if self.fighting_enemy.enemy_dive_cd != 0:
                        continue
                    dive_attack_mod = random.uniform(1.6, 1.8)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * dive_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " flies high and races toward you with it's beak like a spear and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_dive_cd = 3
                    if self.fighting_enemy.enemy_talons_cd != 0:
                        self.fighting_enemy.enemy_talons_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                elif enemy_skill == "talons":
                    if self.fighting_enemy.enemy_talons_cd != 0:
                        continue
                    print("The " + self.fighting_enemy.name + " rakes you with it's talons.")
                    for i in range(2):
                        talons_attack_mod = random.uniform(1.2, 1.3)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * talons_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if enemy is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        sleep(0.5)
                        print(self.fighting_enemy.name + " deals " + str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_talons_cd = 3
                    if self.fighting_enemy.enemy_dive_cd != 0:
                        self.fighting_enemy.enemy_dive_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
            else:
                self.enemy_defence = True
                self.combat = True

                if self.fighting_enemy.enemy_dive_cd != 0:
                    self.fighting_enemy.enemy_dive_cd -= 1
                if self.fighting_enemy.enemy_talons_cd != 0:
                    self.fighting_enemy.enemy_talons_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("The " + self.fighting_enemy.name + " readies for your next attack.")
                print("End Turn")
                sleep(0.5)

            # player turn
            while self.combat:
                sleep(0.35)
                attack_mod = random.uniform(1.2, 1.6)

                print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

                print(self.fighting_player.player_menu)
                action_choice = str.lower(input("Select your action."))

                if action_choice == "attack":
                    self.attack = round(self.fighting_player.stats[0] * attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " damage")
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("You ready yourself for the enemy's next attack.")
                    sleep(0.5)
                    print("End Turn")

                elif action_choice == "skills":
                    print(self.fighting_player.player_skills)
                    skill_choice = str.lower(input())
                    if skill_choice == "big swing":
                        if self.fighting_player.big_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                        sleep(0.5)
                        print(str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.big_cd = 4
                        if self.fighting_player.double_cd != 0:
                            self.fighting_player.double_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break

                        print("End Turn")

                    elif skill_choice == "big swing?":
                        print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                        continue

                    elif skill_choice == "double swing":
                        if self.fighting_player.double_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                            self.damage = self.attack - self.fighting_enemy.enemy_armor

                            # checks if enemy is defending
                            if self.enemy_defence is True:
                                self.damage = self.damage//2

                            self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                            sleep(0.5)
                            print("You deal" + " " + str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.double_cd = 3
                        if self.fighting_player.big_cd != 0:
                            self.fighting_player.big_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                        item_choice = str.lower(input())
                        if item_choice == "back":
                            continue
                    else:
                        print(self.fighting_player.player_items)
                        item_choice = str.lower(input())
                        if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 20
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Medium Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 30
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
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
                break

    def decide_warrior_vs_giant_eagle(self):
        fight_list = [self.warrior_first_vs_giant_eagle, self.warrior_second_vs_giant_eagle]
        if self.fighting_player.stats[1] > self.fighting_enemy.stats[1]:
            self.fight = fight_list[0]
        elif self.fighting_player.stats[1] < self.fighting_enemy.stats[1]:
            self.fight = fight_list[1]
        elif self.fighting_player.stats[1] == self.fighting_enemy.stats[1]:
            self.fight = random.choice(fight_list)

        return self.fight()


class Warrior_vs_corrupted_swordsman_fight:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Corrupted_swordsman()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        self.combat = True

        self.player_defence = False
        self.enemy_defence = False

        self.attack = 0
        self.damage = 0
        self.enemy_attack = 0
        self.enemy_damage = 0

    def warrior_first_vs_corrupted_swordsman(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False
            sleep(0.35)
            attack_mod = random.uniform(1.2, 1.6)

            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = str.lower(input("Select your action."))

            if action_choice == "attack":
                self.attack = round(self.fighting_player.stats[0] * attack_mod)
                self.damage = self.attack - self.fighting_enemy.enemy_armor

                if self.enemy_defence is True:
                    self.damage = self.damage//2

                self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = str.lower(input())
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break

                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                    item_choice = str.lower(input())
                    if item_choice == "back":
                        continue
                else:
                    print(self.fighting_player.player_items)
                    item_choice = str.lower(input())
                    if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 10
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
                        self.fighting_player.player_items.remove('Small Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 20
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 30
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
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
                enemy_action = random.choice(self.fighting_enemy.enemy_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " swings their crude weapon and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_big_cd != 0:
                        self.fighting_enemy.enemy_big_cd -= 1
                    if self.fighting_enemy.enemy_double_cd != 0:
                        self.fighting_enemy.enemy_double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                    if enemy_skill == "big swing":
                        if self.fighting_enemy.enemy_big_cd != 0:
                            continue
                        big_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[0] * big_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " lifts their weapon for a strong blow and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_big_cd = 4
                        if self.fighting_enemy.enemy_double_cd != 0:
                            self.fighting_enemy.enemy_double_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "double swing":
                        if self.fighting_enemy.enemy_double_cd != 0:
                            continue
                        print("The " + self.fighting_enemy.name + " manages to strike twice.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.4)
                            self.enemy_attack = round(self.fighting_enemy.stats[0] * double_attack_mod)
                            self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                            # checks if enemy is defending
                            if self.player_defence is True:
                                self.enemy_damage = self.enemy_damage//2

                            self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                            sleep(0.5)
                            print(self.fighting_enemy.name + " deals " + str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_double_cd = 3
                        if self.fighting_enemy.enemy_big_cd != 0:
                            self.fighting_enemy.enemy_big_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break
    def warrior_second_vs_corrupted_swordsman(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False

            enemy_action = random.choice(self.fighting_enemy.enemy_menu)

            if enemy_action == "attack":
                enemy_attack_mod = random.uniform(1.2, 1.6)
                self.enemy_attack = round(self.fighting_enemy.stats[0] * enemy_attack_mod)
                self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                if self.player_defence is True:
                    self.enemy_damage = self.enemy_damage//2

                self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                print("The enemy, " + self.fighting_enemy.name + " swings their crude weapon and deals ", end="")
                sleep(0.5)
                print(str(self.enemy_damage) + " damage")
                self.combat = True

                if self.fighting_enemy.enemy_big_cd != 0:
                    self.fighting_enemy.enemy_big_cd -= 1
                if self.fighting_enemy.enemy_double_cd != 0:
                    self.fighting_enemy.enemy_double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("End Turn")
                sleep(0.5)

            elif enemy_action == "skills":
                enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                if enemy_skill == "big swing":
                    if self.fighting_enemy.enemy_big_cd != 0:
                        continue
                    big_attack_mod = random.uniform(1.6, 1.8)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * big_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " lifts their weapon for a strong blow and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_big_cd = 4
                    if self.fighting_enemy.enemy_double_cd != 0:
                        self.fighting_enemy.enemy_double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                elif enemy_skill == "double swing":
                    if self.fighting_enemy.enemy_double_cd != 0:
                        continue
                    print("The " + self.fighting_enemy.name + " manages to strike twice.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.4)
                        self.enemy_attack = round(self.fighting_enemy.stats[0] * double_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if enemy is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        sleep(0.5)
                        print(self.fighting_enemy.name + " deals " + str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_double_cd = 3
                    if self.fighting_enemy.enemy_big_cd != 0:
                        self.fighting_enemy.enemy_big_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
            else:
                self.enemy_defence = True
                self.combat = True

                if self.fighting_enemy.enemy_big_cd != 0:
                    self.fighting_enemy.enemy_big_cd -= 1
                if self.fighting_enemy.enemy_double_cd != 0:
                    self.fighting_enemy.enemy_double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("The " + self.fighting_enemy.name + " readies for your next attack.")
                print("End Turn")
                sleep(0.5)

            # player turn
            while self.combat:
                sleep(0.35)
                attack_mod = random.uniform(1.2, 1.6)

                print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

                print(self.fighting_player.player_menu)
                action_choice = str.lower(input("Select your action."))

                if action_choice == "attack":
                    self.attack = round(self.fighting_player.stats[0] * attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " damage")
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("You ready yourself for the enemy's next attack.")
                    sleep(0.5)
                    print("End Turn")

                elif action_choice == "skills":
                    print(self.fighting_player.player_skills)
                    skill_choice = str.lower(input())
                    if skill_choice == "big swing":
                        if self.fighting_player.big_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                        sleep(0.5)
                        print(str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.big_cd = 4
                        if self.fighting_player.double_cd != 0:
                            self.fighting_player.double_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break

                        print("End Turn")

                    elif skill_choice == "big swing?":
                        print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                        continue

                    elif skill_choice == "double swing":
                        if self.fighting_player.double_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                            self.damage = self.attack - self.fighting_enemy.enemy_armor

                            # checks if enemy is defending
                            if self.enemy_defence is True:
                                self.damage = self.damage//2

                            self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                            sleep(0.5)
                            print("You deal" + " " + str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.double_cd = 3
                        if self.fighting_player.big_cd != 0:
                            self.fighting_player.big_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                        item_choice = str.lower(input())
                        if item_choice == "back":
                            continue
                    else:
                        print(self.fighting_player.player_items)
                        item_choice = str.lower(input())
                        if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 20
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Medium Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 30
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
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
                break

    def decide_warrior_vs_corrupted_swordsman(self):
        fight_list = [self.warrior_first_vs_corrupted_swordsman, self.warrior_second_vs_corrupted_swordsman]
        if self.fighting_player.stats[1] > self.fighting_enemy.stats[1]:
            self.fight = fight_list[0]
        elif self.fighting_player.stats[1] < self.fighting_enemy.stats[1]:
            self.fight = fight_list[1]
        elif self.fighting_player.stats[1] == self.fighting_enemy.stats[1]:
            self.fight = random.choice(fight_list)

        return self.fight()


class Warrior_vs_corrupted_knight_fight:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Corrupted_knight()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        self.combat = True

        self.player_defence = False
        self.enemy_defence = False

        self.attack = 0
        self.damage = 0
        self.enemy_attack = 0
        self.enemy_damage = 0

        # self.big_cdt = 4
        # self.big_cd = 0
        # self.double_cdt = 3
        # self.double_cd = 0

    def warrior_first_vs_corrupted_knight(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False
            sleep(0.35)
            attack_mod = random.uniform(1.2, 1.6)

            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = str.lower(input("Select your action."))

            if action_choice == "attack":
                self.attack = round(self.fighting_player.stats[0] * attack_mod)
                self.damage = self.attack - self.fighting_enemy.enemy_armor

                if self.enemy_defence is True:
                    self.damage = self.damage//2

                self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = str.lower(input())
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                    item_choice = str.lower(input())
                    if item_choice == "back":
                        continue
                else:
                    # while self.combat:
                    print(self.fighting_player.player_items)
                    item_choice = str.lower(input())
                    if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                    elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 20
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 30
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
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
                enemy_action = random.choice(self.fighting_enemy.enemy_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " slashes with expert technique and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_pommel_cd != 0:
                        self.fighting_enemy.enemy_pommel_cd -= 1
                    if self.fighting_enemy.enemy_lunge_cd != 0:
                        self.fighting_enemy.enemy_lunge_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                    if enemy_skill == "pommel strike":
                        if self.fighting_enemy.enemy_pommel_cd != 0:
                            continue
                        pommel_attack_mod = random.uniform(1.4, 1.6)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * pommel_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " strikes with the butt of their blade and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_pommel_cd = 3
                        if self.fighting_enemy.enemy_lunge_cd != 0:
                            self.fighting_enemy.enemy_lunge_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "lunge":
                        if self.fighting_enemy.enemy_lunge_cd != 0:
                            continue
                        lunge_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[0] * lunge_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if enemy is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " surges forward with blade in hand and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_lunge_cd = 3
                        if self.fighting_enemy.enemy_pommel_cd != 0:
                            self.fighting_enemy.enemy_pommel_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_pommel_cd != 0:
                        self.fighting_enemy.enemy_pommel_cd -= 1
                    if self.fighting_enemy.enemy_lunge_cd != 0:
                        self.fighting_enemy.enemy_lunge_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break

    def warrior_second_vs_corrupted_knight(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False

            enemy_action = random.choice(self.fighting_enemy.enemy_menu)

            if enemy_action == "attack":
                enemy_attack_mod = random.uniform(1.2, 1.6)
                self.enemy_attack = round(self.fighting_enemy.stats[0] * enemy_attack_mod)
                self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                if self.player_defence is True:
                    self.enemy_damage = self.enemy_damage//2

                self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                print("The enemy, " + self.fighting_enemy.name + " slashes with expert technique and deals ", end="")
                sleep(0.5)
                print(str(self.enemy_damage) + " damage")
                self.combat = True

                if self.fighting_enemy.enemy_pommel_cd != 0:
                    self.fighting_enemy.enemy_pommel_cd -= 1
                if self.fighting_enemy.enemy_lunge_cd != 0:
                    self.fighting_enemy.enemy_lunge_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("End Turn")
                sleep(0.5)


            elif enemy_action == "skills":
                enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                if enemy_skill == "pommel strike":
                    if self.fighting_enemy.enemy_pommel_cd != 0:
                        continue
                    pommel_attack_mod = random.uniform(1.4, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * pommel_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " strikes with the butt of their blade and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_pommel_cd = 3
                    if self.fighting_enemy.enemy_lunge_cd != 0:
                        self.fighting_enemy.enemy_lunge_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

                elif enemy_skill == "lunge":
                    if self.fighting_enemy.enemy_lunge_cd != 0:
                        continue
                    lunge_attack_mod = random.uniform(1.6, 1.8)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * lunge_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    # checks if enemy is defending
                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " surges forward with blade in hand and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_lunge_cd = 3
                    if self.fighting_enemy.enemy_pommel_cd != 0:
                        self.fighting_enemy.enemy_pommel_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

            else:
                self.enemy_defence = True
                self.combat = True

                if self.fighting_enemy.enemy_pommel_cd != 0:
                    self.fighting_enemy.enemy_pommel_cd -= 1
                if self.fighting_enemy.enemy_lunge_cd != 0:
                    self.fighting_enemy.enemy_lunge_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("The " + self.fighting_enemy.name + " readies for your next attack.")
                print("End Turn")
                sleep(0.5)


            # player turn
            while self.combat:
                sleep(0.35)
                attack_mod = random.uniform(1.2, 1.6)

                print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

                print(self.fighting_player.player_menu)
                action_choice = str.lower(input("Select your action."))

                if action_choice == "attack":
                    self.attack = round(self.fighting_player.stats[0] * attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " damage")
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break

                    print("End Turn")
                    break
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("You ready yourself for the enemy's next attack.")
                    sleep(0.5)
                    print("End Turn")
                    break
                elif action_choice == "skills":
                    print(self.fighting_player.player_skills)
                    skill_choice = str.lower(input())
                    if skill_choice == "big swing":
                        if self.fighting_player.big_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                        sleep(0.5)
                        print(str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.big_cd = 4
                        if self.fighting_player.double_cd != 0:
                            self.fighting_player.double_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break

                        print("End Turn")
                        break
                    elif skill_choice == "big swing?":
                        print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                        continue

                    elif skill_choice == "double swing":
                        if self.fighting_player.double_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                            self.damage = self.attack - self.fighting_enemy.enemy_armor

                            # checks if enemy is defending
                            if self.enemy_defence is True:
                                self.damage = self.damage//2

                            self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                            sleep(0.5)
                            print("You deal" + " " + str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.double_cd = 3
                        if self.fighting_player.big_cd != 0:
                            self.fighting_player.big_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                    if len(self.fighting_player.player_items) == 0:
                        print("No Items")
                        item_choice = str.lower(input())
                        if item_choice == "back":
                            continue
                    else:
                        print(self.fighting_player.player_items)
                        item_choice = str.lower(input())
                        if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                            break
                        elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 20
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Medium Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                            break
                        elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 30
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Large Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                            break
                        elif item_choice == "back":
                            continue
                        else:
                            print("Try Again")
                            continue
                else:
                    print("Try Again")
                    continue
                sleep(0.5)

    def decide_warrior_vs_corrupted_knight(self):
        fight_list = [self.warrior_first_vs_corrupted_knight, self.warrior_second_vs_corrupted_knight]
        if self.fighting_player.stats[1] > self.fighting_enemy.stats[1]:
            self.fight = fight_list[0]
        elif self.fighting_player.stats[1] < self.fighting_enemy.stats[1]:
            self.fight = fight_list[1]
        elif self.fighting_player.stats[1] == self.fighting_enemy.stats[1]:
            self.fight = random.choice(fight_list)

        return self.fight()


class Warrior_vs_corrupted_acolyte_fight:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Corrupted_acolyte()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        self.combat = True

        self.player_defence = False
        self.enemy_defence = False

        self.attack = 0
        self.damage = 0
        self.enemy_attack = 0
        self.enemy_damage = 0

    def warrior_first_vs_corrupted_acolyte(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False
            sleep(0.35)
            attack_mod = random.uniform(1.2, 1.6)

            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = str.lower(input("Select your action."))

            if action_choice == "attack":
                self.attack = round(self.fighting_player.stats[0] * attack_mod)
                self.damage = self.attack - self.fighting_enemy.enemy_armor

                if self.enemy_defence is True:
                    self.damage = self.damage//2

                self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = str.lower(input())
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                    item_choice = str.lower(input())
                    if item_choice == "back":
                        continue
                else:
                    # while self.combat:
                    print(self.fighting_player.player_items)
                    item_choice = str.lower(input())
                    if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                    elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 20
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 30
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
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
                enemy_action = random.choice(self.fighting_enemy.enemy_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[2] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " fires a blast of simple arcane energy and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_chaosb_cd != 0:
                        self.fighting_enemy.enemy_chaosb_cd -= 1
                    if self.fighting_enemy.enemy_fireb_cd != 0:
                        self.fighting_enemy.enemy_fireb_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                    if enemy_skill == "chaos bolt":
                        if self.fighting_enemy.enemy_chaosb_cd != 0:
                            continue
                        chaosb_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[2] * chaosb_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " launches corrupted arcane energy and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_chaosb_cd = 3
                        if self.fighting_enemy.enemy_fireb_cd != 0:
                            self.fighting_enemy.enemy_fireb_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "fire bolt":
                        if self.fighting_enemy.enemy_fireb_cd != 0:
                            continue
                        fireb_attack_mod = random.uniform(1.4, 1.6)
                        self.enemy_attack = round(self.fighting_enemy.stats[2] * fireb_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if enemy is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " blasts you with a bolt of fire and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_fireb_cd = 3
                        if self.fighting_enemy.enemy_chaosb_cd != 0:
                            self.fighting_enemy.enemy_chaosb_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_chaosb_cd != 0:
                        self.fighting_enemy.enemy_chaosb_cd -= 1
                    if self.fighting_enemy.enemy_fireb_cd != 0:
                        self.fighting_enemy.enemy_fireb_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break

    def warrior_second_vs_corrupted_acolyte(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False

            enemy_action = random.choice(self.fighting_enemy.enemy_menu)

            if enemy_action == "attack":
                enemy_attack_mod = random.uniform(1.2, 1.6)
                self.enemy_attack = round(self.fighting_enemy.stats[2] * enemy_attack_mod)
                self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                if self.player_defence is True:
                    self.enemy_damage = self.enemy_damage//2

                self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                print("The enemy, " + self.fighting_enemy.name + " fires a blast of simple arcane energy and deals ", end="")
                sleep(0.5)
                print(str(self.enemy_damage) + " damage")
                self.combat = True

                if self.fighting_enemy.enemy_chaosb_cd != 0:
                    self.fighting_enemy.enemy_chaosb_cd -= 1
                if self.fighting_enemy.enemy_fireb_cd != 0:
                    self.fighting_enemy.enemy_fireb_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("End Turn")
                sleep(0.5)


            elif enemy_action == "skills":
                enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                if enemy_skill == "chaos bolt":
                    if self.fighting_enemy.enemy_chaosb_cd != 0:
                        continue
                    chaosb_attack_mod = random.uniform(1.6, 1.8)
                    self.enemy_attack = round(self.fighting_enemy.stats[2] * chaosb_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " launches corrupted arcane energy and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_chaosb_cd = 3
                    if self.fighting_enemy.enemy_fireb_cd != 0:
                        self.fighting_enemy.enemy_fireb_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

                elif enemy_skill == "fire bolt":
                    if self.fighting_enemy.enemy_fireb_cd != 0:
                        continue
                    fireb_attack_mod = random.uniform(1.4, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[2] * fireb_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    # checks if enemy is defending
                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " blasts you with a bolt of fire and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_fireb_cd = 3
                    if self.fighting_enemy.enemy_chaosb_cd != 0:
                        self.fighting_enemy.enemy_chaosb_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

            else:
                self.enemy_defence = True
                self.combat = True

                if self.fighting_enemy.enemy_chaosb_cd != 0:
                    self.fighting_enemy.enemy_chaosb_cd -= 1
                if self.fighting_enemy.enemy_fireb_cd != 0:
                    self.fighting_enemy.enemy_fireb_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("The " + self.fighting_enemy.name + " readies for your next attack.")
                print("End Turn")
                sleep(0.5)


            # player turn
            while self.combat:
                sleep(0.35)
                attack_mod = random.uniform(1.2, 1.6)

                print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

                print(self.fighting_player.player_menu)
                action_choice = str.lower(input("Select your action."))

                if action_choice == "attack":
                    self.attack = round(self.fighting_player.stats[0] * attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " damage")
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("You ready yourself for the enemy's next attack.")
                    sleep(0.5)
                    print("End Turn")

                elif action_choice == "skills":
                    print(self.fighting_player.player_skills)
                    skill_choice = str.lower(input())
                    if skill_choice == "big swing":
                        if self.fighting_player.big_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                        sleep(0.5)
                        print(str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.big_cd = 4
                        if self.fighting_player.double_cd != 0:
                            self.fighting_player.double_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break

                        print("End Turn")

                    elif skill_choice == "big swing?":
                        print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                        continue

                    elif skill_choice == "double swing":
                        if self.fighting_player.double_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                            self.damage = self.attack - self.fighting_enemy.enemy_armor

                            # checks if enemy is defending
                            if self.enemy_defence is True:
                                self.damage = self.damage//2

                            self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                            sleep(0.5)
                            print("You deal" + " " + str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.double_cd = 3
                        if self.fighting_player.big_cd != 0:
                            self.fighting_player.big_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                        item_choice = str.lower(input())
                        if item_choice == "back":
                            continue
                    else:
                        print(self.fighting_player.player_items)
                        item_choice = str.lower(input())
                        if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 20
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Medium Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 30
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
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
                break

    def decide_warrior_vs_corrupted_acolyte(self):
        fight_list = [self.warrior_first_vs_corrupted_acolyte, self.warrior_second_vs_corrupted_acolyte]
        if self.fighting_player.stats[1] > self.fighting_enemy.stats[1]:
            self.fight = fight_list[0]
        elif self.fighting_player.stats[1] < self.fighting_enemy.stats[1]:
            self.fight = fight_list[1]
        elif self.fighting_player.stats[1] == self.fighting_enemy.stats[1]:
            self.fight = random.choice(fight_list)

        return self.fight()


class Warrior_vs_goblin:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Goblin()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        self.combat = True

        self.player_defence = False
        self.enemy_defence = False

        self.attack = 0
        self.damage = 0
        self.enemy_attack = 0
        self.enemy_damage = 0

    def warrior_first_vs_goblin(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False
            sleep(0.35)
            attack_mod = random.uniform(1.2, 1.6)

            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = str.lower(input("Select your action."))

            if action_choice == "attack":
                self.attack = round(self.fighting_player.stats[0] * attack_mod)
                self.damage = self.attack - self.fighting_enemy.enemy_armor

                if self.enemy_defence is True:
                    self.damage = self.damage//2

                self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = str.lower(input())
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                    item_choice = str.lower(input())
                    if item_choice == "back":
                        continue
                else:
                    # while self.combat:
                    print(self.fighting_player.player_items)
                    item_choice = str.lower(input())
                    if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                    elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 20
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 30
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
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
                enemy_action = random.choice(self.fighting_enemy.enemy_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " underhandedly strikes you and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_lil_cd != 0:
                        self.fighting_enemy.enemy_lil_cd -= 1
                    if self.fighting_enemy.enemy_knee_cd != 0:
                        self.fighting_enemy.enemy_knee_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                    if enemy_skill == "lil hit":
                        if self.fighting_enemy.enemy_lil_cd != 0:
                            continue
                        lil_attack_mod = random.uniform(1.4, 1.6)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * lil_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " strikes as hard as they can and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_lil_cd = 3
                        if self.fighting_enemy.enemy_knee_cd != 0:
                            self.fighting_enemy.enemy_knee_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "mace knee":
                        if self.fighting_enemy.enemy_knee_cd != 0:
                            continue
                        knee_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * knee_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if player is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " goes for your knees and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_knee_cd = 3
                        if self.fighting_enemy.enemy_lil_cd != 0:
                            self.fighting_enemy.enemy_lil_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_lil_cd != 0:
                        self.fighting_enemy.enemy_lil_cd -= 1
                    if self.fighting_enemy.enemy_knee_cd != 0:
                        self.fighting_enemy.enemy_knee_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break

    def warrior_second_vs_goblin(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False

            enemy_action = random.choice(self.fighting_enemy.enemy_menu)

            if enemy_action == "attack":
                enemy_attack_mod = random.uniform(1.2, 1.6)
                self.enemy_attack = round(self.fighting_enemy.stats[1] * enemy_attack_mod)
                self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                if self.player_defence is True:
                    self.enemy_damage = self.enemy_damage//2

                self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                print("The enemy, " + self.fighting_enemy.name + " underhandedly strikes you and deals ", end="")
                sleep(0.5)
                print(str(self.enemy_damage) + " damage")
                self.combat = True

                if self.fighting_enemy.enemy_lil_cd != 0:
                    self.fighting_enemy.enemy_lil_cd -= 1
                if self.fighting_enemy.enemy_knee_cd != 0:
                    self.fighting_enemy.enemy_knee_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("End Turn")
                sleep(0.5)


            elif enemy_action == "skills":
                enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                if enemy_skill == "lil hit":
                    if self.fighting_enemy.enemy_lil_cd != 0:
                        continue
                    lil_attack_mod = random.uniform(1.4, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * lil_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " strikes as hard as they can and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_lil_cd = 3
                    if self.fighting_enemy.enemy_knee_cd != 0:
                        self.fighting_enemy.enemy_knee_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

                elif enemy_skill == "mace knee":
                    if self.fighting_enemy.enemy_knee_cd != 0:
                        continue
                    knee_attack_mod = random.uniform(1.6, 1.8)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * knee_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    # checks if player is defending
                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " goes for your knees and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_knee_cd = 3
                    if self.fighting_enemy.enemy_lil_cd != 0:
                        self.fighting_enemy.enemy_lil_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

            else:
                self.enemy_defence = True
                self.combat = True

                if self.fighting_enemy.enemy_lil_cd != 0:
                    self.fighting_enemy.enemy_lil_cd -= 1
                if self.fighting_enemy.enemy_knee_cd != 0:
                    self.fighting_enemy.enemy_knee_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("The " + self.fighting_enemy.name + " readies for your next attack.")
                print("End Turn")
                sleep(0.5)


            # player turn
            while self.combat:
                sleep(0.35)
                attack_mod = random.uniform(1.2, 1.6)

                print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

                print(self.fighting_player.player_menu)
                action_choice = str.lower(input("Select your action."))

                if action_choice == "attack":
                    self.attack = round(self.fighting_player.stats[0] * attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " damage")
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("You ready yourself for the enemy's next attack.")
                    sleep(0.5)
                    print("End Turn")

                elif action_choice == "skills":
                    print(self.fighting_player.player_skills)
                    skill_choice = str.lower(input())
                    if skill_choice == "big swing":
                        if self.fighting_player.big_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                        sleep(0.5)
                        print(str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.big_cd = 4
                        if self.fighting_player.double_cd != 0:
                            self.fighting_player.double_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break

                        print("End Turn")

                    elif skill_choice == "big swing?":
                        print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                        continue

                    elif skill_choice == "double swing":
                        if self.fighting_player.double_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                            self.damage = self.attack - self.fighting_enemy.enemy_armor

                            # checks if enemy is defending
                            if self.enemy_defence is True:
                                self.damage = self.damage//2

                            self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                            sleep(0.5)
                            print("You deal" + " " + str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.double_cd = 3
                        if self.fighting_player.big_cd != 0:
                            self.fighting_player.big_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                        item_choice = str.lower(input())
                        if item_choice == "back":
                            continue
                    else:
                        print(self.fighting_player.player_items)
                        item_choice = str.lower(input())
                        if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 20
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Medium Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 30
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
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
                break

    def decide_warrior_vs_goblin(self):
        fight_list = [self.warrior_first_vs_goblin, self.warrior_second_vs_goblin]
        if self.fighting_player.stats[1] > self.fighting_enemy.stats[1]:
            self.fight = fight_list[0]
        elif self.fighting_player.stats[1] < self.fighting_enemy.stats[1]:
            self.fight = fight_list[1]
        elif self.fighting_player.stats[1] == self.fighting_enemy.stats[1]:
            self.fight = random.choice(fight_list)

        return self.fight()


class Warrior_vs_bugbear:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Bugbear()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        self.combat = True

        self.player_defence = False
        self.enemy_defence = False

        self.attack = 0
        self.damage = 0
        self.enemy_attack = 0
        self.enemy_damage = 0

    def warrior_first_vs_bugbear(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False
            sleep(0.35)
            attack_mod = random.uniform(1.2, 1.6)

            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = str.lower(input("Select your action."))

            if action_choice == "attack":
                self.attack = round(self.fighting_player.stats[0] * attack_mod)
                self.damage = self.attack - self.fighting_enemy.enemy_armor

                if self.enemy_defence is True:
                    self.damage = self.damage//2

                self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = str.lower(input())
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                    item_choice = str.lower(input())
                    if item_choice == "back":
                        continue
                else:
                    # while self.combat:
                    print(self.fighting_player.player_items)
                    item_choice = str.lower(input())
                    if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                    elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 20
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 30
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
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
                enemy_action = random.choice(self.fighting_enemy.enemy_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " strikes you viciously and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_club_cd != 0:
                        self.fighting_enemy.enemy_club_cd -= 1
                    if self.fighting_enemy.enemy_charge_cd != 0:
                        self.fighting_enemy.enemy_charge_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                    if enemy_skill == "club":
                        if self.fighting_enemy.enemy_club_cd != 0:
                            continue
                        club_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[0] * club_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " uses both hands to strike you with their weapon and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_club_cd = 3
                        if self.fighting_enemy.enemy_charge_cd != 0:
                            self.fighting_enemy.enemy_charge_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "charge":
                        if self.fighting_enemy.enemy_charge_cd != 0:
                            continue
                        charge_attack_mod = random.uniform(1.4, 1.6)
                        self.enemy_attack = round(self.fighting_enemy.stats[0] * charge_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if player is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " rushes forward using their body as a weapon and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_charge_cd = 3
                        if self.fighting_enemy.enemy_club_cd != 0:
                            self.fighting_enemy.enemy_club_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_club_cd != 0:
                        self.fighting_enemy.enemy_club_cd -= 1
                    if self.fighting_enemy.enemy_charge_cd != 0:
                        self.fighting_enemy.enemy_charge_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break

    def warrior_second_vs_bugbear(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False

            enemy_action = random.choice(self.fighting_enemy.enemy_menu)

            if enemy_action == "attack":
                enemy_attack_mod = random.uniform(1.2, 1.6)
                self.enemy_attack = round(self.fighting_enemy.stats[0] * enemy_attack_mod)
                self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                if self.player_defence is True:
                    self.enemy_damage = self.enemy_damage//2

                self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                print("The enemy, " + self.fighting_enemy.name + " strikes you viciously and deals ", end="")
                sleep(0.5)
                print(str(self.enemy_damage) + " damage")
                self.combat = True

                if self.fighting_enemy.enemy_club_cd != 0:
                    self.fighting_enemy.enemy_club_cd -= 1
                if self.fighting_enemy.enemy_charge_cd != 0:
                    self.fighting_enemy.enemy_charge_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("End Turn")
                sleep(0.5)


            elif enemy_action == "skills":
                enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                if enemy_skill == "club":
                    if self.fighting_enemy.enemy_club_cd != 0:
                        continue
                    club_attack_mod = random.uniform(1.6, 1.8)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * club_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " uses both hands to strike you with their weapon and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_club_cd = 3
                    if self.fighting_enemy.enemy_charge_cd != 0:
                        self.fighting_enemy.enemy_charge_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

                elif enemy_skill == "charge":
                    if self.fighting_enemy.enemy_charge_cd != 0:
                        continue
                    charge_attack_mod = random.uniform(1.4, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * charge_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    # checks if player is defending
                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " rushes forward using their body as a weapon and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_charge_cd = 3
                    if self.fighting_enemy.enemy_club_cd != 0:
                        self.fighting_enemy.enemy_club_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

            else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_club_cd != 0:
                        self.fighting_enemy.enemy_club_cd -= 1
                    if self.fighting_enemy.enemy_charge_cd != 0:
                        self.fighting_enemy.enemy_charge_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)


            # player turn
            while self.combat:
                sleep(0.35)
                attack_mod = random.uniform(1.2, 1.6)

                print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

                print(self.fighting_player.player_menu)
                action_choice = str.lower(input("Select your action."))

                if action_choice == "attack":
                    self.attack = round(self.fighting_player.stats[0] * attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " damage")
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("You ready yourself for the enemy's next attack.")
                    sleep(0.5)
                    print("End Turn")

                elif action_choice == "skills":
                    print(self.fighting_player.player_skills)
                    skill_choice = str.lower(input())
                    if skill_choice == "big swing":
                        if self.fighting_player.big_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                        sleep(0.5)
                        print(str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.big_cd = 4
                        if self.fighting_player.double_cd != 0:
                            self.fighting_player.double_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break

                        print("End Turn")

                    elif skill_choice == "big swing?":
                        print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                        continue

                    elif skill_choice == "double swing":
                        if self.fighting_player.double_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                            self.damage = self.attack - self.fighting_enemy.enemy_armor

                            # checks if enemy is defending
                            if self.enemy_defence is True:
                                self.damage = self.damage//2

                            self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                            sleep(0.5)
                            print("You deal" + " " + str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.double_cd = 3
                        if self.fighting_player.big_cd != 0:
                            self.fighting_player.big_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                        item_choice = str.lower(input())
                        if item_choice == "back":
                            continue
                    else:
                        print(self.fighting_player.player_items)
                        item_choice = str.lower(input())
                        if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 20
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Medium Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 30
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
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
                break

    def decide_warrior_vs_bugbear(self):
        fight_list = [self.warrior_first_vs_bugbear, self.warrior_second_vs_bugbear]
        if self.fighting_player.stats[1] > self.fighting_enemy.stats[1]:
            self.fight = fight_list[0]
        elif self.fighting_player.stats[1] < self.fighting_enemy.stats[1]:
            self.fight = fight_list[1]
        elif self.fighting_player.stats[1] == self.fighting_enemy.stats[1]:
            self.fight = random.choice(fight_list)

        return self.fight()


class Warrior_vs_ogre:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Ogre()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        self.combat = True

        self.player_defence = False
        self.enemy_defence = False

        self.attack = 0
        self.damage = 0
        self.enemy_attack = 0
        self.enemy_damage = 0

    def warrior_first_vs_ogre(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False
            sleep(0.35)
            attack_mod = random.uniform(1.2, 1.6)

            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = str.lower(input("Select your action."))

            if action_choice == "attack":
                self.attack = round(self.fighting_player.stats[0] * attack_mod)
                self.damage = self.attack - self.fighting_enemy.enemy_armor

                if self.enemy_defence is True:
                    self.damage = self.damage//2

                self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = str.lower(input())
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                    item_choice = str.lower(input())
                    if item_choice == "back":
                        continue
                else:
                    # while self.combat:
                    print(self.fighting_player.player_items)
                    item_choice = str.lower(input())
                    if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                    elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 20
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 30
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
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
                enemy_action = random.choice(self.fighting_enemy.enemy_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " lazily swings their club with inhuman strength and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_smash_cd != 0:
                        self.fighting_enemy.enemy_smash_cd -= 1
                    if self.fighting_enemy.enemy_bash_cd != 0:
                        self.fighting_enemy.enemy_bash_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                    if enemy_skill == "smash":
                        if self.fighting_enemy.enemy_smash_cd != 0:
                            continue
                        smash_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[0] * smash_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " with their incredible strength tries to smash you to a pulp and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_smash_cd = 3
                        if self.fighting_enemy.enemy_bash_cd != 0:
                            self.fighting_enemy.enemy_bash_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "bash":
                        if self.fighting_enemy.enemy_bash_cd != 0:
                            continue
                        bash_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[0] * bash_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if player is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " goes to deliver a might blow with their fist and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_bash_cd = 3
                        if self.fighting_enemy.enemy_smash_cd != 0:
                            self.fighting_enemy.enemy_smash_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_smash_cd != 0:
                        self.fighting_enemy.enemy_smash_cd -= 1
                    if self.fighting_enemy.enemy_bash_cd != 0:
                        self.fighting_enemy.enemy_bash_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break

    def warrior_second_vs_ogre(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False

            enemy_action = random.choice(self.fighting_enemy.enemy_menu)

            if enemy_action == "attack":
                enemy_attack_mod = random.uniform(1.2, 1.6)
                self.enemy_attack = round(self.fighting_enemy.stats[0] * enemy_attack_mod)
                self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                if self.player_defence is True:
                    self.enemy_damage = self.enemy_damage//2

                self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                print("The enemy, " + self.fighting_enemy.name + " lazily swings their club with inhuman strength and deals ", end="")
                sleep(0.5)
                print(str(self.enemy_damage) + " damage")
                self.combat = True

                if self.fighting_enemy.enemy_smash_cd != 0:
                    self.fighting_enemy.enemy_smash_cd -= 1
                if self.fighting_enemy.enemy_bash_cd != 0:
                    self.fighting_enemy.enemy_bash_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("End Turn")
                sleep(0.5)


            elif enemy_action == "skills":
                enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                if enemy_skill == "smash":
                    if self.fighting_enemy.enemy_smash_cd != 0:
                        continue
                    smash_attack_mod = random.uniform(1.6, 1.8)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * smash_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " with their incredible strength tries to smash you to a pulp and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_smash_cd = 3
                    if self.fighting_enemy.enemy_bash_cd != 0:
                        self.fighting_enemy.enemy_bash_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

                elif enemy_skill == "bash":
                    if self.fighting_enemy.enemy_bash_cd != 0:
                        continue
                    bash_attack_mod = random.uniform(1.6, 1.8)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * bash_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    # checks if player is defending
                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " goes to deliver a might blow with their fist and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_bash_cd = 3
                    if self.fighting_enemy.enemy_smash_cd != 0:
                        self.fighting_enemy.enemy_smash_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

            else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_smash_cd != 0:
                        self.fighting_enemy.enemy_smash_cd -= 1
                    if self.fighting_enemy.enemy_bash_cd != 0:
                        self.fighting_enemy.enemy_bash_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)


            # player turn
            while self.combat:
                sleep(0.35)
                attack_mod = random.uniform(1.2, 1.6)

                print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

                print(self.fighting_player.player_menu)
                action_choice = str.lower(input("Select your action."))

                if action_choice == "attack":
                    self.attack = round(self.fighting_player.stats[0] * attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " damage")
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("You ready yourself for the enemy's next attack.")
                    sleep(0.5)
                    print("End Turn")

                elif action_choice == "skills":
                    print(self.fighting_player.player_skills)
                    skill_choice = str.lower(input())
                    if skill_choice == "big swing":
                        if self.fighting_player.big_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                        sleep(0.5)
                        print(str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.big_cd = 4
                        if self.fighting_player.double_cd != 0:
                            self.fighting_player.double_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break

                        print("End Turn")

                    elif skill_choice == "big swing?":
                        print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                        continue

                    elif skill_choice == "double swing":
                        if self.fighting_player.double_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                            self.damage = self.attack - self.fighting_enemy.enemy_armor

                            # checks if enemy is defending
                            if self.enemy_defence is True:
                                self.damage = self.damage//2

                            self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                            sleep(0.5)
                            print("You deal" + " " + str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.double_cd = 3
                        if self.fighting_player.big_cd != 0:
                            self.fighting_player.big_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                        item_choice = str.lower(input())
                        if item_choice == "back":
                            continue
                    else:
                        print(self.fighting_player.player_items)
                        item_choice = str.lower(input())
                        if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 20
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Medium Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 30
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
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
                break

    def decide_warrior_vs_ogre(self):
        fight_list = [self.warrior_first_vs_ogre, self.warrior_second_vs_ogre]
        if self.fighting_player.stats[1] > self.fighting_enemy.stats[1]:
            self.fight = fight_list[0]
        elif self.fighting_player.stats[1] < self.fighting_enemy.stats[1]:
            self.fight = fight_list[1]
        elif self.fighting_player.stats[1] == self.fighting_enemy.stats[1]:
            self.fight = random.choice(fight_list)

        return self.fight()


class Warrior_vs_death_dog:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Death_dog()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        self.combat = True

        self.player_defence = False
        self.enemy_defence = False

        self.attack = 0
        self.damage = 0
        self.enemy_attack = 0
        self.enemy_damage = 0

    def warrior_first_vs_death_dog(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False
            sleep(0.35)
            attack_mod = random.uniform(1.2, 1.6)

            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = str.lower(input("Select your action."))

            if action_choice == "attack":
                self.attack = round(self.fighting_player.stats[0] * attack_mod)
                self.damage = self.attack - self.fighting_enemy.enemy_armor

                if self.enemy_defence is True:
                    self.damage = self.damage//2

                self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = str.lower(input())
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                    item_choice = str.lower(input())
                    if item_choice == "back":
                        continue
                else:
                    # while self.combat:
                    print(self.fighting_player.player_items)
                    item_choice = str.lower(input())
                    if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                    elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 20
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 30
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
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
                enemy_action = random.choice(self.fighting_enemy.enemy_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " is out for blood and attacks and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_dmaul_cd != 0:
                        self.fighting_enemy.enemy_dmaul_cd -= 1
                    if self.fighting_enemy.enemy_drend_cd != 0:
                        self.fighting_enemy.enemy_drend_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                    if enemy_skill == "death maul":
                        if self.fighting_enemy.enemy_dmaul_cd != 0:
                            continue
                        # dmaul_attack_mod = random.uniform(1.6, 1.8)
                        #
                        # self.enemy_attack = round(self.fighting_enemy.stats[0] * dmaul_attack_mod)
                        # self.enemy_damage = self.enemy_attack - self.fighting_player.armor
                        #
                        # if self.player_defence is True:
                        #     self.enemy_damage = self.enemy_damage//2
                        #
                        # self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        # print("The " + self.fighting_enemy.name + " strikes as hard as they can and deals ", end="")
                        # sleep(0.5)
                        # print(str(self.enemy_damage) + " damage")
                        # self.combat = True

                        print("The " + self.fighting_enemy.name + " tries to tear you apart.")
                        for i in range(3):
                            dmaul_attack_mod = random.uniform(1.2, 1.4)
                            self.enemy_attack = round(self.fighting_enemy.stats[1] * dmaul_attack_mod)
                            self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                            # checks if enemy is defending
                            if self.player_defence is True:
                                self.enemy_damage = self.enemy_damage//2

                            self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                            sleep(0.5)
                            print(self.fighting_enemy.name + " deals " + str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_dmaul_cd = 3
                        if self.fighting_enemy.enemy_drend_cd != 0:
                            self.fighting_enemy.enemy_drend_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "death rend":
                        if self.fighting_enemy.enemy_drend_cd != 0:
                            continue
                        drend_attack_mod = random.uniform(1.4, 1.6)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * drend_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if player is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " attacks with razor sharp claws and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_drend_cd = 3
                        if self.fighting_enemy.enemy_dmaul_cd != 0:
                            self.fighting_enemy.enemy_dmaul_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_dmaul_cd != 0:
                        self.fighting_enemy.enemy_dmaul_cd -= 1
                    if self.fighting_enemy.enemy_drend_cd != 0:
                        self.fighting_enemy.enemy_drend_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break

    def warrior_second_vs_death_dog(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False

            enemy_action = random.choice(self.fighting_enemy.enemy_menu)

            if enemy_action == "attack":
                enemy_attack_mod = random.uniform(1.2, 1.6)
                self.enemy_attack = round(self.fighting_enemy.stats[1] * enemy_attack_mod)
                self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                if self.player_defence is True:
                    self.enemy_damage = self.enemy_damage//2

                self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                print("The enemy, " + self.fighting_enemy.name + " is out for blood and attacks and deals ", end="")
                sleep(0.5)
                print(str(self.enemy_damage) + " damage")
                self.combat = True

                if self.fighting_enemy.enemy_dmaul_cd != 0:
                    self.fighting_enemy.enemy_dmaul_cd -= 1
                if self.fighting_enemy.enemy_drend_cd != 0:
                    self.fighting_enemy.enemy_drend_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("End Turn")
                sleep(0.5)


            elif enemy_action == "skills":
                enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                if enemy_skill == "death maul":
                    if self.fighting_enemy.enemy_dmaul_cd != 0:
                        continue
                    # dmaul_attack_mod = random.uniform(1.6, 1.8)
                    #
                    # self.enemy_attack = round(self.fighting_enemy.stats[0] * dmaul_attack_mod)
                    # self.enemy_damage = self.enemy_attack - self.fighting_player.armor
                    #
                    # if self.player_defence is True:
                    #     self.enemy_damage = self.enemy_damage//2
                    #
                    # self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    # print("The " + self.fighting_enemy.name + " strikes as hard as they can and deals ", end="")
                    # sleep(0.5)
                    # print(str(self.enemy_damage) + " damage")
                    # self.combat = True

                    print("The " + self.fighting_enemy.name + " tries to tear you apart.")
                    for i in range(3):
                        dmaul_attack_mod = random.uniform(1.2, 1.4)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * dmaul_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if enemy is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        sleep(0.5)
                        print(self.fighting_enemy.name + " deals " + str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_dmaul_cd = 3
                    if self.fighting_enemy.enemy_drend_cd != 0:
                        self.fighting_enemy.enemy_drend_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

                elif enemy_skill == "death rend":
                    if self.fighting_enemy.enemy_drend_cd != 0:
                        continue
                    drend_attack_mod = random.uniform(1.4, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * drend_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    # checks if player is defending
                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " attacks with razor sharp claws and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_drend_cd = 3
                    if self.fighting_enemy.enemy_dmaul_cd != 0:
                        self.fighting_enemy.enemy_dmaul_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

            else:
                self.enemy_defence = True
                self.combat = True

                if self.fighting_enemy.enemy_dmaul_cd != 0:
                    self.fighting_enemy.enemy_dmaul_cd -= 1
                if self.fighting_enemy.enemy_drend_cd != 0:
                    self.fighting_enemy.enemy_drend_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("The " + self.fighting_enemy.name + " readies for your next attack.")
                print("End Turn")
                sleep(0.5)


            # player turn
            while self.combat:
                sleep(0.35)
                attack_mod = random.uniform(1.2, 1.6)

                print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

                print(self.fighting_player.player_menu)
                action_choice = str.lower(input("Select your action."))

                if action_choice == "attack":
                    self.attack = round(self.fighting_player.stats[0] * attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " damage")
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("You ready yourself for the enemy's next attack.")
                    sleep(0.5)
                    print("End Turn")

                elif action_choice == "skills":
                    print(self.fighting_player.player_skills)
                    skill_choice = str.lower(input())
                    if skill_choice == "big swing":
                        if self.fighting_player.big_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                        sleep(0.5)
                        print(str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.big_cd = 4
                        if self.fighting_player.double_cd != 0:
                            self.fighting_player.double_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break

                        print("End Turn")

                    elif skill_choice == "big swing?":
                        print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                        continue

                    elif skill_choice == "double swing":
                        if self.fighting_player.double_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                            self.damage = self.attack - self.fighting_enemy.enemy_armor

                            # checks if enemy is defending
                            if self.enemy_defence is True:
                                self.damage = self.damage//2

                            self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                            sleep(0.5)
                            print("You deal" + " " + str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.double_cd = 3
                        if self.fighting_player.big_cd != 0:
                            self.fighting_player.big_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                        item_choice = str.lower(input())
                        if item_choice == "back":
                            continue
                    else:
                        print(self.fighting_player.player_items)
                        item_choice = str.lower(input())
                        if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 20
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Medium Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 30
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
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
                break

    def decide_warrior_vs_death_dog(self):
        fight_list = [self.warrior_first_vs_death_dog, self.warrior_second_vs_death_dog]
        if self.fighting_player.stats[1] > self.fighting_enemy.stats[1]:
            self.fight = fight_list[0]
        elif self.fighting_player.stats[1] < self.fighting_enemy.stats[1]:
            self.fight = fight_list[1]
        elif self.fighting_player.stats[1] == self.fighting_enemy.stats[1]:
            self.fight = random.choice(fight_list)

        return self.fight()


class Warrior_vs_dragon:

    def __init__(self, fighting_player=Warrior(), fighting_enemy=Dragon()):
        self.fighting_player = fighting_player
        self.fighting_enemy = fighting_enemy
        self.combat = True

        self.player_defence = False
        self.enemy_defence = False

        self.attack = 0
        self.damage = 0
        self.enemy_attack = 0
        self.enemy_damage = 0

    def warrior_first_vs_dragon(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False
            sleep(0.35)
            attack_mod = random.uniform(1.2, 1.6)

            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

            print(self.fighting_player.player_menu)
            action_choice = str.lower(input("Select your action."))

            if action_choice == "attack":
                self.attack = round(self.fighting_player.stats[0] * attack_mod)
                self.damage = self.attack - self.fighting_enemy.enemy_armor

                if self.enemy_defence is True:
                    self.damage = self.damage//2

                self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                sleep(0.5)
                print(str(self.damage) + " damage")
                self.combat = True

                if self.fighting_player.big_cd != 0:
                    self.fighting_player.big_cd -= 1
                if self.fighting_player.double_cd != 0:
                    self.fighting_player.double_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("You ready yourself for the enemy's next attack.")
                sleep(0.5)
                print("End Turn")

            elif action_choice == "skills":
                print(self.fighting_player.player_skills)
                skill_choice = str.lower(input())
                if skill_choice == "big swing":
                    if self.fighting_player.big_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    big_attack_mod = random.uniform(2.1, 2.5)
                    self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.big_cd = 4
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")

                elif skill_choice == "big swing?":
                    print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                    continue

                elif skill_choice == "double swing":
                    if self.fighting_player.double_cd != 0:
                        print("Skill on cooldown.")
                        continue
                    print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                    for i in range(2):
                        double_attack_mod = random.uniform(1.2, 1.6)
                        self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        # checks if enemy is defending
                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        sleep(0.5)
                        print("You deal" + " " + str(self.damage) + " " + "damage")
                    self.combat = True

                    self.fighting_player.double_cd = 3
                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                    item_choice = str.lower(input())
                    if item_choice == "back":
                        continue
                else:
                    # while self.combat:
                    print(self.fighting_player.player_items)
                    item_choice = str.lower(input())
                    if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                    elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 20
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
                        self.fighting_player.player_items.remove('Medium Health Potion')
                        print("Your wounds begin to heal.")
                        sleep(0.5)
                    elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                        # change to functions?
                        self.fighting_player.hp += 30
                        if self.fighting_player.hp > self.fighting_player.max_hp:
                            self.fighting_player.hp = self.fighting_player.max_hp
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
                enemy_action = random.choice(self.fighting_enemy.enemy_menu)

                if enemy_action == "attack":
                    enemy_attack_mod = random.uniform(1.2, 1.6)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * enemy_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The enemy, " + self.fighting_enemy.name + " strikes with frightening power and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    if self.fighting_enemy.enemy_claws_cd != 0:
                        self.fighting_enemy.enemy_claws_cd -= 1
                    if self.fighting_enemy.enemy_tail_cd != 0:
                        self.fighting_enemy.enemy_tail_cd -= 1
                    if self.fighting_enemy.enemy_breathe_cd != 0:
                        self.fighting_enemy.enemy_breathe_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)
                    break

                elif enemy_action == "skills":
                    enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                    if enemy_skill == "claws":
                        if self.fighting_enemy.enemy_claws_cd != 0:
                            continue
                        claws_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[1] * claws_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " slashes with razor sharp claws as deadly as swords and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_claws_cd = 3
                        if self.fighting_enemy.enemy_tail_cd != 0:
                            self.fighting_enemy.enemy_tail_cd -= 1
                        if self.fighting_enemy.enemy_breathe_cd != 0:
                            self.fighting_enemy.enemy_breathe_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "tail whip":
                        if self.fighting_enemy.enemy_tail_cd != 0:
                            continue
                        tail_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[0] * tail_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if player is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("With a tail as big and mighty as a tree, the " + self.fighting_enemy.name + " whips their tail at you and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_tail_cd = 3
                        if self.fighting_enemy.enemy_claws_cd != 0:
                            self.fighting_enemy.enemy_claws_cd -= 1
                        if self.fighting_enemy.enemy_breathe_cd != 0:
                            self.fighting_enemy.enemy_breathe_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                    elif enemy_skill == "breathe fire":
                        if self.fighting_enemy.enemy_breathe_cd != 0:
                            continue
                        breathe_attack_mod = random.uniform(1.6, 1.8)
                        self.enemy_attack = round(self.fighting_enemy.stats[2] * breathe_attack_mod)
                        self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                        # checks if player is defending
                        if self.player_defence is True:
                            self.enemy_damage = self.enemy_damage//2

                        self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                        print("The " + self.fighting_enemy.name + " breathes in and lets loose a roaring flame and deals ", end="")
                        sleep(0.5)
                        print(str(self.enemy_damage) + " damage")
                        self.combat = True

                        self.fighting_enemy.enemy_breathe_cd = 3
                        if self.fighting_enemy.enemy_claws_cd != 0:
                            self.fighting_enemy.enemy_claws_cd -= 1
                        if self.fighting_enemy.enemy_tail_cd != 0:
                            self.fighting_enemy.enemy_tail_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break
                        print("End Turn")
                        sleep(0.5)
                        break
                else:
                    self.enemy_defence = True
                    self.combat = True

                    if self.fighting_enemy.enemy_claws_cd != 0:
                        self.fighting_enemy.enemy_claws_cd -= 1
                    if self.fighting_enemy.enemy_tail_cd != 0:
                        self.fighting_enemy.enemy_tail_cd -= 1
                    if self.fighting_enemy.enemy_breathe_cd != 0:
                        self.fighting_enemy.enemy_breathe_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("The " + self.fighting_enemy.name + " readies for your next attack.")
                    print("End Turn")
                    sleep(0.5)
                    break

    def warrior_second_vs_dragon(self):
        self.combat = True

        while self.combat:
            self.player_defence = False
            self.enemy_defence = False

            enemy_action = random.choice(self.fighting_enemy.enemy_menu)

            if enemy_action == "attack":
                enemy_attack_mod = random.uniform(1.2, 1.6)
                self.enemy_attack = round(self.fighting_enemy.stats[0] * enemy_attack_mod)
                self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                if self.player_defence is True:
                    self.enemy_damage = self.enemy_damage//2

                self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                print("The enemy, " + self.fighting_enemy.name + " strikes with frightening power and deals ", end="")
                sleep(0.5)
                print(str(self.enemy_damage) + " damage")
                self.combat = True

                if self.fighting_enemy.enemy_claws_cd != 0:
                    self.fighting_enemy.enemy_claws_cd -= 1
                if self.fighting_enemy.enemy_tail_cd != 0:
                    self.fighting_enemy.enemy_tail_cd -= 1
                if self.fighting_enemy.enemy_breathe_cd != 0:
                    self.fighting_enemy.enemy_breathe_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("End Turn")
                sleep(0.5)


            elif enemy_action == "skills":
                enemy_skill = random.choice(self.fighting_enemy.enemy_skills)
                if enemy_skill == "claws":
                    if self.fighting_enemy.enemy_claws_cd != 0:
                        continue
                    claws_attack_mod = random.uniform(1.6, 1.8)
                    self.enemy_attack = round(self.fighting_enemy.stats[1] * claws_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " slashes with razor sharp claws as deadly as swords and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_claws_cd = 3
                    if self.fighting_enemy.enemy_tail_cd != 0:
                        self.fighting_enemy.enemy_tail_cd -= 1
                    if self.fighting_enemy.enemy_breathe_cd != 0:
                        self.fighting_enemy.enemy_breathe_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

                elif enemy_skill == "tail whip":
                    if self.fighting_enemy.enemy_tail_cd != 0:
                        continue
                    tail_attack_mod = random.uniform(1.6, 1.8)
                    self.enemy_attack = round(self.fighting_enemy.stats[0] * tail_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    # checks if player is defending
                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("With a tail as big and mighty as a tree, the " + self.fighting_enemy.name + " whips their tail at you and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_tail_cd = 3
                    if self.fighting_enemy.enemy_claws_cd != 0:
                        self.fighting_enemy.enemy_claws_cd -= 1
                    if self.fighting_enemy.enemy_breathe_cd != 0:
                        self.fighting_enemy.enemy_breathe_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

                elif enemy_skill == "breathe fire":
                    if self.fighting_enemy.enemy_breathe_cd != 0:
                        continue
                    breathe_attack_mod = random.uniform(1.6, 1.8)
                    self.enemy_attack = round(self.fighting_enemy.stats[2] * breathe_attack_mod)
                    self.enemy_damage = self.enemy_attack - self.fighting_player.armor

                    # checks if player is defending
                    if self.player_defence is True:
                        self.enemy_damage = self.enemy_damage//2

                    self.fighting_player.hp = self.fighting_player.hp - self.enemy_damage
                    print("The " + self.fighting_enemy.name + " breathes in and lets loose a roaring flame and deals ", end="")
                    sleep(0.5)
                    print(str(self.enemy_damage) + " damage")
                    self.combat = True

                    self.fighting_enemy.enemy_breathe_cd = 3
                    if self.fighting_enemy.enemy_claws_cd != 0:
                        self.fighting_enemy.enemy_claws_cd -= 1
                    if self.fighting_enemy.enemy_tail_cd != 0:
                        self.fighting_enemy.enemy_tail_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("End Turn")
                    sleep(0.5)

            else:
                self.enemy_defence = True
                self.combat = True

                if self.fighting_enemy.enemy_claws_cd != 0:
                    self.fighting_enemy.enemy_claws_cd -= 1
                if self.fighting_enemy.enemy_tail_cd != 0:
                    self.fighting_enemy.enemy_tail_cd -= 1
                if self.fighting_enemy.enemy_breathe_cd != 0:
                    self.fighting_enemy.enemy_breathe_cd -= 1

                if self.fighting_player.hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("Game Over")
                    quit()
                elif self.fighting_enemy.enemy_hp <= 0:
                    print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                    print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                    print("You defeated the enemy" + " " + self.fighting_enemy.name)
                    self.combat = False
                    break
                print("The " + self.fighting_enemy.name + " readies for your next attack.")
                print("End Turn")
                sleep(0.5)


            # player turn
            while self.combat:
                sleep(0.35)
                attack_mod = random.uniform(1.2, 1.6)

                print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))

                print(self.fighting_player.player_menu)
                action_choice = str.lower(input("Select your action."))

                if action_choice == "attack":
                    self.attack = round(self.fighting_player.stats[0] * attack_mod)
                    self.damage = self.attack - self.fighting_enemy.enemy_armor

                    if self.enemy_defence is True:
                        self.damage = self.damage//2

                    self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                    print("Using " + self.fighting_player.weapon[4] + ", you strike the enemy and deal ", end="")
                    sleep(0.5)
                    print(str(self.damage) + " damage")
                    self.combat = True

                    if self.fighting_player.big_cd != 0:
                        self.fighting_player.big_cd -= 1
                    if self.fighting_player.double_cd != 0:
                        self.fighting_player.double_cd -= 1

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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

                    if self.fighting_player.hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("Game Over")
                        quit()
                    elif self.fighting_enemy.enemy_hp <= 0:
                        print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                        print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                        print("You defeated the enemy" + " " + self.fighting_enemy.name)
                        self.combat = False
                        break
                    print("You ready yourself for the enemy's next attack.")
                    sleep(0.5)
                    print("End Turn")

                elif action_choice == "skills":
                    print(self.fighting_player.player_skills)
                    skill_choice = str.lower(input())
                    if skill_choice == "big swing":
                        if self.fighting_player.big_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        big_attack_mod = random.uniform(2.1, 2.5)
                        self.attack = round(self.fighting_player.stats[0] * big_attack_mod)
                        self.damage = self.attack - self.fighting_enemy.enemy_armor

                        if self.enemy_defence is True:
                            self.damage = self.damage//2

                        self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                        print("You raise " + self.fighting_player.weapon[4] + " aloft to deliver a mighty blow and deal ", end="")
                        sleep(0.5)
                        print(str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.big_cd = 4
                        if self.fighting_player.double_cd != 0:
                            self.fighting_player.double_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("You defeated the enemy" + " " + self.fighting_enemy.name)
                            self.combat = False
                            break

                        print("End Turn")

                    elif skill_choice == "big swing?":
                        print("Deal out a strong attack." + "\n" + "Cooldown Time: " + str(self.fighting_player.big_cdt) + "\n" + "Current Cooldown: " + str(self.fighting_player.big_cd))
                        continue

                    elif skill_choice == "double swing":
                        if self.fighting_player.double_cd != 0:
                            print("Skill on cooldown.")
                            continue
                        print("Using " + self.fighting_player.weapon[4] + " you strike twice in one fell swoop.")
                        for i in range(2):
                            double_attack_mod = random.uniform(1.2, 1.6)
                            self.attack = round(self.fighting_player.stats[0] * double_attack_mod)
                            self.damage = self.attack - self.fighting_enemy.enemy_armor

                            # checks if enemy is defending
                            if self.enemy_defence is True:
                                self.damage = self.damage//2

                            self.fighting_enemy.enemy_hp = self.fighting_enemy.enemy_hp - self.damage
                            sleep(0.5)
                            print("You deal" + " " + str(self.damage) + " " + "damage")
                        self.combat = True

                        self.fighting_player.double_cd = 3
                        if self.fighting_player.big_cd != 0:
                            self.fighting_player.big_cd -= 1

                        if self.fighting_player.hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + " " + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_player.hp <= 0 and self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
                            print("Game Over")
                            quit()
                        elif self.fighting_enemy.enemy_hp <= 0:
                            print("Nameless:" + " " + str(self.fighting_player.hp) + "/" + str(self.fighting_player.max_hp))
                            print(self.fighting_enemy.name + ":" + str(self.fighting_enemy.enemy_hp) + "/" + str(self.fighting_enemy.enemy_max_hp))
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
                        item_choice = str.lower(input())
                        if item_choice == "back":
                            continue
                    else:
                        print(self.fighting_player.player_items)
                        item_choice = str.lower(input())
                        if item_choice == "small health potion" and "Small Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 10
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Small Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "medium health potion" and "Medium Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 20
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
                            self.fighting_player.player_items.remove('Medium Health Potion')
                            print("Your wounds begin to heal.")
                            sleep(0.5)
                        elif item_choice == "large health potion" and "Large Health Potion" in self.fighting_player.player_items:
                            # change to functions?
                            self.fighting_player.hp += 30
                            if self.fighting_player.hp > self.fighting_player.max_hp:
                                self.fighting_player.hp = self.fighting_player.max_hp
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
                break

    def decide_warrior_vs_dragon(self):
        fight_list = [self.warrior_first_vs_dragon, self.warrior_second_vs_dragon]
        if self.fighting_player.stats[1] > self.fighting_enemy.stats[1]:
            self.fight = fight_list[0]
        elif self.fighting_player.stats[1] < self.fighting_enemy.stats[1]:
            self.fight = fight_list[1]
        elif self.fighting_player.stats[1] == self.fighting_enemy.stats[1]:
            self.fight = random.choice(fight_list)

        return self.fight()
