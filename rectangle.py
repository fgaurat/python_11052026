

class Rectangle:


    def __init__(self,longueur,largeur):
        self._longueur = longueur
        self._largeur = largeur


    def surface(self):
        return self._longueur * self._largeur