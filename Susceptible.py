from Living import Living
import random


class Susceptible(Living):
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
        action = random.randint(0, 4)
        if action == 0:
            self.navigate()
        elif action == 1:
            self.research()
        elif action == 2:
            for infected in infected_list:
                dx = abs(infected.get_location()[0] - self.location[0])
                dy = abs(infected.get_location()[1] - self.location[1])
                if dx <= 5 and dy <= 5:
                    self.flee()
                    return
            self.move()
        elif action == 3:
            self.rest()
        elif action == 4:
            self.eat()