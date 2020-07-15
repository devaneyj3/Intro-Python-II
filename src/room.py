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

    def moveToRoom(self, directionOption):
        # If the user enters "q", quit the game.
        if(directionOption == 'q'):
            quit()
        elif(directionOption == 'n'):
            #move player to new room
            print(self.n_to)
            #  self.n_to
        elif(directionOption == 's'):
            #move player to new room
            return self.s_to
        elif(directionOption == 'e'):
            return 'You are going east to ', self.n_to
            #move player to new room
        elif(directionOption == 'w'):
            return self.w_to
            #move player to new room
        else:
            return None