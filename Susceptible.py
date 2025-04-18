from Living import living
import random
class Susceptible(living):
    def __init__(self, name, health, strength, intellect, location):
        super().__init__(name, health, strength, intellect, location)

    def navigate(self):
        self.location[0] += random.randint(-5, 6)+6
        self.location[1] += random.randint(-5, 6)+6
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