# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # this makes it so that when you call room in adv.py it get these traits
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None
    
    def __str__(self):
        return f"{self.name}\n {self.description}"

    def moveToRoom(self, directionOption, current_room):
        # If the user enters "q", quit the game.
        if(directionOption == 'q'):
            quit()
        elif(directionOption == 'n'):
            print(f'\nYou are going north to the {current_room.n_to}\n')
            #move player to new room
            return current_room.n_to
            #  self.n_to
        elif(directionOption == 's'):
            print(f'\nYou are going south to the {current_room.s_to}\n')
            #move player to new room
            return current_room.s_to
        elif(directionOption == 'e'):
            print(f'\nYou are going east to the {current_room.e_to}\n')
            return current_room.e_to
            #move player to new room
        elif(directionOption == 'w'):
            print(f'\nYou are going west to the {current_room.w_to}\n')
            return current_room.w_to
            #move player to new room
        else:
            return None