# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    name = ""
    current_room = ""
    # should this have the super() constructor to inherit all
    # properties of Room class?? (like: name, description)

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"Name: {self.name}, Current-Room: {self.current_room}"


objPlayer = Player("Laura", "Foyer")
print("PLAYER INFO:", objPlayer)
