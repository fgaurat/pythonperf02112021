
def make_incrementor(v):

    v*=2
    def the_function(i):
        return i+v
    return the_function



def do_log(the_func):
    def wrapper(n):
        print("before",n)
        s = the_func(n)
        print("after",s)
        return s

    return wrapper


@do_log
def say_hello(n):
    print("hello",n)
    return n.upper()

@do_log
def dire_bonjour(n):
    print("bonjour",n)

def main():
    # inc_from_12 = make_incrementor(2)
    # a = inc_from_12(1)
    # print(a) # 13
    
    say_hello("Fred")
    dire_bonjour("Fred")


if __name__ == '__main__':
    main()