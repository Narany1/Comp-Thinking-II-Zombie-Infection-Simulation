from Susceptible import Susceptible
from Mutated import Mutated
from Infected import Infected
import random


def susceptibleList(s):
    sList = []
    for i in range(s):
        susceptible = Susceptible("Human" + str(i), None, None, None, [random.randint(0, 100), random.randint(0, 100)])
        sList.append(susceptible)
    return sList


def mutateList(m):
    mList = []
    for i in range(m):
        mutated = Mutated("Mutant" + str(i), None, None, None, [random.randint(0, 100), random.randint(0, 100)])
        mList.append(mutated)
    return mList


def infectedList(i):
    iList = []
    for i in range(i):
        infected = Infected("Zombie" + str(i), None, None, None, [random.randint(0, 100), random.randint(0, 100)])
        iList.append(infected)
    return iList


def simulation(s, i, m):
    listS = susceptibleList(s)
    listM = mutateList(m)
    listI = infectedList(i)
    listR = []  # Removed/Dead

    hours = 0
    max_hours = 1000  # To prevent infinite loops

    print(f"Starting simulation with {len(listS)} Susceptible, {len(listI)} Infected, and {len(listM)} Mutated")

    while len(listS) > 0:
        hours += 1

        # Process Susceptible individuals
        for s in list(listS):  # Use a copy to avoid modification during iteration
            s.randomAction(listI)

            # Check for encounters with infected
            for infected in list(listI):
                dx = abs(infected.get_location()[0] - s.get_location()[0])
                dy = abs(infected.get_location()[1] - s.get_location()[1])

                if dx <= 2 and dy <= 2:
                    # Encounter!
                    if random.randint(0, 100) < 10:  # 10% chance of successful fight
                        if s.fight(infected):
                            listR.append(infected)
                            listI.remove(infected)
                    else:
                        # Getting infected
                        if random.randint(0, 100) < 95:  # 95% chance of infection
                            new_infected = Infected("Infected", None, None, None,
                                                    [s.get_location()[0], s.get_location()[1]])
                            listI.append(new_infected)
                        else:  # 5% chance of mutation
                            new_mutated = Mutated("Mutated", None, None, None,
                                                  [s.get_location()[0], s.get_location()[1]])
                            listM.append(new_mutated)

                        # Either way, remove from susceptible
                        listS.remove(s)
                        break

        # Process Infected individuals
        for infected in list(listI):
            infected.randomAction(listS)

        # Process Mutated individuals
        for mutated in list(listM):
            mutated.randomAction(listI)

            # Check for encounters with infected
            for infected in list(listI):
                dx = abs(infected.get_location()[0] - mutated.get_location()[0])
                dy = abs(infected.get_location()[1] - mutated.get_location()[1])

                if dx <= 2 and dy <= 2:
                    # Battle!
                    if random.randint(0, 100) < 60:  # Mutants have better odds (60%)
                        if mutated.fight(infected):
                            listR.append(infected)
                            listI.remove(infected)

        # Every 24 hours, print status
        if hours % 24 == 0:
            print(
                f"Day {hours // 24}: {len(listS)} Susceptible, {len(listI)} Infected, {len(listM)} Mutated, {len(listR)} Removed")

    result = f"Simulation ended after {hours} hours.\n"
    result += f"Susceptible: {len(listS)}\n"
    result += f"Infected: {len(listI)}\n"
    result += f"Mutated: {len(listM)}\n"
    result += f"Removed: {len(listR)}"

    return result


if __name__ == "__main__":
    # Run simulation with 50 susceptible, 1 infected, 0 mutated initially
    result = simulation(100, 1, 0)
    print(result)