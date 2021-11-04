import hello
import traceback

class DivBy12Exception(Exception):
    """
    Erreur division par 12
    """
    def __init__(self) -> None:
        super().__init__("Erreur division par 12")

def div(a:int, b:int)->float:
    """
    Divise a par b
    """
    if b == 12:
        raise DivBy12Exception()
    return a/b


def call_div(a, b):
    """
    Call division
    """
    r = 0
    try:
        r = div(a, b)
    # except Exception as e:
    #     print("call_div", e)
    #     raise e
    finally:
        print("faire un truc")
    return r


def main():
    a = 2
    b = 12
    try:
        c = call_div(a, b)
        print(c)
    except Exception as e:
        print("main", e)
    else:
        print("le else")


def main_1():

    l = [0, 1, 2, 3, 4, 5]
    # l2 = []

    # # Méthode 1
    # for i in l:
    #     l2.append(i*2)

    # # Méthode 2
    # l2 = list(map(lambda i:i*2,l))
    # a=2

    # # Méthode 3
    # l2 = [mult2(i) for i in l if i%2 ==0]
    # print(l2)

    # l2 = [0,2,4,6,8,10]

    # found = True
    # for i in l:
    #     if i ==3:
    #         break
    #     elif i ==4:
    #         continue
    #     print(i)
    # else:

    #     found = False

    d = {}

    try:
        a = 2
        b = 0
        # c = a/b
    except IndexError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print("Exception", e)
        traceback.print_exc()

    finally:
        print("après", l)


if __name__ == '__main__':
    main()
