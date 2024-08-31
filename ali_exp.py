from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import random
import sys
import openpyxl
from openpyxl import load_workbook
import pandas as pd

url="https://fr.aliexpress.com/category/205000316/men-clothing.html?category_redirect=1&spm=a2g0o.detail.102.1.6785uCA1uCA1ig"

def scroll():
    for s in range(1,7096,64):
        driver.execute_script(f"window.scrollTo(0, {s});")
        time.sleep(0.1)
service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)
time.sleep(2)
scroll()
listurl=driver.find_elements(by=By.XPATH,value='//*[@id="card-list"]/a')

print(len(listurl))
listurl2=[]
for ps in listurl:
    print(ps.get_attribute('href'))
    listurl2.append(ps.get_attribute('href'))

driver.execute_script("window.open('');")
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.get(listurl2[1])
time.sleep(7)
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(4)

driver.quit()