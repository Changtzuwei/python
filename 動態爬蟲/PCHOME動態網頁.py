from selenium import webdriver
from selenium.webdriver.chrome.options import Options#設定
from bs4 import BeautifulSoup
import time
#chrome_option = Options()
#chrome_option.add_argument('--headless')
#chrome = webdriver.Chrome(options=chrome_option)
chrome = webdriver.Chrome()
chrome.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone")
for i in range(3):
    time.sleep(2)
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight);")
htmlpage = BeautifulSoup(chrome.page_source)
item_list = htmlpage.findAll('h5',{'class','prod_name'})
for i in item_list:
    print(i.text)
chrome.close()