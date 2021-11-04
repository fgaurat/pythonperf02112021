from Rectangle import Rectangle



class Carre(Rectangle):

    def __init__(self,cote=0) -> None:
        """
        init Carre :
        - cote
        """
        super().__init__(longueur=cote, largeur=cote)
        print("def __init__(self,cote=0)")
        self._cote = cote

    @property
    def cote(self):
        return self._cote

    @cote.setter
    def cote(self,cote):
        self.longueur = cote
        self.largeur= cote
        self._cote = cote
    
    def __str__(self):
        #return f"{__name__}.{__class__.__name__}, {self.longueur=} {self.largeur=}"
        return f"{__class__.__name__} {self._cote=}"


