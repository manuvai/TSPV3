from random import randint, shuffle
from .Agent import Agent

class AgentGenerator:

    @classmethod
    def generate(cls, villes: list) -> Agent:
        
        path = [v for v in villes]
        shuffle(path)
        ag = Agent(path)
        return Agent(path)