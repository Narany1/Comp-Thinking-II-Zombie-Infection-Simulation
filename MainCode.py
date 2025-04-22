from Susceptible import Susceptible
from Mutated import Mutated
from Infected import Infected


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

def infectedList(i):
    iList = []
    for i in range(i):
        infected = Infected("", 0, 0, 0,[0,0])
        iList.append(infected)
    return iList

def removeList(r):
    pass


def simulation(s, i, r, m):
    listS = susceptibleList(s)
    listM = mutateList(m)
    listI = infectedList(i)
    listR = []