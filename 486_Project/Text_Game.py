# edited no_command_matches function from adventurelib
from Fight_Class import *
from Story_Class import *
from Characters_Class import *
from adventurelib import *


def select_class():
    while True:
        print("""
Available Classes:
[1]Warrior
        """)

        choice = str.lower(input("Choose your class."))

        if choice == "warrior":
            player_class = Warrior()
            break

        else:
            print("You must select a class.")

    return player_class


# story title
Story().title()

# player
player = select_class()

# story intro
Story().intro()
sleep(5)

# sets state for all rooms to be None
Room.state = None

# creating rooms and their descriptions
Beginning_Room = Room("""
A journey of a thousand miles begins with a single step.
""")
Animal_Starting_Room = Room("""
As you begin your journey you notice a sinister presence around you. You see before you dangerous wildlife that appear bloodthirstier than normal.
""")
Wolf_Encounter = Room("""
This savage beast notices your presence and attacks!
""")
Nest_Event = Room("""
You hear the call of a bird and see a shiny nest. Do you satisfy your curiosity or walk away? [investigate/ignore]
""")
Giant_Eagle_Encounter = Room("""
You hear it before you see as a Giant Eagle swoops down to attack you.
""")
Dead_Man_Event = Room("""
You see the remains of someone who wasn't so lucky. There might be something good but would it be worth it? [rummage/respect]
""")
Giant_Lizard_Encounter = Room("""
This large scaled beast turns to approach and attacks!
""")
Human_Starting_Room = Room("""
The sinister feeling and presence of corruption grows more noticeable. You notice before you people that have been corrupted by the dragon's influence.
""")
Corrupted_Swordsman_Encounter = Room("""
The corrupted fighter swayed by the dragon attacks without a second thought.
""")
Corrupted_Knight_Encounter = Room("""
This armored warrior tainted by the dragon's influence attacks with no hesitation.
""")
Corrupted_Acolyte_Encounter = Room("""
A magic user corrupted by the dragon's influence prepares to attack.
""")
Convenient_Event = Room("""
A campfire is still lit but your eyes are drawn to the armor lying there. No one's there but they could come back any moment. [advance/retreat]
""")
New_Weapon_Event = Room("""
You see a Corrupted Swordsman who appears ready for a fight. You wonder if you should confront from or withdraw till they leave. [confront/withdraw]
""")
# close to suffocating?
Monster_Starting_Room = Room("""
The feeling of corruption is strong and before you are creatures inhumane in nature.
""")
Bugbear_Encounter = Room("""
A powerfully built creature matching your height rushes forward to attack.
""")
Goblin_Encounter = Room("""
Out of the corner of your eye you notice some creature lurking. As it realizes that you noticed, it springs forward to attack.
""")
# with your back to it attacks
Sleeping_Event = Room("""
You see what seems like a Bugbear sleeping not too far away. 
You could take your chances to sneak around and see if you can find anything or walk away and not risk it. [sneak/leave]
""")
Big_Event = Room("""
You see before you a creature of monstrous size and strength. 
This monster before you is an ogre which almost guarantees death but would be a worthy feat to slay such a creature.
[glory/life]
""")
# is this a sign or some kind of warning; before you can continue to think
Death_Dog_Encounter = Room("""
Two heads are better than one, and twice as dangerous. 
This monster is a Death Dog and you consider if this is some kind of sign or warning for the battle ahead. 
Before you can continue to think it attacks like a creature from Hell.
""")
Dragon_Intro = Room(Story().final_dialogue())
Dragon_Encounter = Room("""
It feels like what stands before you is some kind of incarnation of death and destruction itself.
""")
# setting room states for specific rooms
Wolf_Encounter.state = "combat"
Nest_Event.state = "event"
Giant_Eagle_Encounter.state = "combat"
Dead_Man_Event.state = "event"
Giant_Lizard_Encounter.state = "combat"
Corrupted_Swordsman_Encounter.state = "combat"
Corrupted_Knight_Encounter.state = "combat"
Corrupted_Acolyte_Encounter.state = "combat"
Convenient_Event.state = "event"
New_Weapon_Event.state = "event"
Bugbear_Encounter.state = "combat"
Goblin_Encounter.state = "combat"
Sleeping_Event.state = "event"
Big_Event.state = "event"
Death_Dog_Encounter.state = "combat"
Dragon_Encounter.state = "combat"

# enemies
Wolf_Encounter.enemy = Wolf()
Nest_Event.enemy = Giant_eagle()
Giant_Eagle_Encounter.enemy = Giant_eagle()
Giant_Lizard_Encounter.enemy = Giant_lizard()
Corrupted_Swordsman_Encounter.enemy = Corrupted_swordsman()
Corrupted_Knight_Encounter.enemy = Corrupted_knight()
Corrupted_Acolyte_Encounter.enemy = Corrupted_acolyte()
Convenient_Event.enemy = Corrupted_knight()
New_Weapon_Event.enemy = Corrupted_swordsman()
Bugbear_Encounter.enemy = Bugbear()
Goblin_Encounter.enemy = Goblin()
Sleeping_Event.enemy = Bugbear()
Big_Event.enemy = Ogre()
Death_Dog_Encounter.enemy = Death_dog()
Dragon_Encounter.enemy = Dragon()

# creating exits/paths for rooms
Beginning_Room.north = Animal_Starting_Room
Animal_Starting_Room.north = Wolf_Encounter
Wolf_Encounter.west = Nest_Event
Wolf_Encounter.north = Dead_Man_Event
Nest_Event.north = Giant_Eagle_Encounter
Dead_Man_Event.west = Giant_Eagle_Encounter
Dead_Man_Event.east = Giant_Lizard_Encounter
Giant_Lizard_Encounter.north = Human_Starting_Room
Human_Starting_Room.west = New_Weapon_Event
Corrupted_Swordsman_Encounter.south = Corrupted_Knight_Encounter
Corrupted_Knight_Encounter.west = Convenient_Event
Corrupted_Knight_Encounter.south = New_Weapon_Event
Corrupted_Acolyte_Encounter.east = Convenient_Event
# New_Weapon_Event.east = Monster_Starting_Room
Monster_Starting_Room.north = Bugbear_Encounter
Monster_Starting_Room.west = Corrupted_Swordsman_Encounter
Bugbear_Encounter.north = Goblin_Encounter
Goblin_Encounter.west = Sleeping_Event
Goblin_Encounter.north = Death_Dog_Encounter
Goblin_Encounter.east = Big_Event
Death_Dog_Encounter.north = Dragon_Intro
Dragon_Intro.north = Dragon_Encounter

# setting the combats for the rooms so they can be called
Wolf_Encounter.combat = Warrior_vs_wolf_fight(fighting_player=player, fighting_enemy=Wolf_Encounter.enemy).decide_warrior_vs_wolf_fight
Giant_Eagle_Encounter.combat = Warrior_vs_giant_eagle_fight(fighting_player=player, fighting_enemy=Giant_Eagle_Encounter.enemy).decide_warrior_vs_giant_eagle
Giant_Lizard_Encounter.combat = Warrior_vs_giant_lizard_fight(fighting_player=player, fighting_enemy=Giant_Lizard_Encounter.enemy).decide_warrior_vs_giant_lizard
Corrupted_Swordsman_Encounter.combat = Warrior_vs_corrupted_swordsman_fight(fighting_player=player, fighting_enemy=Corrupted_Swordsman_Encounter.enemy).decide_warrior_vs_corrupted_swordsman
Corrupted_Knight_Encounter.combat = Warrior_vs_corrupted_knight_fight(fighting_player=player, fighting_enemy=Corrupted_Knight_Encounter.enemy).decide_warrior_vs_corrupted_knight
Corrupted_Acolyte_Encounter.combat = Warrior_vs_corrupted_acolyte_fight(fighting_player=player, fighting_enemy=Corrupted_Acolyte_Encounter.enemy).decide_warrior_vs_corrupted_acolyte
Bugbear_Encounter.combat = Warrior_vs_bugbear(fighting_player=player, fighting_enemy=Bugbear_Encounter.enemy).decide_warrior_vs_bugbear
Goblin_Encounter.combat = Warrior_vs_goblin(fighting_player=player, fighting_enemy=Goblin_Encounter.enemy).decide_warrior_vs_goblin
Death_Dog_Encounter.combat = Warrior_vs_death_dog(fighting_player=player, fighting_enemy=Death_Dog_Encounter.enemy).decide_warrior_vs_death_dog
Dragon_Encounter.combat = Warrior_vs_dragon(fighting_player=player, fighting_enemy=Dragon_Encounter.enemy).decide_warrior_vs_dragon

# beginning of code for game
current_room = Beginning_Room
print("Exit(s):" + " " + str(current_room.exits()))
print(current_room)


@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
@when('n', direction='north')
@when('s', direction='south')
@when('e', direction='east')
@when('w', direction='west')
def go(direction):
    global current_room
    # the lines with "if direction..." to "else: print..." were based on code from Youtuber LukeRS
    if direction in current_room.exits():
        current_room = current_room.exit(direction)
    else:
        print("You can't go that way.")

    # check and handles room states
    if current_room.state == "combat":
        print(current_room)
        sleep(1)
        current_room.combat()
        print(current_room.exits())
        print("Only the remains of battle are left behind.")
        current_room.description = "Only the remains of battle were left behind."
        current_room.state = "empty"

    elif current_room.state == "event":
        print(current_room)

    else:
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"

    # used for game ending
    if current_room is Dragon_Encounter and current_room.state == "empty":
        Story().epilogue()
        name = input("What's your name brave hero?")
        print("Now everyone will know the name " + name + " and tell your story for years to come.")
        quit()


# possible Nest_Event outcome
@when('investigate')
def investigate():
    if current_room is Nest_Event and current_room.state == "event":
        print("This bird of prey attacks the intruder messing with their home.")
        Warrior_vs_giant_eagle_fight(fighting_player=player, fighting_enemy=Nest_Event.enemy).decide_warrior_vs_giant_eagle()
        print("After dealing with that bird and rifling through the nesting, you see that the shiny nesting were some decent gauntlets")
        # player.hands = 3
        player.hands = 4
        current_room.description = "Only the remains of battle and a broken nest are left behind."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# possible Nest_Event outcome
@when('ignore')
def ignore():
    if current_room is Nest_Event and current_room.state == "event":
        current_room.description = "You decide that it would better to play it safe and avoid being bird food."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# possible Dead_Man_Event outcome
@when('rummage')
def rummage():
    if current_room is Dead_Man_Event and current_room.state == "event":
        print("After searching the body you managed to find some potions that clean and some covered in blood.")
        print("You might as well keep them since the dead won't be needing it.")
        player.player_items.append("Medium Health Potion")
        player.player_items.append("Medium Health Potion")
        player.player_items.append("Large Health Potion")
        current_room.description = "All that remains is the memory of assistance from someone soon to be one with the world."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# possible Dead_Man_Event outcome
@when('respect')
def respect():
    if current_room is Dead_Man_Event and current_room.state == "event":
        print("It feels like the dead should be left to rest. You silently and quickly pay your respects and continue onward.")
        current_room.description = "All that's left is a reminder of what could happen if you're not careful."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# possible Convenient_Event outcome
@when('advance')
def advance():
    if current_room is Convenient_Event and current_room.state == "event":
        print("You go forward to see what you find. Not too long after you walk forward you hear the clank of armor.")
        print("They might not be a good guy but you are trying to steal from them.")
        Warrior_vs_corrupted_knight_fight(fighting_player=player, fighting_enemy=Convenient_Event.enemy).decide_warrior_vs_corrupted_knight()
        print("You manage to acquire a pretty decent helmet and greaves")
        # player.head = 1
        # player.legs = 2
        player.head = 2
        player.legs = 3
        current_room.description = "The dead knight is a reminder that everything has price."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# possible Convenient_Event outcome
@when('retreat')
def retreat():
    if current_room is Convenient_Event and current_room.state == "event":
        print("It seems smarter not to take the risk and avoid confrontation.")
        current_room.description = "Avoiding this area would be the smart move."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# possible New_Weapon_Event outcome
@when('confront')
def confront():
    if current_room is New_Weapon_Event and current_room.state == "event":
        print("It'd be faster to face them head-on than waiting around.")
        Warrior_vs_corrupted_swordsman_fight(fighting_player=player, fighting_enemy=New_Weapon_Event.enemy).decide_warrior_vs_corrupted_swordsman()
        print("It almost feels like the swordsman's blade speaks out to you.")
        print("It seems like a fine weapon so you take it for yourself.")
        player.weapon = [3, 3, 0, 3, "Damaged Corruption"]
        player.stats = [player.base_stats[i] + player.weapon[i] for i in range(len(player.base_stats))]
        player.new_max_hp()
        current_room.description = " This is where you got that dark blade."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# possible New_Weapon_Event outcome
@when('withdraw')
def withdraw():
    if current_room is New_Weapon_Event and current_room.state == "event":
        print("You decide to wait it out but use the time to sharpen your blade.")
        player.weapon = [3, 1, 0, 2, "Sharp Trusty Sword"]
        player.stats = [player.base_stats[i] + player.weapon[i] for i in range(len(player.base_stats))]
        current_room.description = " This where you spent the time to sharpen your trusty sword."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# possible Sleeping_Event outcome
@when('sneak')
def sneak():
    if current_room is Sleeping_Event and current_room.state == "event":
        print("As you get close, you notice movement from the Bugbear and realize it was waiting to pounce.")
        Warrior_vs_bugbear(fighting_player=player, fighting_enemy=Sleeping_Event.enemy).decide_warrior_vs_bugbear()
        player.player_items.append("Medium Health Potion")
        player.player_items.append("Medium Health Potion")
        player.player_items.append("Large Health Potion")
        player.player_items.append("Large Health Potion")
        print("You take your spoils of battle which were some useful looking potions.")
        current_room.description = "All that remains is a monster's failed ambush."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# possible Sleeping_Event outcome
@when('leave')
def leave():
    if current_room is Sleeping_Event and current_room.state == "event":
        print("You think its better to be safe than sorry and decide to leave things be and move on.")
        current_room.description = " It's better to let sleeping cats...or dogs...sleep or whatever they say."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# possible Big_Event outcome
@when('glory')
def glory():
    if current_room is Big_Event and current_room.state == "event":
        print(" Today is a good day to die.")
        Warrior_vs_ogre(fighting_player=player, fighting_enemy=Big_Event.enemy).decide_warrior_vs_ogre()
        print("After that battle you take a trophy as proof of your victory.")
        print("Oddly and grossly enough, this Ogre's Toothpick seems like a pretty decent weapon.")
        player.weapon = [4, 0, 0, 4, "Ogre's Toothpick"]
        # player.weapon = [6, 0, 0, 6, "Ogre's Toothpick"]
        player.stats = [player.base_stats[i] + player.weapon[i] for i in range(len(player.base_stats))]
        player.new_max_hp()
        current_room.description = " This is where you got that gross but pretty strong weapon."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# possible Big_Event outcome
@when('life')
def life():
    if current_room is Big_Event and current_room.state == "event":
        print("You'd rather live to see another day.")
        current_room.description = " This where you spent the time to sharpen your trusty sword."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# adventurelib function that runs the game
start()
