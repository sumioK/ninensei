import requests
from bs4 import BeautifulSoup
import urllib

load_url = 'https://piso-animals.com/posts/index'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

for element in soup.find_all('a'):
  print(element.text)
  url = element.get('href')
  link_url = urllib.parse.urljoin(load_url, url)
  print(link_url)
