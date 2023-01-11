import requests
from pathlib import Path

out_folder = Path('Media')
image_url = 'https://www.ymori.com/books/python2nen/sample1.png'
image_data = requests.get(image_url)

filename = image_url.split('/')[-1]
out_path = out_folder.joinpath(filename)

with open(out_path, mode='wb') as f :
  f.write(image_data.content)