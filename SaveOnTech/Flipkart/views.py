from bs4 import BeautifulSoup
import requests
from my_fake_useragent import UserAgent
import random
import re

def str2int(s):
    return(int(re.sub('[^ 0-9 .]','',s)))

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
        self.name=self.soup.select('._35KyD6')[0].text
    def pprice(self):
        price=self.soup.findAll('div',{'class':'_1vC4OE _3qQ9m1'})[0].text
        self.price=str2int(price)
    def pdiscount(self):
        temp=self.soup.findAll('div',{'class':'VGWI6T _1iCvwn'})
        if(len(temp)==0):
            discount=0
            self.aprice=self.price
        else:
            discount=self.soup.findAll('div',{'class':'VGWI6T _1iCvwn'})[0].text
            self.discount=str2int(discount)
            self.aprice=(self.price*100)/self.discount
    def pimg(self):
        temp=self.soup.findAll('div',{'class':'_2_AcLJ'})[0]
        self.img=str((temp['style'].split('(')[1]).split('?')[0])
def website(soup):
    s = soup.findAll('a', {'class': '_31qSD5'})
    P = []
    l=[]
    for i in s:
        t = str(('https://www.flipkart.com' + i['href'].split('?')[0]))
        l.append(t)
    ls=set(l)
    print(ls)
    for i in ls:
        p = Product()
        p.phref(i)
        p.pname()
        p.pprice()
        p.pdiscount()
        p.pimg()
        print(p.name)
        P.append(p)
    print(123)
    return(P)
