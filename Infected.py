from Living import living
import random

class Infected(living):
    def __init__(self, name, health, strength, intellect, location):
        super().__init__(name, health, strength, intellect, location)
        self.strength = random.randint(150, 175)
        self.intellect = 0
        self.health = random.randint(150, 175)

    def hunt(self, target, targets_list):
        # Move towards the target
        dx = 1 if target.get_location()[0] > self.location[0] else -1
        dy = 1 if target.get_location()[1] > self.location[1] else -1
        self.location[0] += dx * random.randint(1, 3)
        self.location[1] += dy * random.randint(1, 3)
        self.check_in_bounds()

    def randomAction(self, susceptible_list):
        randomNum = random.randint(0, 2)
        if randomNum == 0:
            self.move()
        elif randomNum == 1:
            # Find the nearest susceptible
            if susceptible_list:
                nearest = susceptible_list[0]
                min_distance = float('inf')
                for target in susceptible_list:
                    dist = ((target.get_location()[0] - self.location[0]) ** 2 +
                            (target.get_location()[1] - self.location[1]) ** 2) ** 0.5
                    if dist < min_distance:
                        min_distance = dist
                        nearest = target
                self.hunt(nearest, susceptible_list)
        elif randomNum == 2:
            # Just wait/rest
            pass