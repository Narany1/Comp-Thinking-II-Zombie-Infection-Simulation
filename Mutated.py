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
        return super().fight(foe)

    def flee(self):
        self.location[0] += random.randint(-5, 6) - 10
        self.location[1] += random.randint(-5, 6) - 10
        self.check_in_bounds()

    def rest(self):
        self.health += 10

    def eat(self):
        self.health += 5
        self.strength += 10

    def randomAction(self, infected_list):
        randomNum = random.randint(0, 4)
        if randomNum == 0:
            self.scavenge()
        elif randomNum == 1:
            if infected_list:
                # Find nearest infected to fight
                nearest = None
                min_distance = float('inf')
                for infected in infected_list:
                    dist = ((infected.get_location()[0] - self.location[0]) ** 2 +
                            (infected.get_location()[1] - self.location[1]) ** 2) ** 0.5
                    if dist < min_distance:
                        min_distance = dist
                        nearest = infected

                if nearest and min_distance <= 2:
                    self.fight(nearest)
        elif randomNum == 2:
            self.flee()
        elif randomNum == 3:
            self.rest()
        elif randomNum == 4:
            self.eat()