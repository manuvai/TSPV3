from math import sqrtn

class Ville:
  """
  Ville class.
  """
  def __init__(self, nom, tabCords):
    self.nom = nom
    self.x = float(tabCords[0])
    self.y = float(tabCords[1])

  def __str__(self):
    res = "City {} => x={}, y={}".format(self.nom, self.x, self.y)
    return res

  def distanceBetween(villeA, villeB):
    x1, x2 = villeA.x, villeB.x
    y1, y2 = villeA.y, villeB.y

    res = sqrt(((float(x1) - float(x2)) ** 2) + ((float(y1) - float(y2)) ** 2))

    return res
