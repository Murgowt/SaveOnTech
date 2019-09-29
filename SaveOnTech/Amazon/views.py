from bs4 import BeautifulSoup
import requests
from my_fake_useragent import UserAgent
import random
import re

ua=UserAgent()
link=r'https://www.amazon.in/s?i=electronics&bbn=1805560031&rh=n%3A976419031%2Cn%3A976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_36%3A1318506031%2Cp_89%3AAsus%7CHUAWEI%7CHonor%7CLenovo%7CMi%7CMotorola%7CNokia%7COPPO%7CRedmi%7CSamsung%7CVivo%7CXiaomi%7Crealme%2Cp_n_operating_system_browse-bin%3A1485077031%2Cp_72%3A1318476031%2Cp_n_feature_seven_browse-bin%3A8561133031%2Cp_n_feature_eight_browse-bin%3A8561112031%7C8561116031%2Cp_n_feature_three_browse-bin%3A1897963031%2Cp_n_condition-type%3A8609960031%2Cp_n_feature_five_browse-bin%3A8561106031%2Cp_n_feature_two_browse-bin%3A1898707031%2Cp_n_pct-off-with-tax%3A2665399031%2Cp_n_feature_thirteen_browse-bin%3A8561102031&dc&fst=as%3Aoff&qid=1567887652&rnid=8561098031&ref=sr_nr_p_n_feature_thirteen_browse-bin_2'
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




csession=requests.session()
user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}
req=csession.get(link,headers=headers)
content=req.content
soup=BeautifulSoup(content,'html.parser')


def str2int(s):
    return(float(re.sub('[^ 0-9 .]','',s)))
class Product:
    def __init__(self):
        self.href=None
        self.name=None
        self.aprice=None
        self.price=None
        self.discount=None
        self.img=None
        self.flag=0
    def flaged(self):
        self.flag=1
    def phref(self,href):
        self.href=href
        user = random.choice(user_agent_list)
        header = {'User-Agent': user}
        req=requests.get(href,headers=header)
        content=req.content
        self.soup=BeautifulSoup(content,'html.parser')
        
    def pname(self):
        temp=self.soup.findAll('span',{'class':'a-size-large'})
        if(len(temp)==0):
            self.flaged()
        else:
            self.name=temp[0].text.strip()
                
        
    def pprice(self):
        temp=self.soup.findAll('span',{'class':'a-size-medium a-color-price priceBlockDealPriceString'})
        if(len(temp)==0):
            self.price=0
            self.flaged()
        else:
            self.price=str2int(temp[0].text)
        
    def pdiscount(self):
        
        temp=self.soup.findAll('span',{'class':'priceBlockStrikePriceString a-text-strike'})
        if(len(temp)==0):
            discount=0
            self.aprice=self.price
        else:
            self.aprice=str2int(temp[0].text)
            self.discount=((self.aprice-self.price)/self.aprice)*100

        
    def pimg(self):
        temp=self.soup.findAll('span',{'class':'a-button-text'})
        if(len(temp)==0):
            self.flaged()
        else:
            print(temp)
        print(self.img)

s=soup.findAll('div',{'class':'s-result-list s-search-results sg-row'})
P=[]
t=[]
count=0
for i in s:
    t=i.findAll('a',{'class':'a-size-base a-link-normal s-no-hover a-text-normal'})
p=[]
for i in t:
    p.append('https://www.amazon.in'+i['href'].split('?')[0])
        
for q in range(0,10):
    i=p[q]
    t=Product()
    t.phref(i)
    t.pname()
    t.pprice()
    t.pdiscount()
    t.pimg()
    if(t.flag==1):
        print("FLAGGED")









