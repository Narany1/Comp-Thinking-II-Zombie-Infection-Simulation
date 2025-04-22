from Living import living
import random


class Susceptible(living):
    def __init__(self, name, health, strength, intellect, location):
        super().__init__(name, health, strength, intellect, location)

    def navigate(self):
        self.location[0] += random.randint(-5, 6)
        self.location[1] += random.randint(-5, 6)
        self.check_in_bounds()

    def research(self):
        self.intellect += 2

    def flee(self):
        self.location[0] += random.randint(-5, 6) - 8
        self.location[1] += random.randint(-5, 6) - 8
        self.check_in_bounds()

    def rest(self):
        self.health += 10

    def eat(self):
        self.health += 5
        self.strength += 10

    def randomAction(self, infected_list):
        randomNum = random.randint(0, 4)
        if randomNum == 0:
            self.navigate()
        elif randomNum == 1:
            self.research()
        elif randomNum == 2:
            # Check if there are infected nearby and flee
            for infected in infected_list:
                dx = abs(infected.get_location()[0] - self.location[0])
                dy = abs(infected.get_location()[1] - self.location[1])
                if dx <= 5 and dy <= 5:
                    self.flee()
                    return
            self.move()  # Just move normally if no infected nearby
        elif randomNum == 3:
            self.rest()
        elif randomNum == 4:
            self.eat()