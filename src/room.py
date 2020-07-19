# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
    
    def __str__(self):
        roomTitle = 'current room'.upper()
        if len(self.items) < 1:
            itemMessage = "There are no items in the room"
        else:
            itemMessage = "Items in the room:"
        output = f"\t{roomTitle}\n\n\t{self.name}\n \t {self.description}\n\n\t\t{itemMessage}\n "
        for i, item in enumerate(self.items):
            output += f'\n\t{i + 1}: {str(item)}'
        return output
    

    def remove_from_room(self, item):
        # print('Item in the remove_from_room func, room.py are: ', self.items)
        for item in self.items:
            self.items.remove(item)
        # print('The passed in item in the remove_from_room func, room.py are: ', item.name) 
    def addToRoom(self, item):
        self.items.append(item)
