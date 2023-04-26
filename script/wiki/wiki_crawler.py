import os
import requests
from bs4 import BeautifulSoup
import time

cookie = {}
agent = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
         "Cookie" : "cf_clearance=EIGWwifVzSBWD78Q3NW0JgS7KlaIxWoPWaOLnE4lc4w-1680598750-0-150; _ga_0BZYS7HPVC=GS1.1.1679988426.1.1.1679988486.0.0.0; _ga=GA1.2.2072305059.1679988427; _gcl_au=1.1.135544876.1679988427; _fbp=fb.1.1679988428882.152420752",
         "Referer": "https://wiki.torn.com/?__cf_chl_tk=TL.t1MH.uhqtSMX.e8F2ZHBf8P1r0MhnRvDdl0Lxqgg-1680598750-0-gaNycGzNCxA"}

def save_subpages(url):
    # 获取页面内容
    time.sleep(1)
    response = requests.get(url, cookies=cookie, headers=agent)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 提取页面标题作为文件名
    title = soup.find("h1").text.strip().replace("\n", "") + ".html"
    
    # 判断该文件是否已存在，如果存在，则不需要再次保存该页面
    if os.path.exists(title):
        print(title + ' already exists')
        return
    
    # 将页面内容保存到本地文件中
    with open(title, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
        print(title + ' saved')
    
    # 获取该页面所有链接
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('https://wiki.torn.com/'):
            links.append(href)
    
    # 递归遍历所有链接，并保存它们的页面内容
    # for link in links:
    #     save_subpages(link)

save_subpages("https://wiki.torn.com/wiki/New_Player_Missions")