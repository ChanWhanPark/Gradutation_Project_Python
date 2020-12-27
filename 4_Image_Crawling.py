from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
import os

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('keyword : ')
crawl_num = int(input('number of picture(maximum 50): '))

url = baseUrl + quote_plus(plusUrl)
html = urlopen(url)
soup = bs(html, "html.parser")
img = soup.find_all(class_ = '_img')

dir_path = './img'
dir_name = plusUrl
os.mkdir(dir_path + '/' + dir_name + '/')
path = dir_path + '/' + dir_name + '/'

n = 1
for i in img:
    print(n)
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open(path + plusUrl + str(n)+'.jpg','wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    if n > crawl_num:
        break

print('Image Crawling is done.')
