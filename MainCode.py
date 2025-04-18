from Susceptible import Susceptible
from Mutated import Mutated


def susceptibleList(s):
    sList = []
    for i in range(s):
        susceptible = Susceptible("", 0, 0, 0,[0,0])
        sList.append(susceptible)
    return sList

def mutateList(m):
    mList = []
    for i in range(m):
        mutated = Mutated("", 0, 0, 0,[0,0])
        mList.append(mutated)
    return mList

def simulation(s, i, r, m):
    listS = susceptibleList(s)
    listM = mutateList(m)