from collections import deque
import collections
import copy
def gen_mult2(nums):# [0...9]
    for j in nums:
        print("gen_mult2 ",j)
        yield j*2

def gen_integer(a):
    for i in gen_mult2(range(a)):
        print("gen_integer ",a,i)
        yield i

def main():
    l = [
        [0,1],
        [2,3],
        [4,5],
    ]
    # d = deque(l)
    # d.appendleft(12)
    # list
    # for i in d:
    #     print(i)

    # s = l[:]
    s = copy.deepcopy(l)
    print(l)
    print(s)
    l[0][0] = 1000
    print(l)
    print(s)

    a = {"key1":"value1","key2":"value2","key3":"value3"}
    b = {"key4":"value4","key1":"value5"}
    
    c = collections.ChainMap(b,a)
    print(c['key1'])

    for value in gen_integer(5):
        print(value)




if __name__ == '__main__':
    main()