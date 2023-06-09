from selenium import webdriver
from selenium.webdriver.chrome.options import Options#設定
from bs4 import BeautifulSoup
import time
#是否在背景執行
#chrome_option = Options()
#chrome_option.add_argument('--headless')
#chrome = webdriver.Chrome(options=chrome_option)
chrome = webdriver.Chrome()
chrome.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone")
for i in range(3):#重複抓三次資料
    time.sleep(2)#等資料載入
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight);")#移到最下方
htmlpage = BeautifulSoup(chrome.page_source)#抓取頁面程式碼
item_list = htmlpage.findAll('h5',{'class','prod_name'})#找商品名稱
for i in item_list:#把商品的清單輸出出來
    print(i.text)
chrome.close()#把瀏覽器關起來