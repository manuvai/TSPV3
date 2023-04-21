from Agent import Agent

class AbstractBreedingMethod:

    @classmethod
    def breed(cls, parent1: Agent, parent2: Agent) -> list:
        pass