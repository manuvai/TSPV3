from random import randint
from .AbstractBreedingMethod import AbstractBreedingMethod
from .Agent import Agent

class CrossTwoPointsBreedingMethod(AbstractBreedingMethod):
    @classmethod
    def breed(cls, parent1: Agent, parent2: Agent) -> list:
        pathLen = len(parent1.villes)
        index1 = randint(0, len(parent1.villes) - 1)
        index2 = randint(0, len(parent1.villes) - 1)
        
        childPath1, childPath2 = [], []

        for i in range(pathLen):
            childPath1.append(None)
            childPath2.append(None)
            
        for i in range(pathLen):
            crossingInTakingOut = index1 > index2 and (i > index1 or i < index2)
            crossingOutTakingIn = index1 < index2 and i > index1 and i < index2

            if (crossingInTakingOut or crossingOutTakingIn):
                childPath1[i] = parent1.villes[i]          
                childPath2[i] = parent2.villes[i]
        
        for i in range(pathLen):
            if not (parent2.villes[i] in childPath1):
                for j in range(pathLen):
                    if childPath1[j] is None:
                        childPath1[j] = parent2.villes[i]
                        break

            if not (parent1.villes[i] in childPath2):
                for j in range(pathLen):
                    if childPath2[j] is None:
                        childPath2[j] = parent1.villes[i]
                        break

        return Agent(childPath1), Agent(childPath2)

if __name__ == '__main__':
    path = CrossTwoPointsBreedingMethod.breed(Agent([0, 1, 2, 3]), Agent([3, 2, 0, 1]))

    print(path)