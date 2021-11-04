import sys
from monmodule import *


def main():
    
    a=2
    
    
    
    

    # print("start main",a)
    # print("start monmodule",a)
    a = 2
    print(sys.getrefcount(a))
    b = 2


    def in_main():
        nonlocal b
        print('in_main',b)
        b = 1000

    in_main()
    print(b)

    print(sys.getrefcount(a))
    c = 2
    print(sys.getrefcount(a))
    # print(hex(id(a)))
    # print(hex(id(b)))
    # print(sys.getrefcount(b))
    # s = 'toto'
    # print(sys.getrefcount(s))
    # a = 3
    # print(hex(id(a)))

    l = [1, 2, 3]
    print(hex(id(l)))
    l.append(4)
    print(hex(id(l)))


if __name__ == '__main__':
    print("before main", a)
    main()
    print("after main", a)
