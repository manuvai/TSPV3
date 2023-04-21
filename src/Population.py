from random import randint, random

from .Agent import Agent
from .AgentGenerator import AgentGenerator
from .CrossOnePointBreedingMethod import CrossOnePointBreedingMethod
from .CrossTwoPointsBreedingMethod import CrossTwoPointsBreedingMethod
from .SwapMutatorMethod import SwapMutatorMethod


class Population:
    NB_AGENTS = 200
    p_selection = 0.5
    p_breed = 0.3
    p_mutate = 0.32

    # TODO Ajouter un générateur d'agent avec ajout des villes de façon "plus intuitive"
    # TODO Ajouter une nouvelle méthode de mutation
    # TODO Permettre de calculer la matrice de distance en amont
    def __init__(self, liste_villes: list) -> None:
        self.villes = liste_villes
        self.agents = []

    def get_best_path(self):
        self.sort()

        return self.agents[0]
    
    def get_worst_path(self):
        self.sort()

        return self.agents[-1]

    @classmethod
    def populate(cls, villes: list, nb: int = NB_AGENTS) -> list:
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
        self.sort()
        self.selection()
        self.breed()
        self.repopulate()
        self.mutate()

    def repopulate(self):
        agents_left = __class__.NB_AGENTS - len(self.agents)
        self.agents += __class__.populate(self.villes, agents_left)

    def sort(self):
        self.agents = sorted(self.agents, reverse=False, key=lambda a: a.distance())

    def selection(self):
        indexTronc = int(len(self.agents) * __class__.p_selection)
        self.agents = self.agents[:indexTronc]

    def breed(self):
        def __pick_parents(agents):
            
            index1 = randint(0, len(agents) - 1)
            index2 = randint(0, len(agents) - 1)

            return agents[index1], agents[index2]

        def __generate_childs(agents):
            parents = __pick_parents(agents)
            if (random() < 0.5):
                child1, child2 = CrossOnePointBreedingMethod.breed(parents[0], parents[1])
            else:
                child1, child2 = CrossTwoPointsBreedingMethod.breed(parents[0], parents[1])

            return child1, child2

        tempAgents = []
        nb_wanted = int((__class__.p_selection + __class__.p_breed) * __class__.NB_AGENTS)
        
        for i in range(len(self.agents), nb_wanted, 2):
            ag1, ag2 = __generate_childs(self.agents)

            tempAgents.append(ag1)
            tempAgents.append(ag2)

        if i < nb_wanted:
            ag1, temp = __generate_childs(self.agents)
            tempAgents.append(ag1)

        self.agents += tempAgents

    def mutate(self):

        nb_agents = len(self.agents)
        for i in range(1, nb_agents):
            agent = self.agents[i]

            if (random() > __class__.p_mutate):
                agent = SwapMutatorMethod.mutate(agent)
            self.agents[i] = agent
