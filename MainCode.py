from Susceptible import Susceptible
from Mutated import Mutated
from Infected import Infected
import matplotlib.pyplot as plt
import random


def create_population(cls, count, name_prefix):
    return [cls(f"{name_prefix}{i}", None, None, None, [random.randint(0, 100), random.randint(0, 100)]) for i in range(count)]

def simulation(s, i, m):
    listS = create_population(Susceptible, s, "Human")
    listM = create_population(Mutated, m, "Mutant")
    listI = create_population(Infected, i, "Zombie")
    listR = []
    hours = 0
    susceptible_counts = []
    infected_counts = []
    mutated_counts = []
    removed_counts = []
    time_steps = []


    print(f"Starting simulation with {len(listS)} Susceptible, {len(listI)} Infected, {len(listM)} Mutated")

    while listS and hours < 1000:
        hours += 1

        for s in list(listS):
            s.randomAction(listI)
            for infected in list(listI):
                dx = abs(infected.get_location()[0] - s.get_location()[0])
                dy = abs(infected.get_location()[1] - s.get_location()[1])
                if dx <= 2 and dy <= 2:
                    if random.randint(0, 100) < 10 and s.fight(infected):
                        listI.remove(infected)
                        listR.append(infected)
                    else:
                        if random.randint(0, 100) < 95:
                            listI.append(Infected("Infected", None, None, None, s.get_location().copy()))
                        else:
                            listM.append(Mutated("Mutated", None, None, None, s.get_location().copy()))
                        listS.remove(s)
                        break

        for infected in list(listI):
            infected.randomAction(listS)

        for mutated in list(listM):
            mutated.randomAction(listI)

        susceptible_counts.append(len(listS))
        infected_counts.append(len(listI))
        mutated_counts.append(len(listM))
        removed_counts.append(len(listR))
        time_steps.append(hours)

        if hours % 24 == 0:
            print(f"Day {hours // 24}: {len(listS)} Susceptible, {len(listI)} Infected, {len(listM)} Mutated, {len(listR)} Removed")
    plt.figure(figsize=(10, 6))
    plt.plot(time_steps, susceptible_counts, label="Susceptible", color="blue")
    plt.plot(time_steps, infected_counts, label="Infected", color="red")
    plt.plot(time_steps, mutated_counts, label="Mutated", color="green")
    plt.plot(time_steps, removed_counts, label="Removed", color="gray")
    plt.xlabel("Time (Hours)")
    plt.ylabel("Population Count")
    plt.title("Virus Spread Simulation Over Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return f"Simulation ended after {hours} hours.\nSusceptible: {len(listS)}\nInfected: {len(listI)}\nMutated: {len(listM)}\nRemoved: {len(listR)}"


if __name__ == "__main__":
    # Run simulation with 50 susceptible, 1 infected, 0 mutated initially
    result = simulation(100, 1, 0)
    print(result)