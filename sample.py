import requests
from bs4 import BeautifulSoup

target_url = 'https://note.mu/daikawai/n/nc73889d6d835'
r = requests.get(target_url)         #requestsを使って、webから取得
soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

for hoge in soup.find_all("img"):
    print(hoge)

#for a in soup.find_all('a'):
      #print(a.get('href'))         #リンクを表示
