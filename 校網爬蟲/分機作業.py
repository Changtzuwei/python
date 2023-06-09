import requests
from bs4 import BeautifulSoup
url = 'https://www.mkc.edu.tw/Home?Sn=EV6S9OxI5fUiItcBOR6%2fsn0j5rmStDGs&%E8%A1%8C%E6%94%BF%E5%96%AE%E4%BD%8D'
res = requests.get(url)
htmlpage = BeautifulSoup(res.text,'lxml')
table = htmlpage.find('table',{'class':"table table-bordered table-hover table-striped"})
print(table)
#table.findAll('strong')
strong = table.findAll('strong')
file = open(r'馬偕護專校徽.txt','w',encoding='utf-8')
print(strong)
for i in strong:
    file.write(i.text+'\n')
    print(i.text)