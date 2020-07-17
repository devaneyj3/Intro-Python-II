# Write a class to hold item information, e.g. what room they are in
# currently.

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"The {self.name}, it {self.description}."

    def on_take(self):
        print(f'\nYou have picked up the {self.name}\n')

    
