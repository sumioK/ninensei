import requests
from bs4 import BeautifulSoup
import urllib

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

for element in soup.find_all('img'):
  # ここで定義するsrcはimgタグのsrc=以降
  src = element.get('src')

# urljoinは基底URLと別のURLを結合して絶対URLを作る
  image_url = urllib.parse.urljoin(load_url, src)
  filename = image_url.split('/')[-1]
  print(image_url, '>>', filename)
