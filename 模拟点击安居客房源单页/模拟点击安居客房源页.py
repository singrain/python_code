# -*- coding: utf-8 -*-
import urllib.request
import time
from random import choice
import iplist
import os

numbers=1
#input your target
end_num=int(input('请输入你想刷的次数：'))
pro_id=int(input('请输入房源ID：'))
url='http://sh.zu.anjuke.com/fangyuan/%d'%pro_id
#req=urllib.request.Request(url)
#headers
headers={'GET':url,
      'Host':'sh.zu.anjuke.com',
      'Referer':'http://sh.zu.anjuke.com/fangyuan/19971896?__ONLOAD_TIME=1384672537320&__FROM_PAGE=Listing_V2_IndexPage_All&__SERVER_ID=52886d17633f73.19126162&from=Filter_1&__CLICK_TIME=1384672539585',
      'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36'}
#ip list
iplist=iplist.result2
while numbers<=end_num:

    #choice ip
    ip=choice(iplist)
    #set ip agent
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://'+ip})
    opener = urllib.request.build_opener(proxy_handler)

    req=urllib.request.Request(url)
    #add headers
    for i in headers:
        req.add_header(i,headers[i])
    response=urllib.request.urlopen(req)
    #html=response.read().decode('utf-8')
    #print(html)
    print('已刷%d次'%numbers)
    numbers+=1
    time.sleep(10)

print("刷完！")

os.system('pause')

