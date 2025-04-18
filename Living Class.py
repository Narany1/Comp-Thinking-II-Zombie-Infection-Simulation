import random


class living:

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