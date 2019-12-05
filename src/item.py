# Create a file called item.py and add an Item class in there.
# The item should have name and description attributes.


class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"

    def on_take(self):
        print(f"You have picked up {self.name}")

# objItem = Item("Hammer", "Heavy duty")
# print("ITEM", objItem)
