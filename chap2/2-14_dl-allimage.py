import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

load_url = 'https://www.ymori.com/books/python2nen/test2.html'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

# 保存用ディレクトリの作成
out_folder = Path("downloads2")
out_folder.mkdir(exist_ok=True)

# すべてのimgタグを検索しリンクを取得
for element in soup.find_all('img'):
  src = element.get('src')

  # 絶対URLを作って画像データを取得する
  image_url = urllib.parse.urljoin(load_url, src)
  imgdata = requests.get(image_url)

  # URLから最後のファイル名を取り出して、保存フォルダとつなげる
  filename = image_url.split('/')[-1]
  out_path = out_folder.joinpath(filename)
  
  # 画像データをファイルに出力
  with open(out_path, mode='wb') as f:
    f.write(imgdata.content)

    # １秒停止
    time.sleep(1)
