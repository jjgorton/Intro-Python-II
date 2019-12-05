# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        if getattr(self.current_room, f'{direction}_to') is not None:
            self.current_room = getattr(self.current_room, f'{direction}_to')

            print(f'\nYou have moved to the {self.current_room.name}\n{self.current_room.description}\n')

        else:
            print("Ouch! You bumped into a wall.  Try another direction.")
