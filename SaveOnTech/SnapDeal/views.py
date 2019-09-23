from django.shortcuts import render

# Create your views here.
from bs4 import BeautifulSoup
import requests
from my_fake_useragent import UserAgent
import random
import re

def str2int(s):
    return(int(re.sub('[^0-9.]','',s)))

class Product:
    def __init__(self):
        self.href=None
        self.name=None
        self.aprice=None
        self.price=None
        self.discount=None
        self.img=None
    def phref(self,href):
        self.href=href
        req=requests.get(href)
        content=req.content
        self.soup=BeautifulSoup(content,'html.parser')
    def pname(self):
        self.name=self.soup.select('.pdp-e-i-head')[0].get('title')
    def pprice(self):
        price=self.soup.select('.payBlkBig')[0].text
        self.price=str2int(price)
    def pdiscount(self):
        discount=self.soup.select('.pdpDiscount')[0].text
        self.discount=str2int(discount)
        self.aprice=(self.price*100)/self.discount
    def pimg(self):
        temp=self.soup.findAll('a',{'data-slide-index':'0'})
        self.img=str(temp[0].img['src'])
def Hello(soup):
    s = soup.select('.product-tuple-image')
    P = []
    for i in s:
        t = str(i.a['href'])
        p = Product()
        p.phref(t)
        p.pname()
        p.pprice()
        p.pdiscount()
        p.pimg()
        print("done")
        P.append(p)
    return(P)
