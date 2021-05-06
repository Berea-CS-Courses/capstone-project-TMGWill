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


story = Story()

# story title
story.title()

# player
# player = Warrior()
# player = story.select_class()
player = select_class()


# story intro
story.intro()
# sleep(5)

# enemies
bw1 = Corrupted_swordsman()
bw2 = Corrupted_swordsman()
w1 = Wolf()
w2 = Wolf()

# sets state for all rooms to be empty
Room.state = None

# creating rooms and their descriptions
room1 = Room("""
A journey of a thousand miles begins with a single step.
""")
room2 = Room("""
This open area leaves you alone with your thoughts (Yikes).
""")
room3 = Room("""
You see a figure standing a distance away. Do you approach them? (yes/no)
""")
room4 = Room("""
A savage beast notices your presence and attacks!
""")
room5 = Room("""
mean guy first
""")
room6 = Room("""
mean dog first
""")

Beginning_Room = Room("""
A journey of a thousand miles begins with a single step.
""")
Animal_Starting_Room = Room("""
A journey of a thousand miles begins with a single step.
""")
Wolf_Encounter = Room("""
A journey of a thousand miles begins with a single step.
""")
Nest_Event = Room("""
A journey of a thousand miles begins with a single step.
""")
Giant_Eagle_Encounter = Room("""
A journey of a thousand miles begins with a single step.
""")
Dead_Man_Event = Room("""
A journey of a thousand miles begins with a single step.
""")
Giant_Lizard_Encounter = Room("""
A journey of a thousand miles begins with a single step.
""")
Human_Starting_Room = Room("""
A journey of a thousand miles begins with a single step.
""")
Corrupted_Swordsman_Encounter = Room("""
A journey of a thousand miles begins with a single step.
""")
Corrupted_Swordsman_Encounter_2 = Room("""
A journey of a thousand miles begins with a single step.
""")
Corrupted_Acolyte_Encounter = Room("""
A journey of a thousand miles begins with a single step.
""")
Convenient_Event = Room("""
A journey of a thousand miles begins with a single step.
""")
New_Weapon_Event = Room("""
A journey of a thousand miles begins with a single step.
""")
Monster_Starting_Room = Room("""
A journey of a thousand miles begins with a single step.
""")
Bugbear_Encounter = Room("""
A journey of a thousand miles begins with a single step.
""")
Goblin_Encounter = Room("""
A journey of a thousand miles begins with a single step.
""")
Sleeping_Event = Room("""
A journey of a thousand miles begins with a single step.
""")
Big_Event = Room("""
A journey of a thousand miles begins with a single step.
""")
Death_Dog_Encounter = Room("""
A journey of a thousand miles begins with a single step.
""")
Dragon_Intro = Room("""
A journey of a thousand miles begins with a single step.
""")
Dragon_Encounter = Room("""
A journey of a thousand miles begins with a single step.
""")
# setting room states for specific rooms
room3.state = "event"
room4.state = "combat"
room5.state = "combat"
room6.state = "combat"

# enemies
room4.enemy = Wolf()

# creating exits/paths for rooms
room1.north = room2
room2.north = room3
room3.north = room4
room2.west = room5
room2.east = room6

Beginning_Room.north = Animal_Starting_Room
Animal_Starting_Room.north = Wolf_Encounter
Wolf_Encounter.west = Nest_Event
Wolf_Encounter.north = Dead_Man_Event
Nest_Event.north = Giant_Eagle_Encounter
Dead_Man_Event.west = Giant_Eagle_Encounter
Dead_Man_Event.east = Giant_Lizard_Encounter
Giant_Lizard_Encounter.north = Human_Starting_Room
Human_Starting_Room.west = Corrupted_Swordsman_Encounter
Corrupted_Swordsman_Encounter.north = Corrupted_Swordsman_Encounter_2
Corrupted_Swordsman_Encounter_2.west = Corrupted_Acolyte_Encounter
Corrupted_Swordsman_Encounter_2.north = New_Weapon_Event
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
room4.combat = Warrior_vs_wolf_fight(fighting_player=player, fighting_enemy=room4.enemy).warrior_first_vs_wolf
room5.combat = Warrior_vs_bad_warrior_fight(fighting_player=player, fighting_enemy=bw2).warrior_second_vs_bad_warrior
room6.combat = Warrior_vs_wolf_fight(fighting_player=player, fighting_enemy=w2).warrior_second_vs_wolf

current_room = room1
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
        print("Only the remains of battle are left behind")
        current_room.description = "Only the remains of battle were left behind"
        current_room.state = "empty"

    elif current_room.state == "event":
        print(current_room)

    else:
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)


# room3 possible event outcome
@when('yes')
def yes():
    if current_room is room3 and current_room.state == "event":
        # current_room.combat = True
        print("In a manic fit, the person turns on you and attacks!")
        Warrior_vs_bad_warrior_fight(fighting_player=player, fighting_enemy=bw1).warrior_first_vs_bad_warrior()
        current_room.description = """
The remains of the insane are all that's left.
        """
        room2.description = """
This open area leaves you alone with your thoughts after that fight (Extra Yikes).
        """
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# room3 possible event outcome
@when('no')
def no():
    if current_room is room3 and current_room.state == "event":
        current_room.description = """
That person left and you feel awkward.
        """
        room2.description = """
This open area leaves you alone with your thoughts after that person left (Feels Weird Man).
        """
        print("Exit(s):" + " " + str(current_room.exits()))
        print(current_room)
        current_room.state = "empty"


# adventurelib function that runs the game
start()
