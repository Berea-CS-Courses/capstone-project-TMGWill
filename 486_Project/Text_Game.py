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
            print("nope")

    return player_class


# story title
Story().title()

# player
# player = Warrior()
# player = story.select_class()
player = select_class()


# story intro
Story().intro()
# sleep(5)

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
You see a Corrupted Swordsman who appears stronger than the others. You wonder if you should confront from or withdraw till they leave. [confront/withdraw]
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
You see what seems like a Bugbear sleeping not too far away. You could take your chances to sneak around and see if you can find anything or walk away and not risk it. [sneak/leave]
""")
Big_Event = Room("""
You see before you a creature of monstrous size and strength. This monster before you is an ogre which almost guarantees death but would be a worthy feat to slay such a creature.
""")
# is this a sign or some kind of warning; before you can continue to think
Death_Dog_Encounter = Room("""
Two heads are better than one, and twice as dangerous. This monster is a Death Dog and you consider if this is some kind of sign or warning for the battle ahead. Before you can continue to think it attacks like a creature from Hell.
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
Human_Starting_Room.west = Corrupted_Swordsman_Encounter
Corrupted_Swordsman_Encounter.north = Corrupted_Knight_Encounter
Corrupted_Knight_Encounter.west = Corrupted_Acolyte_Encounter
Corrupted_Knight_Encounter.north = New_Weapon_Event
Corrupted_Acolyte_Encounter.west = Convenient_Event
New_Weapon_Event.east = Monster_Starting_Room
Monster_Starting_Room.north = Bugbear_Encounter
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


# possible Nest_Event outcome
@when('investigate')
def investigate():
    if current_room is Nest_Event and current_room.state == "event":
        print("This bird of prey attacks the intruder messing with their home.")
        Warrior_vs_giant_eagle_fight(fighting_player=player, fighting_enemy=Nest_Event.enemy).decide_warrior_vs_giant_eagle()
        print("After dealing with that bird and rifling through the nesting, you see that the shiny nesting were some decent gauntlets")
        player.hands = 4
        current_room.description = "Only the remains of battle and a broken nest are left behind."
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"

# adventurelib function that runs the game
start()

# FIX FIGHTS FOR ENEMIES REMOVE BREAKS
