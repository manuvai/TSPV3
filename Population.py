from random import randint

from Agent import Agent
class Population:
    def __init__(self, liste_villes: list) -> None:
        self.villes = liste_villes
        self.agents = []

    def populate(villes: list, nb: int) -> list:
        """Generates random agents

        Args:
            nb      (int): Le nombre de population
            villes  (list): La liste des villes
        """
        def __generate_agent(villes: list):
            path = []
            temp_villes = villes

            while len(temp_villes) > 0:
                index = randint(0, len(temp_villes) - 1)
                path.append(temp_villes.pop(index))

            return Agent(path)
        
        agents = []
        
        for i in range(nb):
            agents.append( \
                    __generate_agent(villes) \
                )
            
        return agents
            
    def selection(self):
        pass

    def breed(self):
        pass

    def mutate(self):
        pass

