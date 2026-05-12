from rectangle import Rectangle



class Carre(Rectangle): # Carre hérite de Rectangle

    def __init__(self, cote):
        super().__init__(cote, cote)
        self._cote = cote

    
    def get_cote(self): # Accesseur pour l'attribut cote
        return self._cote
    
    def set_cote(self, cote): # Mutateur pour l'attribut cote
        if cote > 0:
            self._cote = cote
            self.longueur = cote
            self.largeur = cote
        else:
            raise ValueError("Le côté doit être positif")