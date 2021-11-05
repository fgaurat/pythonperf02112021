import multiprocessing
import time
from multiprocessing import Pool
import logging

from main import download_file
import requests
from bs4 import BeautifulSoup



logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(processName)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)

def f(x):
    logger.info(x)
    return x*x


def main():
    url = "https://logs.eolem.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [a['href'] for a in soup.find_all('a') if a['href'][0]!="?"]

    args = []
    for log_file in all_a:
        url_file = f"{url}/{log_file}"
        args.append((url_file,log_file))

    print(args)
    with Pool() as p:
        p.starmap(download_file, args)

    print()
    print("after loop")



def main_calc_proc():
    print(multiprocessing.cpu_count())
    r = []

    with Pool() as p:
        print(p)
        r = p.map(f, [*range(10)])

    print(r)
    time.sleep(2)
    r = map(f, [*range(10)])
    print(list(r))

if __name__ == '__main__':
    main()