#<a></a>:超連結
import requests
from bs4 import BeautifulSoup
url = 'https://www.mkc.edu.tw/'
res = requests.get(url)
html = BeautifulSoup(res.text)
data = html.find('div',{'class':'nws-content'})
data = data.find('ul',{'id':'20076'})
data = data.find_all('span',{'class':'title'})
for i in data:
    print(i.text)
#print(data)