from Living import living
import random

class Mutated(living):
    def __init__(self, name, health, strength, intellect, location):
        super().__init__(name, health, strength, intellect, location)

    def scavenge(self):
        self.location[0] += random.randint(-5, 6) + 8
        self.location[1] += random.randint(-5, 6) + 8
        self.check_in_bounds()

    def fight(self, foe):
        foe_stats = foe.strength + foe.health + foe.intellect
        current_stats = self.strength + self.health + self.intellect + 10
        win_rate = 60
        win_rate += current_stats - foe_stats

    def flee(self):
        self.location[0] += random.randint(-5, 6) - 10
        self.location[1] += random.randint(-5, 6) - 10
        self.check_in_bounds()

    def rest(self):
        self.health += 10

    def eat(self):
        self.health += 5
        self.strength += 10