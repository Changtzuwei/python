import requests
from bs4 import BeautifulSoup
url = 'https://www.mkc.edu.tw/Home?Sn=EV6S9OxI5fUiItcBOR6%2fsn0j5rmStDGs&%E8%A1%8C%E6%94%BF%E5%96%AE%E4%BD%8D'
res = requests.get(url)
html = BeautifulSoup(res.text)
data = html.find('a',{'class':'logo'})
data = data.find('img')
print(data)
print(url + data.get('src'))
res = requests.get(url + data.get('src'))
file = open(r'馬偕護專校徽.txt','w',encoding='utf-8')
file.write(res.text)
file.close()