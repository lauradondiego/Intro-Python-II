# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    currentRoom = ""
    # should this have the super() constructor to inherit all
    # properties of Room class?? (like: name, description)

    def __init__(self, currentRoom):
        self.currentRoom = currentRoom

    def __str__(self):
        return f"Current-Room: {self.currentRoom}"


obj = Player("Kitchen")
print("PLAYER INFO:", obj)
