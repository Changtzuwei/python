from urllib import parse
url = "https://www.mkc.edu.tw/Home?Sn=lkTddRHX%2fk87vdeXUUC4C25i0gGU17En&%E6%9C%AC%E6%A0%A1%E7%B0%A1%E4%BB%8B"
urlparse = parse.urlparse(url)
print(urlparse.netloc)#網路位置
print(urlparse.query)#變數
print(urlparse.scheme)#網路協定