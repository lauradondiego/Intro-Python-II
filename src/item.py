# Create a file called item.py and add an Item class in there.
# The item should have name and description attributes.


class Item:
    name = ""
    description = ""

    def __init__(self, anme, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"


objItem = Item("Hammer", "Heavy duty")
print("ITEM", objItem)
