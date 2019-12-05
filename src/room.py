# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    # =None if a person does not pass in direction
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, items=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items  # this item is the knife we wrote in the adv file on

    def __str__(self):  # dunder means double underline
        str = f" Room-Name: {self.name}, Description of the room: {self.description}, {self.items}"

    # def getItem(self):
    #     return "Item in Room:" .join([item.name for item in self.items])

    # def getExits(self):
    #     exit = []
    #     if self.n_to is not None:
    #         exit.append("n")
    #     if self.s_to is not None:
    #         exit.append("s")
    #     if self.e_to is not None:
    #         exit.append("e")
    #     if self.w_to is not None:
    #         exit.append("w")
    #     return "possible exits:" .join(exit)


#     def __str__(self):
#         return f"Name: {self.name}, Description: {self.description}"


# itemsInRoom = ItemList("Knife", "It's sharp")
# print("Items in Room", itemsInRoom)

# The room should have name and description attributes.
# The room should also have n_to, s_to, e_to, and w_to
# attributes which point to the room in that respective direction.
