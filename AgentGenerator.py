from random import randint
from Agent import Agent

class AgentGenerator:

    @classmethod
    def generate(cls, villes: list) -> Agent:
        
        path = []
        temp_villes = villes

        while len(temp_villes) > 0:
            index = randint(0, len(temp_villes) - 1)
            path.append(temp_villes.pop(index))

        return Agent(path)