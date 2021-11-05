import numpy as np



def main():
    a = np.array([0.1,2.2,5.3,9.4],dtype=np.int16)
    a = np.array([[0,1],[2,3],[4,5]],dtype=np.int16)
    b = a*2
    print(b)
    print(a.shape)


if __name__ == '__main__':
    main()