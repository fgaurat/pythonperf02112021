def mult(**kw):
    r = 1
    for v in kw.values():
        r*=v
    return r

def add(*l):
    r = 0
    for i in l:
        r += i
    return r

def main():
    data = [1,2,34]
    t = tuple(data)
    s = {10,20,30,40}
    print(*s,sep="-")
    print(1,2,34,sep="-")
    add(*t)
    print("data",data)
    print("t",t)
    r = add(*data)
    print(r)

    r = mult(b=2,a=10)
    print(r)


if __name__ == '__main__':
    main()
