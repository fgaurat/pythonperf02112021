import time
import threading


def long_traitement_1():
    for i in range(1000):
        # print("long_traitement_1",i)
        time.sleep(0.3)

def long_traitement_2():
    for i in range(1000):
        # print("long_traitement_2",i)
        time.sleep(0.3)

def main():
    
    th1 = threading.Thread(target=long_traitement_1)
    th2 = threading.Thread(target=long_traitement_2)
    th1.start()
    th2.start()

    # th1.join()
    # th2.join()



if __name__ == '__main__':
    main()