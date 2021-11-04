import requests
from bs4 import BeautifulSoup

def main():
    url = "https://logs.eolem.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [a['href'] for a in soup.find_all('a') if a['href'][0]!="?"]

    for a in all_a:
        print(a)
if __name__ == '__main__':
    main()
