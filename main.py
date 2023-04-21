import sys
import signal

from matplotlib import pyplot as plt

from src.FileAdapter import FileAdapter
from src.Population import Population

# FILE = csvTSP250
NB_POPULATION = 200
NB_ITERATION = 1000
MAX_ITERATION = NB_ITERATION
DIFF_MAX = 4
FULL_DEBUG = True and False
RUNNING = True


def getFormatedTime(t):
    d = int(t / (3600 * 24))
    res = t % (3600 * 24)
    h = int(res / 3600)
    res = res % 3600
    m = int(res / 60)
    res = res % 60

    response = ""
    if d:
        response += "{} d".format(d)
    if h:
        if response != "":
            response += ", "
        response += "{} h".format(h)
    if m:
        if response != "":
            response += ", "
        response += "{} m".format(m)
    if res:
        if response != "":
            response += ", "
        response += "{:.2f} s".format(res)

    return response


def stopRun(signal, frame):
    """
    Signal handler to stop infinite loop.
    @param    signal    The signal caucht.
    @param    frame     The frame.
    """
    global RUNNING
    RUNNING = False
    # exit(0)



class PopulationDrawer:
    def __init__(self, population):
        self.population = population

    def drawGraph(self):
        x, y = [], []
        for ville in self.population.villes:
            x.append(ville.x)
            y.append(ville.y)

        plt.plot(x, y, "o")
        plt.title("Villes")

        x, y = [], []
        for v in self.population.get_best_path().villes:
            x.append(v.x)
            y.append(v.y)

        plt.scatter(x, y, c="red")

        # x.append(
        #     self.population.villes[self.population.get_best_path().villes[0]].x)
        # y.append(
        #     self.population.villes[self.population.get_best_path().villes[0]].y)

        plt.plot(x, y)
        plt.show()

        pass

def debug(population: Population):
    best = population.get_best_path()
    worst = population.get_worst_path()
    print("Best distance : {} - worst : {}".format(best.distance(), worst.distance()))

ITERATIONS = 1000

if __name__ == '__main__':
    file_adapter = FileAdapter('data/TSP250.csv')
    lines = file_adapter.get_lines()

    liste_villes = file_adapter.get_villes(lines)

    population = Population(liste_villes)

    population.repopulate()
    drawer = PopulationDrawer(population)

    # drawer.drawGraph()
    debug(population)

    i = 0

    while (i < ITERATIONS):
        population.evolve()
        debug(population)


        i += 1
    # drawer.drawGraph()
    debug(population)

