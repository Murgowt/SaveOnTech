from django.shortcuts import render
from bs4 import BeautifulSoup
import re
import requests
from my_fake_useragent  import UserAgent
import random
from Flipkart import views as FV
from Amazon import views as AV
from SnapDeal import views as SV
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
    ]

user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}
ua = UserAgent()


def Organizer(request):
    lr=LowRange()


def LowRange():
    Alink = r'https://www.amazon.in/s?i=electronics&bbn=1805560031&rh=n%3A976419031%2Cn%3A976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_36%3A1318506031%2Cp_89%3AAsus%7CHUAWEI%7CHonor%7CLenovo%7CMi%7CMotorola%7CNokia%7COPPO%7CRedmi%7CSamsung%7CVivo%7CXiaomi%7Crealme%2Cp_n_operating_system_browse-bin%3A1485077031%2Cp_72%3A1318476031%2Cp_n_feature_seven_browse-bin%3A8561133031%2Cp_n_feature_eight_browse-bin%3A8561112031%7C8561116031%2Cp_n_feature_three_browse-bin%3A1897963031%2Cp_n_condition-type%3A8609960031%2Cp_n_feature_five_browse-bin%3A8561106031%2Cp_n_feature_two_browse-bin%3A1898707031%2Cp_n_pct-off-with-tax%3A2665399031%2Cp_n_feature_thirteen_browse-bin%3A8561102031&dc&fst=as%3Aoff&qid=1567887652&rnid=8561098031&ref=sr_nr_p_n_feature_thirteen_browse-bin_2'
    Flink=r'https://www.flipkart.com/mobiles/smartphones~type/pr?sid=tyy%2C4io&p%5B%5D=facets.processor_brand%255B%255D%3DSnapdragon&p%5B%5D=facets.sim_type%255B%255D%3DDual%2BSim&p%5B%5D=facets.internal_storage%255B%255D%3D64%2B-%2B127.9%2BGB&p%5B%5D=facets.number_of_cores%255B%255D%3DOcta%2BCore&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3D10000&p%5B%5D=facets.price_range.to%3D20000&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&p%5B%5D=facets.type%255B%255D%3DSmartphones&p%5B%5D=facets.operating_system%255B%255D%3DAndroid&p%5B%5D=facets.screen_size%255B%255D%3D6%2Binch%2B%2526%2Babove&p%5B%5D=facets.battery_capacity%255B%255D%3D5000%2BmAh%2B%2526%2BAbove&p%5B%5D=facets.battery_capacity%255B%255D%3D4000%2B-%2B4999%2BmAh&p%5B%5D=facets.clock_speed%255B%255D%3D2.5%2BGHz%2B%2526%2BAbove&p%5B%5D=facets.clock_speed%255B%255D%3D2%2B-%2B2.5%2BGHz&p%5B%5D=facets.network_type%255B%255D%3D4G%2BVOLTE&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DHuawei&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DVivo&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.serviceability%5B%5D%3Dfalse'
    Slink=r'https://www.snapdeal.com/products/mobiles-mobile-phones/filters/Form_s~Smartphones?sort=plrty&q=Form_s%3ASmartphones%7CPrice%3A10000%2C20000%7CBrand%3AVivo%5EOppo%5EMI%5EMoto%7CRAM_s%3A4%20GB%5E6%20GB%7CConnectivity_s%3AVoLTE%7CScreensize_s%3A6.0%20%26%20Above%7CPrimaryCamera_s%3A8MP-13MP%7C'
    linklist={Alink:AV.Hello,Flink:FV.Hello,Slink:SV.Hello}

    for link in linklist:
        req = requests.get(link, headers=headers)
        content = req.content
        soup = BeautifulSoup(content, 'html.parser')
        print(linklist[link](soup))


LowRange()