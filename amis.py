from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from tqdm import tqdm , trange

f=open("AME.txt","r")
listo=[]
for iln in f:
    listo.append(iln.strip())
f.close()

wrb = webdriver.Firefox('geckodriver.exe')

for t in listo:
    colum={'url':[],'name':[]}
    url='https://www.mql5.com/en/users/'+t
    wrb.get(url)

    try:
        wrb.find_element(by=By.XPATH, value="//span[@class='friends-list__counter friends-list__counter_mutual']")
    except:
        continue
    nmbr = wrb.find_element(by=By.XPATH, value="//span[@class='friends-list__counter friends-list__counter_mutual']").text
    for i in range(int(nmbr)//10):
        time.sleep(1)
        wrb.find_element(by=By.XPATH, value="//button[contains(@class,'show-more-friends__btn')]").click()
        time.sleep(5)

    try:
        wrb.find_elements(by=By.XPATH, value="//span[@class='friend-block__name']")
    except: 
        continue
    all_links = wrb.find_elements(by=By.XPATH, value="//span[@class='friend-block__name']")
    for i in all_links:
        colum['name'].append(i.text)
        colum['url'].append(i.find_element(by=By.XPATH, value="..").get_attribute('href'))
                
    data=pd.DataFrame(colum)
    data.to_excel(t+'.xlsx')

wrb.quit()