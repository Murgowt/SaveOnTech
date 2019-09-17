from django.shortcuts import render

# Create your views here.
import requests
import re
import bs4
res=requests.get('https://www.snapdeal.com/products/mobiles-mobile-phones/filters/Form_s~Smartphones?sort=plrty&q=Form_s%3ASmartphones%7CPrice%3A10000%2C20000%7CBrand%3AVivo%5EOppo%5EMI%5EMoto%7CRAM_s%3A4%20GB%5E6%20GB%7CConnectivity_s%3AVoLTE%7CScreensize_s%3A6.0%20%26%20Above%7CPrimaryCamera_s%3A8MP-13MP%7C')
soup=bs4.BeautifulSoup(res.text,'html.parser')
def Hello(soup):
    r=[]
    p1=soup.select('.product-title')#name
    p2=soup.select('.lfloat.product-price')#discount price
    p3=soup.select('.lfloat.product-desc-price.strike')#actual price
    p4=soup.select('.product-discount')#discount
    p5=soup.select('.product-tuple-image')#for href
    p6=soup.select('.product-image')#for images(need to extract srcs again)
    for i in range(len(p1)):
        l=[]
        l.append(p1[i].text)
        l.append(int(re.sub('[^ 0-9]','',p2[i].text)))
        l.append(int(re.sub('[^ 0-9]','',p3[i].text)))
        l.append(int(re.sub('[^ 0-9]','',p4[i].text)))
        l.append(p5[i].text)
        r.append(l)
    print(r)    
Hello(soup)
        
        
        
        
        
