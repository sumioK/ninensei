import requests
from bs4 import BeautifulSoup

load_url = 'https://piso-animals.com/posts/index'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

for element in soup.find_all('a'):
  print(element.text)