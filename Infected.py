
from Living import living
import random

class Infected(living):

    def __init__(self, strength, intellect, health, name, location):
        super().__init__(name, health, strength, intellect, location)
        self.strength = random.randint(150, 175)
        self.intellect = 0
        self.health = random.randint(150, 175)

    def hunt(self, targets):
        nearest = None
        min_distance = float('inf')
        for target in targets:
            if isinstance(target, Infected):
                continue
            dist = ((target.location[0] - self.location[0]) ** 2 +
                    (target.location[1] - self.location[1]) ** 2) ** 0.5
            if dist < min_distance:
                min_distance = dist
                nearest = target

        if nearest:
            dx = 1 if nearest.location[0] > self.location[0] else -1
            dy = 1 if nearest.location[1] > self.location[1] else -1
            self.location[0] += dx * random.randint(1, 3)
            self.location[1] += dy * random.randint(1, 3)
            self.check_in_bounds()