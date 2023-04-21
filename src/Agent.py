from .Ville import Ville


class Agent:
    def __init__(self, villes: list = []) -> None:
        self.villes = villes

    def distance(self) -> float:
        res = 0
        for i in range(len(self.villes)):
            ville1 = self.villes[i - 1]
            ville2 = self.villes[i]

            res += Ville.distanceBetween(ville1, ville2)

        return res
    
    def __str__(self) -> str:
        temp = [v.__str__() for v in self.villes]

        return "-".join(temp)
