from player import Player

commands = {
    "quit": None,
    "q": None,
    "i": Player.show_inventory,
    "inventory": Player.show_inventory,
    "get": Player.take,
    "take": Player.take,
    "pickup": Player.take,
    "grab": Player.take,
    "drop": Player.drop,
    "remove": Player.drop,
    "n": Player.move,
    "north": Player.move,
    "e": Player.move,
    "east": Player.move,
    "s": Player.move,
    "south": Player.move,
    "w": Player.move,
    "west": Player.move,
}
