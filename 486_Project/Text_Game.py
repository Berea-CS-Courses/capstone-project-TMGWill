from Fight_Class import *
from Characters_Class import *
from adventurelib import *

player = warrior()
bw1 = bad_warrior()
w1 = wolf()

room1 = Room("""
Exit(s): north
A journey of a thousand miles begins with a single step.
""")
room2 = Room("""
Exit(s): north, south
This open area leaves you alone with your thoughts (Yikes).
""")
room3 = Room("""
You see a figure standing a distance away. Do you approach them? (yes/no)
""")
room3a = Room("""
You killed that guy
""")
room3b = Room("""
That guy left and you feel awkward.
""")
room4 = Room("""
A savage beast notices your presence and attacks!
""")

room1.north = room2
room2.north = room3
room3b.north = room4

current_room = room1
print(current_room)
while True:

    def go(direction):
        global current_room
        room = current_room.exit(direction)
        if room:
            current_room = room
            print(current_room)

    direction = input()
    go(direction)

    if current_room is room3:
        fight = input()
        if fight == "yes":
            print("In a manic fit, the person turns on you and attacks!")
            warrior_fight(fighting_player=player, fighting_enemy=bw1).warrior_first_vs_bad_warrior()
            room3a = Room("""
Exit(s): north, south
You killed that guy
            """)
            room2a = Room("""
Exit(s): north
This open area leaves you alone with your thoughts after that fight (Extra Yikes).
            """)
            room3a.south = room2a
            current_room = room3a
            print(current_room)
        elif fight == "no":
            room3b = Room("""
Exit(s): north, south
That person left and you feel awkward.
            """)
            room2b = Room("""
Exit(s): north
This open area leaves you alone with your thoughts after that person left (Feels Weird Man).
            """)
            room3b.south = room2b
            current_room = room3b
            print(current_room)
    room3a.north = room4
    room3b.north = room4
    if current_room is room4:
        wolf_fight(fighting_player=player, fighting_enemy=w1).warrior_first_vs_wolf()
