# Implement a class to hold room information. This should have name and
# description attributes.
class Room:


    def __init__(self, name, description, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    
    def __str__(self):
        return f'self.name = {self.name} \nself.description = {self.description} \nself.n_to = {self.n_to} \nself.s_to = {self.s_to} \nself.e_to = {self.e_to} \nself.w_to = {self.w_to}'


myRoom = Room("Dinning Room", "Capacity with 8 people", "north", "south", "east", "west")

print(myRoom)