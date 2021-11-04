from Carre import Carre
from ICalcGeo import ICalcGeo
from Rectangle import Rectangle
from Cercle import Cercle

def affiche_surface(o:ICalcGeo):
    print('affiche_surface')
    print(o.surface)

def main():
    r = Rectangle(4,6)
    r1 = Rectangle(4,6)
    print(id(r))
    print(id(r1))
    c = Carre(12)
    ce = Cercle(2)
    # print(ce.surface)
    # affiche_surface(ce)
    # print(c)
    # print(c.surface)
    # c.cote = 2
    # print(c.surface)
    
    # affiche_surface(r)
    # affiche_surface(c)
    # affiche_surface("toto")

    print(type(r))
    
    Rectangle2 = type("Rectangle2",(),{"longueur":0,"largeur":0})
    r2 = Rectangle2()
    if isinstance(r2,Rectangle2):
        print("ok")
    else:
        print("ko")


    print(r2.longueur)
    print(r2.largeur)
if __name__ == '__main__':
    main()
