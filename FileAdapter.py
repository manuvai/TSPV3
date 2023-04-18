from Ville import Ville


class FileAdapter:
    def __init__(self, path: str) -> None:
        self.path = path

    def get_lines(self) -> list:
        """Retourne la liste des lignes de coordonnées contenues dans le fichier

        Returns:
            list: La liste de coordonnées
        """
        lines = []

        with open(self.path) as f:
            for line in f:
                x, y = line.split()
                lines.append((x, y))
        
        return lines
    
    def get_villes(self, lines: list) -> list:
        """Retourne la liste de villes à partir d'une liste de coordonnées

        Args:
            lines (list): La liste de coordonnées

        Returns:
            list: La liste de villes
        """
        return [Ville(i, lines[i]) for i in range(len(lines))]

if __name__ == '__main__':
    file_adapter = FileAdapter('data/TSP25.csv')
    lines = file_adapter.get_lines()
    print(lines)

    liste_villes = file_adapter.get_villes(lines)
    print(liste_villes)
