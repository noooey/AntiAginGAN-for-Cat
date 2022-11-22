# -*- coding: utf-8 -*-

# import requirements
import os
import sys
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
from dotenv import load_dotenv

# load .env
load_dotenv()

# const
idx = 0
one_page = 30 # 한 페이지에 이미지 개수
url = os.environ.get('URL')

# webdrivier options
option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
option.add_experimental_option("useAutomationExtension", False)
option.add_experimental_option("excludeSwitches", ['enable-automation'])

# connect Chrome webdriver
# Must match chrome to driver version.
driver = webdriver.Chrome(executable_path='/home/kueyeon/chromedriver', chrome_options=option)

# access web page, wait max 5sec
driver.get(url)
driver.implicitly_wait(5)

# move into the frame
driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame'))
driver.implicitly_wait(5)

# HTML code machining for crawling
category_html = driver.page_source
category_soup = BeautifulSoup(category_html,'html.parser')

category_word = [('s304',2), ('s275',3)]

for x in category_word:
    categories = category_soup.select('ul.'+x[0]+' li') # select elements

    for y in range(len(categories)):
        actions = ActionChains(driver)
        hover_button= driver.find_element_by_xpath(f'//*[@id="css_gnb_frame"]/div[1]/ul/li[{x[1]}]')
        actions.move_to_element(hover_button)

        kind_button = driver.find_element_by_xpath(f'//*[@id="css_gnb_frame"]/div[{x[1]}]/ul/li[{y+1}]')
        actions.click(kind_button)
        actions.perform()

        # wait a second...
        time.sleep(0.5)

        file_idx = 0 # file index
        success = 0 # number of seccess images 

        # HTML code machining for crawling
        init_html = driver.page_source
        init_soup = BeautifulSoup(init_html,'html.parser')

        # select first paging herf for accessing each page
        paging = init_soup.select('div#paging a') # select elements
        page_path = paging[-1].get('href')
        pages = int(page_path.split('=')[-1])
        page_endpoint = "=".join(page_path.split('=')[:-1])+'='
        # print(page_endpoint)

        # 폴더 경로
        path = '/home/kueyeon/workspace/virtual-cat/data/images/kitten/'+str(idx)

        for i in range(1, pages+1):
            # access each pages
            print(url+page_endpoint+str(i))
            driver.get(url+page_endpoint+str(i))
            driver.implicitly_wait(5)

            # HTML code machining for crawling
            html = driver.page_source
            soup = BeautifulSoup(html,'html.parser')

            imgs = soup.select('div.list img') # select elements

            # save files
            for img in imgs:
                # print(url+img.get('src'))
                src = url+img.get('src')
                format = src[-4:]

                # file path
                length = 4
                filename = '0'*(length-len(str(file_idx)))+str(file_idx)
                saveUrl = path+'/'+filename+format

                # user-agent 헤더를 가지고 있어야 접근 허용하는 사이트도 있을 수 있음(pixabay가 이에 해당)
                req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0'})
                try:
                    imgUrl = urllib.request.urlopen(req).read() #웹 페이지 상의 이미지를 불러옴
                    if not os.path.exists(path):
                        os.makedirs(path)
                    with open(saveUrl,"wb") as f: # directory open
                        f.write(imgUrl) # save file
                    success+=1
                except urllib.error.HTTPError:
                    print('에러')
                    sys.exit(0)
                file_idx += 1
        
        idx += 1
        print('성공 : '+str(success))