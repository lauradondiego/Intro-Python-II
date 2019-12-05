from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", #name
                     "North of you, the cave mount beckons"), #description

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

item = {
    'knife': Item("knife", "A rusted object"), #create an item using the blueprint I defined in ITEM CLASS
        'hammer': Item("hammer", "a heavy duty weapon"),

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

# Link items together
room['outside'].items = item['knife'] #item coming from line 24 in the ROOM CLASS file
room['foyer'].items = item['hammer']

#
# Main
#



# Make a new player object that is currently in the 'outside' room.
playerName = input("Welcome Player 1, Please enter your name: ")
print("Hello", playerName + "!")
player = Player(playerName, room['outside'])
#
while True:   #while the player is running the game
    # if room is not None:
        print("You are in the: ", player.current_room.name, "room")
        print(f"Room Description: ", player.current_room.description)

        directionInput = input("Please choose a direction: n, s, w, e, OR press q to quit: ")
        validDirection = ["n", "s", "w", "e", "q"]
        if directionInput in validDirection:
            if directionInput == "q":
                print("Godbye, quitter!")
                break
            else: 
                selectedRoom = player.current_room.__getattribute__(f"{directionInput}_to") #player takes name and current room 
                #directionInput giecs us nswe in __getattribute built in function
                # print("selected room", selectedRoom.name) 
                if selectedRoom is not None: #if there is a selected room
                    player.current_room = selectedRoom
                else:
                   print("error")

   # ^ prints out current room name&description




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
