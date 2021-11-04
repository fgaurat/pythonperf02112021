from Rectangle import Rectangle


def main():
    r2 = Rectangle.from_string("5,6")
    print(r2)
def main_2():
    r = Rectangle(2,3)
    r1 = Rectangle(2,3)
   
    # r.longueur = 12
    a = r.longueur


    print(r.longueur)
    # assert r.longueur == 12
    print(r.surface)
    print(r1.surface)
    print("nb obj : Rectangle.cpt",Rectangle.get_cpt())
        
    s = str(r)
    print(s)
    print(int(r1))


    if r == r1:
        print("ok")
    else:
        print("ko")

if __name__ == '__main__':
    main()