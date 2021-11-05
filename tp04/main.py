import requests
from bs4 import BeautifulSoup
import threading

class DownloadThread(threading.Thread):


    def __init__(self,url_file,log_file):
        super().__init__(group=None)
        self._url_file = url_file
        self._log_file = log_file

    def run(self):
        resp = requests.get(self._url_file)
        with open(self._log_file,'w') as f:
            f.write(resp.text)



def download_file(url_file,log_file):
    print(threading.current_thread().name)
    print(threading.get_ident())
    resp = requests.get(url_file)
    with open(log_file,'w') as f:
        f.write(resp.text)


def main():
    url = "https://logs.eolem.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [a['href'] for a in soup.find_all('a') if a['href'][0]!="?"]

    for log_file in all_a:
        url_file = f"{url}/{log_file}"
        #th = threading.Thread(target=download_file,args=[url_file,log_file],name=f"th_{log_file}")
        th = DownloadThread(url_file,log_file)
        th.start()
        # download_file(url_file,log_file)

    print("after loop")

if __name__ == '__main__':
    main()
