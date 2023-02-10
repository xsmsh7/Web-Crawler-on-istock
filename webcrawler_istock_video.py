#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Video Window Version
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests

class colors:
    MARK = '\033[92m' #GREEN
    RESET = '\033[0m' #RESET COLOR
    
input_category = input("Please enter video category：")
ip_ask = input("Please enter the ip to search (generally enter no)：")
page_num = input("Please enter the page for search：")

if ip_ask == 'no':
    web_path = f"https://www.istockphoto.com/search/2/film?phrase={input_category}&page="
else:
    ip = str(ip_ask)
    web_path = f'https://www.istockphoto.com/search/more-like-this/{ip}?phrase={input_category}&assettype=film&page='
    
browser = webdriver.Chrome(ChromeDriverManager().install())
path = f"istock_video/{input_category}"
current_path = os.path.abspath(os.getcwd())
print("Downloading to",current_path + '\ISTOCK_video\\' + str(input_category) )
if not os.path.exists(path):
        os.makedirs(path)
record = 0
for page in range(1,int(page_num)+1):# 執行1~2頁
    browser.get(web_path + str(page))# 連結網站
    browser.implicitly_wait(3)
    soup = BeautifulSoup(browser.page_source,"html.parser")
    results = soup.find_all("video",{"class":"AssetVideoOverlay-module__mosaicAssetVideo___oiHIk"})
    image_links = [result.get("src") for result in results]   
    image_links = list(set(image_links))
    print(f"{colors.MARK}========================================第{str(page)}頁========================================{colors.RESET}")    
    for index, link in enumerate(image_links):
        print('[',page,']',record+1,':',link)
        record+=1
        img = requests.get(link)
        with open(path + "\\" + input_category + str(index+1) + ".mp4", "wb") as file:  
            file.write(img.content) 

print("Total downloaded:",record)

