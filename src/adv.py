from os import system, name
from player import Player
from room import Room
from item import Item


# Helper Functions
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def is_valid_input(command: str, obj: str = "", *ignore_these):
    if not(command):
        return False

    cmd_list = commands.keys()
    return command in cmd_list


def parse(player: Player, cmd: str, obj: str = "", *ignore_these):
    # execute the command
    if commands[cmd]:
        commands[cmd](player, cmd, obj)


def evaluate(player: Player, user_input: str):
    is_game_over = False

    input_list = user_input.strip().split(" ", 2)
    if is_valid_input(*input_list):
        if (input_list[0] == "q" or input_list[0] == "quit"):
            is_game_over = True

        parse(player, *input_list)
    else:
        print("I'm sorry, I don't understand what you mean")

    return is_game_over


# Available commands
commands = {
    "quit": None,
    "q": None,
    "get": Player.take,
    "take": Player.take,
    "n": Player.move,
    "e": Player.move,
    "s": Player.move,
    "w": Player.move,
}

# Declare the items
items = {
    "torch": Item("Torch", "A rustic wooden handle wrapped in silk."),
    "gold": Item("Gold Ore", "Unrefined, but still worth the time and effort to get."),
    "whip": Item("Whip", """A long, strong, whip made of leather. It's perfect for 
swinging across gaps."""),
    "pickaxe": Item("Pickaxe", "A heafty tool used for mining ore."),
    "item5": Item("Item 05", "some item"),
    "item6": Item("Item 06", "maybe it's nothing"),
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items["torch"], items["whip"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items["gold"]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items["pickaxe"], items["item5"], items["item6"]]),
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

clear()
while not(is_game_over):
    print("========== ========== ==========")
    print(str(player) + "\n")
    # Read
    user_input = input("What would you like to do (q to quit)? ").lower()

    # Evaluate / Parse
    clear()
    is_game_over = evaluate(player, user_input)
# Loop
