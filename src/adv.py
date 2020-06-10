from os import system, name
from room import Room
from player import Player

cmd_lookup = {
    "quit": None,
    "q": None,
    "n": Player.move,
    "e": Player.move,
    "s": Player.move,
    "w": Player.move,
}


# Helper Functions
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def is_valid_input(user_input: str):
    cmd_list = cmd_lookup.keys()
    return any(cmd for cmd in cmd_list if cmd == user_input)


def parse(player: Player, user_input: str):
    # execute the command
    if cmd_lookup[user_input]:
        cmd_lookup[user_input](player, user_input)


def evaluate(player: Player, user_input: str):
    is_game_over = False

    if is_valid_input(user_input):
        if (user_input == "q" or user_input == "quit"):
            is_game_over = True

        # print(f"-- command received: '{user_input}' --")
        parse(player, user_input)
    else:
        print("I'm sorry, I don't understand what you mean")

    return is_game_over


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room["outside"])

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
is_game_over = False

while not(is_game_over):
    print("========== ========== ==========")
    print(str(player) + "\n")
    # Read
    user_input = input("What would you like to do (q to quit)? ").lower()

    # Evaluate / Parse
    clear()
    is_game_over = evaluate(player, user_input)
# Loop
