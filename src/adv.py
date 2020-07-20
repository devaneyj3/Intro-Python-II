from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", [ Item('hammer', 'kills enemies by 1/3 HP')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [ Item('staff', 'preforms magic'), Item('ladder', 'acceses another room')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('gem', 'restore you HP')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('sword', 'kills enemies by half HP'), Item('lucky charms', ' is a leperchaun\'s favorite dish')])
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

name = input('\nWhat is your name? ')

# Make a new player object that is currently in the 'outside' room.
## the current_room argument is connected to the room object from above that is why the room name and description declare in room.py get print out
# room = {
# 'outside':  Room("Outside Cave Entrance",
#                 "North of you, the cave mount beckons"),
# room['outside'] == Room object from room.py: gives us name and description that is printed out in room.py.
# so player_1 has access to the room name and description

player_1 = Player(name, room['outside'])  

player_1.welcomeMessage(name)

def StartGame():
    while playing == True: 

        # prints out the current room and items
        player_room = Room(player_1.current_room.name, player_1.current_room.description, player_1.current_room.items)
        print(f'{player_room}')

        # If current room has items give option to take
        items = player_1.current_room.items
        takeItemOption = input(f'\nWhat to you want to do?\n')
        command = takeItemOption.split()
        if command[0] == 'get':
            for item in items:
                if item.name == command[1]:
                    # create new item object so we can use its method
                    item_obj = Item(item.name, item.description)
                    # take item
                    item_obj.on_take()
                    # add object to player inventory
                    player_1.addToInventory(item_obj)
                    # remove object from room
                    for item_obj in items:
                        player_room.remove_from_room(item)
                else:
                    print('\nThe item is not in this room.\n')
        elif command[0] == 'drop':
            itemToDrop = command[1]
            removedItem = player_1.removeFromInventory(itemToDrop)
            # add dropped item to room
            player_room.addToRoom(removedItem)
        
        elif(command[0] == 'q'):
            quit()
        elif command[0] == 'h':
                print(f'''\n
                        [n] = North
                        [s] = South
                        [e] = East
                        [w] = West
                        [q] = Quit
                        [i] = Inventory
                        [get] [item] = Get an item(sword, staff, etc.) and add it to the inventory.
                        [drop] [item] = Drop an item in your current room
                        \n''')
                continue 
        elif command[0].lower() == "i" or command[0].lower() == "inventory":
            print(player_1.showInventory())
    
        else:# player moves to new room from current room
            player_1.moveToRoom(command[0])

StartGame()

