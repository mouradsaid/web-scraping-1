from requests_html import HTMLSession
import pandas as pd
import time
import sys 
import random
from tqdm import tqdm

try:
    f = open("config.txt", encoding='utf-8' )
    url=f.readline().split('URL :')[1].strip().split('?pageNum=')[0]
    first_number=int(f.readline().split('FIRST_PAGEF_NUMBER :')[1].strip())
    last_number=int(f.readline().split('LAST_PAGE_NUMBER :')[1].strip())
    times=float(f.readline().split('TIME(s) :')[1].strip())
    f.close()
except:
    print('\n'*5,'Make sure that the .confg.txt file is written correctly')
    time.sleep(8)
    sys.exit()

colum = {'Name':[],'Phone':[],'Titel':[],'Type':[],'City':[],'Page':[]}
session = HTMLSession()

print('\n'*5)

with tqdm(total=last_number,desc ="Download progress") as pbar:
    for i_this in range(first_number,last_number+1):
        try:
            r = session.get(url+'?pageNum='+str(i_this))
            author = r.html.find('.new-offers-container',first=True).find('.new-card-listing  ')
            for elm in author:
                try:
                    elemant_a=elm.find('.new-card-buts',first=True).find("a")
                    try:
                        colum['Page'].append(i_this)
                    except:
                        colum['Page'].append(None)
                    try:
                        colum['Name'].append(elemant_a[1].xpath('//a/@data-title')[0])
                    except:
                        colum['Name'].append(None)
                    try:
                        colum['Phone'].append(elemant_a[0].xpath('//a/@href')[0].replace('tel:', ''))
                    except:
                        colum['Phone'].append(None)
                    try:
                        colum['Titel'].append(elm.find('.new-card-title')[1].text)
                    except:
                        colum['Titel'].append(None)        
                    try:
                        colum['Type'].append(elm.find('.new-card-title')[0].text)
                    except:
                        colum['Type'].append(None)    
                    try:
                        colum['City'].append(elm.find('.new-card-city',first=True).text)
                    except:
                        colum['City'].append(None)         
                except:
                    continue
            time.sleep(times)
            pbar.update(1)
        except:
            continue
            pbar.update(1)

data=pd.DataFrame(colum)
data.to_excel(str(random.randint(0,99999))+'.xlsx',sheet_name='sheet1',index=False) 