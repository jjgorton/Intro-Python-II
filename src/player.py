# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def move(self, direction):
        if getattr(self.current_room, f'{direction}_to') is not None:
            self.current_room = getattr(self.current_room, f'{direction}_to')

            print(
                f'\nYou have moved to the {self.current_room.name}\n{self.current_room.description}\n')

        else:
            print("Ouch! You bumped into a wall.  Try another direction.")

    def add_item(self, item_name):
        item = None
        for item_obj in self.current_room.items:
            if item_obj.name == item_name:
                item = item_obj
                self.inventory.append(item)
                self.current_room.remove_item(item)
                item.on_take()

        if item == None:
            print(f"{item_name} isn't here")

    def remove_item(self, item_name):
        item = None
        for item_obj in self.inventory:
            if item_obj.name == item_name:
                item = item_obj
                self.inventory.remove(item)
                self.current_room.add_item(item)
                item.on_drop

        if item == None:
            print(f"You don't have {item_name} ")
