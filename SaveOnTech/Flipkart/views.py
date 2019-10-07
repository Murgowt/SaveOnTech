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
        self.flag=0
    def flagged(self):
        self.flag=1
    def phref(self,href):
        self.href=href
        req=requests.get(href)
        content=req.content
        self.soup=BeautifulSoup(content,'html.parser')
    def pname(self):
        temp=self.soup.select('._35KyD6')
        if (len(temp) == 0):
            self.flaged()
        else:
            self.name = temp[0].text.strip()
    def pprice(self):
        temp=self.soup.findAll('div',{'class':'_1vC4OE _3qQ9m1'})
        if (len(temp) == 0):
            self.price = 0
            self.flaged()
        else:
            self.price = str2int(temp[0].text)
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
        temp=self.soup.findAll('div',{'class':'_2_AcLJ'})
        if (len(temp) == 0):
            self.flaged()
        else:
            temp2 = temp[0]
            self.img=str((temp2['style'].split('(')[1]).split('?')[0])
def Hello(soup):
    s = soup.findAll('a', {'class': '_31qSD5'})
    P = []
    names=[]
    l=[]
    for i in s:
        t = str(('https://www.flipkart.com' + i['href'].split('?')[0]))
        l.append(t)
    ls=set(l)
    for i in ls:
        p = Product()
        p.phref(i)
        p.pname()
        p.pprice()
        p.pdiscount()
        p.pimg()
        P.append(p)
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
        print('0')
    return(P)
