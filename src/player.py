# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item


class Player:
    def __init__(self, current_room: Room):
        self.current_room: Room = current_room
        self.inventory: list = []

    def __str__(self):
        return str(self.current_room)

    def __repr__(self):
        return f"Player: [current_room={self.current_room}]"

    def move(self, *command):
        direction, obj_str = command

        move_to: dict = {
            "n": self.current_room.n_to,
            "north": self.current_room.n_to,
            "e": self.current_room.e_to,
            "east": self.current_room.e_to,
            "s": self.current_room.s_to,
            "south": self.current_room.s_to,
            "w": self.current_room.w_to,
            "west": self.current_room.w_to,
        }

        new_room = move_to[direction]
        if new_room:
            print(direction)
            self.current_room = new_room
        else:
            print("Sorry, you can't go in that direction")

    def take(self, *command):
        cmd_str, item_name = command

        if not(item_name):
            print("Umm! You picked up nothing... Congratulations!")
            return

        item_from_room = self.current_room.remove_item(item_name)
        if item_from_room:
            self.inventory.append(item_from_room)
            item_from_room.on_take()
        else:
            print(f"There is no {item_name} here!")
