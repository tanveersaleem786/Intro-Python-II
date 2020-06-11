from os import system, name
from game_commands import commands
from game_objects import outside, sword
from player import Player


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


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(outside, sword)

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
    print(f"{str(player)}\n")
    # Read
    user_input = input("What would you like to do (q to quit)? ").lower()

    # Evaluate / Parse
    clear()
    is_game_over = evaluate(player, user_input)
    print()
# Loop
