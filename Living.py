import random


import random

class Living:
    def __init__(self, name, health=None, strength=None, intellect=None, location=None):
        self.name = name
        self.health = health if health is not None else random.randint(50, 101)
        self.strength = strength if strength is not None else random.randint(50, 101)
        self.intellect = intellect if intellect is not None else random.randint(50, 101)
        self.location = location if location else [0, 0]

    def check_in_bounds(self):
        self.location[0] = max(0, min(100, self.location[0]))
        self.location[1] = max(0, min(100, self.location[1]))

    def move(self):
        self.location[0] += random.randint(-5, 6)
        self.location[1] += random.randint(-5, 6)
        self.check_in_bounds()

    def fight(self, foe):
        foe_stats = foe.strength + foe.health + foe.intellect
        current_stats = self.strength + self.health + self.intellect + 10
        win_rate = max(5, min(95, 50 + current_stats - foe_stats))
        return random.randint(1, 101) <= win_rate

    def get_location(self):
        return self.location

    def get_health(self):
        return self.health

    def get_strength(self):
        return self.strength

    def get_intellect(self):
        return self.intellect

    def set_location(self, x, y):
        self.location = [x, y]

    def set_health(self, number):
        self.health = number

    def set_strength(self, number):
        self.strength = number

    def set_intellect(self, number):
        self.intellect = number