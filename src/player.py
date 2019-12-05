# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    # should this have the super() constructor to inherit all
    # properties of Room class?? (like: name, description)

    # NONE bc at begining of game they have nothing
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"Name: {self.name}, Current-Room: {self.current_room}, Inventory: {self.inventory}"

    def on_drop(self):  # you will have to pass in which item to drop
        drop_item = input(
            "Would you like to drop any items from your inventory?(input item name to drop)")
        # the i gets the index and item gets the name in the array on line 14
        for i, item in enumerate(self.inventory):
            if item.name == drop_item:  # you can call item whatever you want in for loops
                del self.inventory[i]
                print('Item successfully removed\n')  # \n gives a new line

    def check_inventory(self):
        if self.inventory:
            print("you currently have\n")
            for i in self.inventory:  # looping thru the inventory array
                print(i.name) #the index of whatever the name is at that specified index
            else:
                print("You currently do not have any items")
