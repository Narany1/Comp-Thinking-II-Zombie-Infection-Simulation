from Living import Living
import random

class Infected(Living):
    def __init__(self, name, health=None, strength=None, intellect=None, location=None):
        super().__init__(name, health, strength, intellect, location)
        self.strength = random.randint(150, 175)
        self.intellect = 0
        self.health = random.randint(150, 175)

    def hunt(self, target):
        dx = target.get_location()[0] - self.location[0]
        dy = target.get_location()[1] - self.location[1]
        if dx != 0:
            self.location[0] += int(dx / abs(dx)) * random.randint(1, 3)
        if dy != 0:
            self.location[1] += int(dy / abs(dy)) * random.randint(1, 3)
        self.check_in_bounds()

    def randomAction(self, susceptible_list):
        action = random.randint(0, 2)
        if action == 0:
            self.move()
        elif action == 1 and susceptible_list:
            nearest = min(susceptible_list, key=lambda s: ((s.get_location()[0] - self.location[0]) ** 2 + (s.get_location()[1] - self.location[1]) ** 2) ** 0.5)
            self.hunt(nearest)