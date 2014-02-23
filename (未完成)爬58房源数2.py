import urllib.request
import re

#获取输入的帖子单页html
def getHtml2(url2):
    html2=urllib.request.urlopen(url2).read().decode('utf-8')
    return html2

#寻找关键字
def getImage(html2):
    reg2=r'租金价格'
    imglist=re.findall(reg2,html2)
    x=0
    #print (imglist)
    for a in imglist:
        x+=1
    if x>0:
        return True

#调用函数
i=0
num=10000000000000
while num<200000000000000:
    url='http://cq.58.com/zufang/%14dx.shtml'%num
    #print(url)
    html2=getHtml2(url)
    if html2:
        i+=1
print (i)
