import random


class living():

    def __init__(self, name, health, strength, intellect, location):
        self.health = random.randint(50, 101)
        self.strength = random.randint(50, 101)
        self.intellect = random.randint(50, 101)
        self.location = [0, 0]

    def check_in_bounds(self):
        if self.location[0] < 0:
            self.location[0] = 0
        if self.location[1] < 0:
            self.location[1] = 0
        if self.location[0] > 100:
            self.location[0] = 100
        if self.location[1] > 100:
            self.location[1] = 100

    def move(self):
        self.location[0] += random.randint(-5, 6)
        self.location[1] += random.randint(-5, 6)
        self.check_in_bounds()

    def fight(self, foe):
        foe_stats = foe.strength + foe.health + foe.intellect
        current_stats = self.strength + self.health + self.intellect + 10
        win_rate = 50
        win_rate += current_stats - foe_stats
        run = random.randint(1, 101)

        return run <= win_rate

    def convert(obj, source_list, target_class, target_list):
        """
        Converts an object to a different class and moves it between lists.

        Args:
            obj: The object to convert
            source_list: The list containing the original object
            target_class: The class to convert the object to
            target_list: The list to add the converted object to

        Returns:
            tuple: (updated target_list, updated source_list)
        """
        # Create a new instance of the target class
        new_obj = target_class(name=None, health=None, strength=None, intellect=None, location=None)

        # Copy over the stats from the original object
        new_obj.set_health(obj.get_health())
        new_obj.set_strength(obj.get_strength())
        new_obj.set_intellect(obj.get_intellect())
        new_obj.set_location(obj.get_location()[0], obj.get_location()[1])

        # Add the new object to the target list
        target_list.append(new_obj)

        # Remove the original object from the source list
        if obj in source_list:
            source_list.remove(obj)

        return target_list, source_list

    def get_location(self):
        return self.location

    def get_health(self):
        return self.health

    def get_strength(self):
        return self.strength

    def get_intellect(self):
        return self.intellect

    def set_location(self, x, y):
        self.location[0] = x
        self.location[1] = y

    def set_health(self, number):
        self.health = number

    def set_strength(self, number):
        self.strength = number

    def set_intellect(self, number):
        self.intellect = number

    def randomAction(self):
        pass