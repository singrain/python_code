#coding:utf-8
import urllib.request
import re
import time
#the time now
time=time.strftime('%Y-%m-%d',time.localtime(time.time()))

url_id=1325
while url_id<=(url_id+50):
    #visit the page
    url='http://www.youdaili.cn/Daili/http/%d.html'%url_id
    req=urllib.request.Request(url)
    response=urllib.request.urlopen(url)
    html=response.read().decode('utf-8')
    #find the time on the page
    reg=re.compile(r'\d{4}-\d{2}-\d{2}')
    result=reg.findall(html)
    result=result[0]
    #is the page released today?
    if result==time:
        print('开始获取,开始下载')
        reg2=re.compile(r'\d*\.\d*\.\d*\.\d*')
        result2=reg2.findall(html)
        print('下载完成')
        #print (result2)
        break

    else:
        url_id+=5
        #print(url_id)

else:
    print('获取失败...')

