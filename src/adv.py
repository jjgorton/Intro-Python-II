from player import Player
from room import Room
from item import Item

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


# Declare all the Items

item = {
    'torch': Item("Torch", """Having a long handle, this elaborately decorated torch is already lit"""),

    'watch': Item("Pocket Watch", """Ticking away the seconds, the gold pocket watch has a long thin chain attached to it""")
}


# Assigning each Item's starting position

room['foyer'].add_item(item['torch'])
room['overlook'].add_item(item['watch'])

#
# Main
#

# Greeting:
player_name = input('\nWelcome, adventurer!  What is your name?\n')

# Start position:
player = Player(player_name, room['outside'])

print(
    f'\nYou find yourself next to an {player.current_room.name}\n{player.current_room.description}')

valid_dir = ['n', 's', 'e', 'w']

allowed_cmds = '\nAvailable Commands:\n   "n" - move North\n   "s" - move South\n   "e" - move East\n   "w" - move West\n\n  if you find a sword, try typing "get sword" or "take sword" to pick up the sword\n\n use "drop sword" to put it down.\n\n Type "i" or "inventory" to see what you have are carrying.\n\n  Type "q" to quit the game.\n'

cmds = input('Type "?" to see Available Commands\n>>>').lower()

while not cmds[0] == 'q':

    if cmds[0] in valid_dir:
        player.move(cmds[0])

        for item in player.current_room.items:
            print(item.name)

    elif cmds[0] == 'take' or cmds[0] == 'get':
        player.add_item(cmds[1])

    elif cmds[0] == 'drop':
        for item in player.inventory:
            if item.name == cmds[1]:
                player.remove_item(item)
                player.current_room.add_item(item)
                item.on_drop()
            else:
                print(f"You don't have a {cmds[1]} ")

    else:
        print("\nI don't know what that means. Please use one of the listed commands.\n")

    cmds = input().lower().split()

print(f"Goodbye, {player.name}. Thanks for playing!")
