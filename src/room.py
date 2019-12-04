# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    name = ""
    description = ""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f" Room-Name: {self.name} Room-Description: {self.description}"


obj = Room("Kitchen", "There's something in the dishwasher")
print("ROOM:", obj)
