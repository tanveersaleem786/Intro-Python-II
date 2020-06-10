# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, current_room: Room):
        self.current_room: Room = current_room

    def __str__(self):
        return str(self.current_room)

    def __repr__(self):
        return f"Player: [current_room={self.current_room}]"

    def move(self, *direction):
        move_in: dict = {
            "n": self.current_room.n_to,
            "e": self.current_room.e_to,
            "s": self.current_room.s_to,
            "w": self.current_room.w_to,
        }

        new_room = move_in[direction[0]]
        if (new_room):
            print(direction[0])
            self.current_room = new_room
        else:
            print("Sorry, you can't go in that direction")
