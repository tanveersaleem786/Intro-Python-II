# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def __str__(self):
        return str(self.current_room)

    def __repr__(self):
        return f"Player: [current_room={self.current_room}]"
