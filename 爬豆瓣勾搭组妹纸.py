# -*- coding: utf-8 -*-
import urllib.request
import re
import time
import os

#获取输入的帖子单页html
def getHtml2(url2):
    html2=urllib.request.urlopen(url2).read().decode('utf-8')
    return html2

#抽取图片相关列表，并下载图片
def gettopic(html2):
    reg2=re.compile(r'http://www.douban.com/group/topic/\d+')
    topiclist=reg2.findall(html2)
    x=0
    #限制下载的图片数
    for topicurl in topiclist:
        x+=1
    return topicurl


#下载图片到本地
def download(topic_page):
    reg3=re.compile(r'http://img3.douban.com/view/group_topic/large/public/.+\.jpg')
    imglist=reg3.findall(topic_page)
    i=1
    download_img=None
    for imgurl in imglist:
#取图片ID为文件名
        img_numlist=re.findall(r'p\d{7}',imgurl)
        for img_num in img_numlist:
            
            download_img=urllib.request.urlretrieve(imgurl,'D:\python\code\girls\%s.jpg'%img_num)
            time.sleep(1) 
            i+=1
            print(imgurl)
    return download_img

#调用函数
page_end=int(input('请输入结束时的页码：'))
num_end=page_end*25
num=0
page_num=1
while num<=num_end:
    html2=getHtml2('http://www.douban.com/group/kaopulove/discussion?start=%d'%num)
    topicurl=gettopic(html2)
    topic_page=getHtml2(topicurl)
    download_img=download(topic_page)
    num=page_num*25
    page_num+=1

else:
    print('采集完成！')

os.system('pause')

