import urllib.request
import re
import urllib.parse

#下载图片
def getImage(html):
    reg=r'http://imgsrc.baidu.com/forum/w%3D580.+\.jpg'
    imgre=re.compile(reg)
    imglist=imgre.findall(html)
    x=1
    #限制下载的图片数
    for imgurl in imglist:
        if x<=10:
            urllib.request.urlretrieve(imgurl,'%s.jpg'%x)
            x+=1
        else:
            print('超过图片数量限制')
            break

#获取html
def getHtml(url):
    html=urllib.request.urlopen(url).read().decode('gbk')
    reg=r'%C9%E3%D3%B0'
    imgre=re.compile(reg)
    resultlist=imgre.findall(html)
    if resultlist:
        return html

#获取帖子id
def getUrl(num):
    url='http://tieba.baidu.com/p/%s'%num
    return url

#从输入的帖子开始获取，直到上限
num=input('输入起始数:')
while int(num)<=2537728262:
    url=getUrl(num)
    html=getHtml(url)
    getImage(html)
    num+=1
else:
    print('输入ID超出范围！')
