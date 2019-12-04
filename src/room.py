# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    name = ""
    description = ""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f" Room-Name: {self.name}, Description: {self.description}, Directions: N: {self.n_to}, S: {self.s_to}, E: {self.e_to}, W: {self.w_to}"


obj = Room("testFoyer", "testDescription")
print("ROOM:", obj)


# The room should have name and description attributes.
# The room should also have n_to, s_to, e_to, and w_to
# attributes which point to the room in that respective direction.
