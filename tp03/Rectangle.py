
from ICalcGeo import ICalcGeo


class Rectangle:
    """
    La classe Rectangle
    """
    _cpt = 0

    def __init__(self,longueur=0,largeur=0) -> None:
        """
            init Rectangle
                - longueur
                - largeur
        """
        print("def __init__(self,longueur,largeur)")
        self._longueur = longueur
        self._largeur = largeur
        Rectangle._cpt+=1
    

    @property
    def longueur(self):
        return self._longueur

    @property
    def largeur(self):
        return self._largeur
    
    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur

    @largeur.setter
    def largeur(self,largeur):
        self._largeur = largeur
    
    @property
    def surface(self):
        return self._largeur * self._longueur
    
    @staticmethod
    def get_cpt():
        return Rectangle._cpt

    
    @classmethod
    def from_string(cls,value):
        l = [int(i) for i in value.split(",")]

        return cls(*l)

    def __int__(self):
        return self._largeur*self._longueur

    def __str__(self):

        return f"{__name__}.{__class__.__name__}, {self._longueur=} {self._largeur=}"

    def __eq__(self, o: object) -> bool:
        result = True if self._longueur == o._longueur and self._largeur == o._largeur else False 
        return result


