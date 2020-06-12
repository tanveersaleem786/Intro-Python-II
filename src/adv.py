from room import Room
from player import Player
from item import Item

# Declare item
item1 = Item("knif", "sharp knif")
item2 = Item("coin", "small coin")
item3 = Item("gold", "gold piece")
item4 = Item("road", "Steal road")
item5 = Item("gun", "small gun")
item6 = Item("riffle", "riffle description")
item7 = Item("arrow", "arrow description")
item8 = Item("Boat", "Boat description")
item9 = Item("bottle", "bottle description")

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item1, item2]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item3, item4]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item5]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item6, item7]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item8, item9]),
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
player = Player('Tanveer', room['outside'])
# Write a loop that:
while True:    
    # * P(rints the current room name
    print(f"\n{player.name} you are currently in {player.current_room.name}")
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
    # *Print current room items
    item_list = ''
    i = 1
    for item in player.current_room.items:
        item_list += f'\n {i}. {item.name}'
        i += 1
    
    if item_list == '':
        print("There is no item in this room")
    else:
        print(f"\nList of Items available in the room  {item_list}")  
              
    # * Waits for user input and decides what to do.
    print("\n\nList of Commands")
    print("********************************************************\n")
    print("(n) - Move North")
    print("(s) - Move South")
    print("(e) - Move East")
    print("(w) - Move West")
    print("(take/get itemName) - Grab Item")
    print("(drop itemName)     - Release Item")
    print("(i) - Inventory")
    print("(q) - Quit")
    print("\n********************************************************\n")
    choice = input("Enter your command here : ")
    choice = choice.split(" ", 2)
    
    # If the user enters a cardinal direction, attempt to move to the room there.
    try:
        if choice[0] in {'n', 's','e', 'w'}:
            if hasattr(player.current_room, f'{choice[0]}_to'):
                player.current_room = getattr(player.current_room, f'{choice[0]}_to')
            else:
                print("This location does not exist.")
                
            
            #if choice[0] == 'n' or choice[0] == 'e' or choice[0] == 's' or choice[0] == 'w':
            #new_location = getattr(player.current_room, '%s_to' % choice[0])        
            # if not new_location:
            #     print("This location does not exist.")
            # else:
            #     player.current_room = new_location
                
        elif choice[0] == 'i' or choice[0] == 'inventory':
            inventory_list = ''
            t = 1
            for item in player.inventory:
                inventory_list += f'\n {t}. {item.name}'
                t += 1
            
            if inventory_list == '':
                print("There is no item in player inventory")
            else:
                print(f'\n Items in player inventory {inventory_list}')

        elif  choice[0] == 'q' or choice[0] == 'quit':
            break

        elif choice[0] == "get" or choice[0] == "take":
            picked_item = player.current_room.find_item(choice[1])
            #if picked_item is None:
            if not picked_item:
               print(f"The '{choice[1]}' does not exist in the room.")
            else:   
                player.take_item(picked_item)
                player.current_room.remove_item(picked_item)                
                picked_item.on_take()
        
        elif choice[0] == "drop":
            dropped_item = player.find_item(choice[1])
            if not dropped_item:
               print(f"The '{choice[1]}' does not exist in player's inventory.")
            else:
                player.current_room.add_item(dropped_item)
                player.drop_item(dropped_item)
                dropped_item.on_drop()

        # Print an error message if the movement isn't allowed.
        else:
            print("Command does not exist.")
    

    # If the user enters "q", quit the game.
    except:
        print("somthing wrong")