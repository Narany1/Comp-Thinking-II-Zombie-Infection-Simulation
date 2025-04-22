from Living import Living
import random


class Mutated(Living):
    def scavenge(self):
        self.location[0] += random.randint(-5, 6) + 8
        self.location[1] += random.randint(-5, 6) + 8
        self.check_in_bounds()

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
        action = random.randint(0, 4)
        if action == 0:
            self.scavenge()
        elif action == 1 and infected_list:
            nearest = min(infected_list, key=lambda i: ((i.get_location()[0] - self.location[0]) ** 2 + (i.get_location()[1] - self.location[1]) ** 2) ** 0.5)
            dist = ((nearest.get_location()[0] - self.location[0]) ** 2 + (nearest.get_location()[1] - self.location[1]) ** 2) ** 0.5
            if dist <= 2:
                if self.fight(nearest):
                    infected_list.remove(nearest)
        elif action == 2:
            self.flee()
        elif action == 3:
            self.rest()
        elif action == 4:
            self.eat()