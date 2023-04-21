from random import randint

from Agent import Agent
from AgentGenerator import AgentGenerator
class Population:
    NB_AGENTS = 10000
    
    def __init__(self, liste_villes: list) -> None:
        self.villes = liste_villes
        self.agents = []

    def populate(villes: list, nb: int = NB_AGENTS) -> list:
        """Generates random agents

        Args:
            nb      (int): Le nombre de population
            villes  (list): La liste des villes
        """
        
        agents = []
        
        for i in range(nb):
            agent = AgentGenerator.generate(villes)
            agents.append(agent)
            
        return agents
    
    def evolve(self):
        self.selection()
        self.breed()
        self.mutate()
            
    def selection(self):
        pass

    def breed(self):
        pass

    def mutate(self):
        pass

