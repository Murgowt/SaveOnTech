from django.shortcuts import render

# Create your views here.
from bs4 import BeautifulSoup
import requests
from my_fake_useragent import UserAgent
import random
import re

user_agent_list = [
    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    # Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]


def str2int(s):
    return (int(re.sub('[^0-9.]', '', s)))


def str2int(s):
    return (float(re.sub('[^ 0-9 .]', '', s)))


class Product:
    def __init__(self):
        self.href = None
        self.name = None
        self.aprice = None
        self.price = None
        self.discount = None
        self.img = None
        self.flag = 0

    def flaged(self):
        self.flag = 1

    def phref(self, href):
        self.href = href
        user = random.choice(user_agent_list)
        header = {'User-Agent': user}
        req = requests.get(href, headers=header)
        content = req.content
        self.soup = BeautifulSoup(content, 'html.parser')

    def pname(self):
        temp = self.soup.findAll('span', {'class': 'a-size-large'})
        if (len(temp) == 0):

            self.flaged()
        else:
            self.name = temp[0].text.strip()

    def pprice(self):
        temp = self.soup.findAll('span', {'class': 'a-size-medium a-color-price priceBlockDealPriceString'})
        if (len(temp) == 0):
            self.price = 0
            self.flaged()
        else:
            self.price = str2int(temp[0].text)

    def pdiscount(self):

        temp = self.soup.findAll('span', {'class': 'priceBlockStrikePriceString a-text-strike'})
        if (len(temp) == 0):
            discount = 0
            self.aprice = self.price
        else:
            self.aprice = str2int(temp[0].text)
            self.discount = ((self.aprice - self.price) / self.aprice) * 100

    def pimg(self):
        temp = self.soup.findAll('img', {'class': 'imgSwatch'})
        if (len(temp) == 0):
            self.flaged()
        else:
            self.img = temp[0]
            self.img = self.img['src']


def Hello(soup):
    s = soup.findAll('div', {'class': 's-result-list s-search-results sg-row'})
    P = []
    t = []
    count = 0
    for i in s:
        t = i.findAll('a', {'class': 'a-size-base a-link-normal s-no-hover a-text-normal'})
    p = []
    for i in t:
        p.append('https://www.amazon.in' + i['href'].split('?')[0])

    final = []
    names = []
    for i in p:
        t = Product()
        t.phref(i)
        t.pname()
        t.pprice()
        t.pdiscount()
        t.pimg()
        if (t.flag == 1):
            continue
        else:
            temp = t.name.split('(')[0].lower()
            temp2 = temp.replace(' ', '')
            if (temp2 in names):
                continue
            else:
                names.append(temp2)
                final.append(t)
    print('Done.Amazon')
    return(final)
