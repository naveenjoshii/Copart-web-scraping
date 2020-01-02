from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import time as time_
import urllib.request
import os
def millis():
    return int(round(time_.time() * 1000))
root = "D:/ML-Workspace/Dataset For damaged  cars/Data"
copart = "https://www.copart.com"
driver = webdriver.Chrome("C:/Users/HP/Downloads/chromedriver_win32/chromedriver")
count=0
for i in range(2,1000):
    driver.get("https://www.copart.com/lotSearchResults/?free=true&query=toyota&page="+str(i))
    time.sleep(2)
    content = driver.page_source
    soup = BeautifulSoup(content,'lxml')
    tro = soup.findAll('tr', attrs={'class':'odd'})
    tre = soup.findAll('tr', attrs={'class':'even'})
    tr = tro+tre
    for i in tr:
        imageurl = i.find('div',attrs={'class':'viewallphotos'})
        spans = i.findAll('span')
        #print(spans[-4].text)
        fn = spans[-4].text
        directory = root+"/"+fn
        if not os.path.exists(directory):
            os.makedirs(directory)
        imagelink = imageurl.find('a',class_='image_viewer_link')['data-url']
        #print(imagelink[1:])
        driver.get(copart+imagelink[1:])
        time.sleep(2)
        c = driver.page_source
        s = BeautifulSoup(c,'lxml')
        tr = s.findAll('div', class_='viewAllPhotosRelative')
        for i in tr:
            imgsrc = i.find('img')['src']
            title  = i.find('img')['title']
            #print(imgsrc)
            #print(title)
            val = millis()
            count=count+1
            filename = title +"-"+str(val)+".jpg"
            saveimageDir = directory +"/"+ filename
            try:
                urllib.request.urlretrieve(imgsrc, saveimageDir)
            except:
                print("file not found")
        print(title + " car images with " + fn + " saved Successfully !!" + "------------Total Images saved till now "+str(count)+" -------------------")
        time.sleep(2)
