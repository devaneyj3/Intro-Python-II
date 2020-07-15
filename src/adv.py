from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

playing = True

current_room = room['outside']

name = input('\nWhat is your name? ')

# Make a new player object that is currently in the 'outside' room.
## the current_room argument is connected to the room object from above that is why the room name and description declare in room.py get print out
# room = {
# 'outside':  Room("Outside Cave Entrance",
#                 "North of you, the cave mount beckons"),
# room['outside'] == Room object from room.py: gives us name and description that is printed out in room.py.
# so player_1 has access to the room name and description

player_1 = Player(name, current_room)  

player_1.welcomeMessage(name)

def StartGame():
    while playing == True:
        print(f'\n{player_1.current_room}')

        directionOption = input('\nWhere would you like to go? [n][s][e][w][q]\nHint: Type n for North, s for South, e for East, w for West, or type q for to quit.\n')

        # make instance of room object
        roomObj = Room(current_room.name, current_room.description)
        # player moves to new room from current room
        curr = roomObj.moveToRoom(directionOption, current_room)
        ## change the current room of the player object
        player_1.current_room = curr

StartGame()

 # * Prints the current description (the textwrap module might be useful here).
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
