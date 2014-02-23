#coding: utf-8
##def main():
##    pass
##
##if __name__ == '__main__':
##    main()

import urllib.request
import time,re
import iplist
from random import choice

#read the page
class View(object):
    def __init__(self,headers,iplist,req):
        self.headers=headers
        self.iplist=iplist
        #self.req=req
    def use_proxy(self):
        #ip list
        #iplist=iplist.result2
        #choice ip
        ip=choice(self.iplist)
        #set ip agent
        proxy_support = urllib.request.ProxyHandler({'http': 'http://'+ip})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)

    def add_header(self,url):
        self.req=urllib.request.Request(url)
        for i in self.headers:
            self.req.add_header(i,self.headers[i])
        #print(req)
        return self.req

    def read_site(self):
        the_page=urllib.request.urlopen(self.req)
        html=the_page.read().decode('utf-8')
        return html

#download the content
class Re_download(object):
    def __init__(self,html,num,title):
        self.html=html
        self.num=num
    def search(self):
        reg=re.compile('<title>(.+) &#8211; 腾讯CDC</title>')
        titlelist=reg.findall(self.html)
        #print(titlelist)
        for self.title in titlelist:
            return self.title
    def download(self):
        f=open('1.txt','a')
        f.write(str(self.title))
        f.close()
        #urllib.request.urlretrieve(title,'%s.txt'%self.num)
        time.sleep(1)

#use the classView
url='http://cdc.tencent.com/?p=7821'
iplist=iplist.result2
headers={'GET':url,
      'Host':'cdc.tencent.com',
      'Referer':'http://cdc.tencent.com/',
      'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36'}
req=''
view_page=View(headers,iplist,req)
view_page.use_proxy()
view_page.add_header(url)
html=view_page.read_site()

#use the classRe_download
num=1
title=''
download_content=Re_download(html,num,title)
download_content.search()
download_content.download()

