import requests
from bs4 import BeautifulSoup

def main():
    url = "https://logs.eolem.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [a['href'] for a in soup.find_all('a') if a['href'][0]!="?"]

    for log_file in all_a:
        url_file = f"{url}/{log_file}"
        resp = requests.get(url_file)
        with open(log_file,'w') as f:
            f.write(resp.text)



if __name__ == '__main__':
    main()
