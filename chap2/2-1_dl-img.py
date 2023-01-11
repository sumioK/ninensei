import requests

image_url = 'https://www.ymori.com/books/python2nen/sample1.png'
imagedata = requests.get(image_url)

filename = image_url.split('/')[-1]

with open(filename, 'wb') as f:
  f.write(imagedata.content)