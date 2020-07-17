# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    
    def __str__(self):
        return f"{self.name} is at the {self.current_room}."

    def welcomeMessage(self,name):
            welcomeMessage = (f'\nAt the king castle, {name} is summoned. The king tells you that you must save the princess from evil leperchauns. Will you embark on an adventure to find their lucky charms to save the princess. You leave the castle.\n')
            print(welcomeMessage)
            return name

    def moveToRoom(self, directionOption):
        # If the user enters "q", quit the game.
        attribute = directionOption + '_to'
        if directionOption == "i":
            print(self.showInventory())
        elif hasattr(self.current_room, attribute): 
            self.current_room = getattr(self.current_room, attribute)
        else:
            print('Choose another direction') 

    def addToInventory(self, item):
        print(f'You have added a {item.name} to your inventory')
        self.inventory.append(item)
        
    def showInventory(self):
        inventoryMessage = f'\nYou have {len(self.inventory)} items in your inventory\n'
        for index, item in enumerate(self.inventory):
            inventoryMessage += f'\n\t{index + 1}: {item}\n'
        print(inventoryMessage)
