# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def __str__(self):
        return f"{self.name} is at the {self.current_room}."

    def welcomeMessage(self,name):
            welcomeMessage = (f'\nAt the king castle, {name} is summoned. The king tells you that you must save the princess from evil leperchauns. Will you embark on an adventure to find their lucky charms to save the princess. You leave the castle.\n')
            print(welcomeMessage)
            return name