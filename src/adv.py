from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",  # name
                     "North of you, the cave mount beckons"),  # description

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declare all the items
item = {  # you reference this using 'knife' and in the parens you have name/description
    # create an item using the blueprint I defined in ITEM CLASS
    'knife': Item("Knife", "A rusted crusty old dagger should help you get to the treasure."),
    'hammer': Item("Hammer", "Use this heavy duty weapon to protect against enemies."),
    'gloves': Item("Rubber Gloves", "These gloves will help cover up any fingerprints."),
    'flashlight': Item("Flashlight", "When the night comes, use this tool to help guide you to the hidden treasure. "),
    'key': Item("Golden Key", "You found the Golden Key! Use this to open up the treasure chest!"),

}

# Link items together

# item coming from blueprint in the ROOM CLASS file
room['outside'].items = item['gloves']
room['foyer'].items = item['knife']
room['overlook'].items = item['flashlight']
room['narrow'].items = item['hammer']
room['treasure'].items = item['key']

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
playerName = input("Welcome Player 1, Please enter your name: ")
print("Hello", playerName + "!")
# empty array is referring to items in PLAYER CLASS
# instantiated player here and passed in 3 things
player = Player(playerName, room['outside'], [])
# they empty array is like a backpack where you can store things (we instatiated it to none)
# and you can also perform array methods on it like .append()

while True:  # while the player is running the game
    # if room is not None:
    print("You are in the: ", player.current_room.name, "room")
    print(f"Room Description: ", player.current_room.description)
    # look in the ROOM CLASS for items attribute
    print(f"Available Items: ", player.current_room.items)

    itemInput = input("Pick up available item? Y/N \n")
    validItemPickup = ["y", "n"]

    if itemInput == "y":
        player.inventory.append(player.current_room.items)
        player.check_inventory()  # checking to see if the player actually has inventory
        player.current_room.items.on_take()  # ontake method from the ITEM CLASS
        print(
            f"this room contains the following items: {player.current_room.items}")
    elif itemInput == "n":
        print(f"Okay {playerName}, good luck without a weapon! \n")

    directionInput = input(
        "Choose a direction: n, s, w, e, OR d to drop item, OR i to check inventory, OR q to quit: ")
    validDirection = ["n", "s", "w", "e", "d", "i", "q"]

    if directionInput in validDirection:
        if directionInput == "q":
            print("Godbye, quitter!")
            break
        elif directionInput == "d":
            player.on_drop()  # bc this is in the PLAYER CLASS
        elif directionInput == "i":
            player.check_inventory()
        else:
            selectedRoom = player.current_room.__getattribute__(
                f"{directionInput}_to"
            )  # player takes name and current room
            # directionInput givess us nswe in __getattribute built in function
            # print("selected room", selectedRoom.name)
            if selectedRoom is not None:  # if there is a selected room
                player.current_room = selectedRoom
            else:
                print("error")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
