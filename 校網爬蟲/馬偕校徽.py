import requests
from bs4 import BeautifulSoup
url = 'https://www.mkc.edu.tw'
res = requests.get(url)
html = BeautifulSoup(res.text)
data = html.find('a',{'class':'logo'})
data = data.find('img')
print(data)
print(url + data.get('src'))
res = requests.get(url + data.get('src'))
file = open(r'馬偕護專校徽.png','wb')
file.write(res.content)
file.close()