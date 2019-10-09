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
        self.flag=0
        self.pr=0
    def flaged(self):
        self.flag = 1
    def phref(self,href):
        self.href=href
        req=requests.get(href)
        content=req.content
        self.soup=BeautifulSoup(content,'html.parser')
    def pname(self):
        temp=self.soup.select('.pdp-e-i-head')
        if (len(temp) == 0):
            self.flaged()
        else:
            self.name = temp[0].get('title')
    def pprice(self):
        temp=self.soup.select('.payBlkBig')
        if (len(temp) == 0):
            self.price = 0
            self.flaged()
        else:
            self.price = str2int(temp[0].text)
    def pdiscount(self):
        temp=self.soup.select('.pdpDiscount')
        if (len(temp) == 0):
            discount = 0
            self.aprice = self.price
        else:
            self.discount = str2int(temp[0].text)
            self.aprice = (self.price * 100) / self.discount
    def pimg(self):
        temp=self.soup.findAll('a',{'data-slide-index':'0'})
        if (len(temp) == 0):
            self.flaged()
        else:
            self.img=str(temp[0].img['src'])
def Hello(soup):
    s = soup.select('.product-tuple-image')
    P = []
    names=[]
    for i in s:
        t = str(i.a['href'])
        p = Product()
        p.phref(t)
        p.pname()
        p.pprice()
        p.pdiscount()
        p.pimg()
        if (p.flag == 1):
            continue
        else:
            temp = p.name.split('(')[0].lower()
            temp2 = temp.replace(' ', '')

            if (temp2 in names):
                continue
            else:
                names.append(temp2)
                P.append(p)
        print('Yo!!')
    return(P)
