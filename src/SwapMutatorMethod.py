from .Agent import Agent
from random import randint

class SwapMutatorMethod:
    
    @classmethod
    def mutate(cls, agent: Agent) -> Agent:
        index1 = randint(0, len(agent.villes) - 1)
        index2 = randint(0, len(agent.villes) - 1)

        agent.villes[index1], agent.villes[index2] = agent.villes[index2], agent.villes[index1]

        return agent
