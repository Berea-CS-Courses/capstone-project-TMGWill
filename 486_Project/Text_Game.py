# edited no_command_matches function from adventurelib
from Fight_Class import *
from Story_Class import *
from Characters_Class import *
from adventurelib import *


story = story()
# story title
story.title()
# player
# player = warrior()
player = story.select_class()

# story intro
story.intro()

# enemies
bw1 = bad_warrior()
bw2 = bad_warrior()
w1 = wolf()

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
# setting room states for specific rooms
room3.state = "event"
room4.state = "combat"
room5.state = "combat"

# creating exits/paths for rooms
room1.north = room2
room2.north = room3
room3.north = room4
room2.west = room5

# setting the combats for the rooms so they can be called
room4.combat = wolf_fight(fighting_player=player, fighting_enemy=w1).warrior_first_vs_wolf
room5.combat = warrior_fight(fighting_player=player, fighting_enemy=bw2).warrior_second_vs_bad_warrior

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
    # room = current_room.exit(direction)
    # if room:
    #     current_room = room
    # the lines with "if direction..." to "else: print..." were based on code from Youtuber LukeRS
    if direction in current_room.exits():
        current_room = current_room.exit(direction)
        # print(current_room)
    else:
        print("You can't go that way.")

    # check and handles room states
    if current_room.state == "combat":
        print(current_room)
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
        warrior_fight(fighting_player=player, fighting_enemy=bw1).warrior_first_vs_bad_warrior()
        current_room.description = """
You killed that guy
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
