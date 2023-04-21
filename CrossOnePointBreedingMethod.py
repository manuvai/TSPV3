from random import randint
from AbstractBreedingMethod import AbstractBreedingMethod
from Agent import Agent


class CrossOnePointBreedingMethod(AbstractBreedingMethod):
    @classmethod
    def breed(cls, parent1: Agent, parent2: Agent) -> list:
        index = randint(1, len(parent1.villes) - 1)

        childPath1, childPath2 = [], []

        for i in range(index):
            childPath1.append(parent1.villes[i])
            childPath2.append(parent2.villes[i])

        for i in range(len(parent1.villes)):
            if (not parent1.villes[i] in childPath2):
                childPath2.append(parent1.villes[i])

            if (not parent2.villes[i] in childPath1):
                childPath1.append(parent2.villes[i])

        return Agent(childPath1), Agent(childPath2)
    

if __name__ == '__main__':
    path = CrossOnePointBreedingMethod.breed(Agent([0, 1, 2, 3]), Agent([3, 2, 0, 1]))

    print(path)
