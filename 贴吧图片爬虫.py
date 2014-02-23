import urllib.request
import re

#获取输入的帖子单页html
def getHtml2(url2):
    html2=urllib.request.urlopen(url2).read().decode('gbk')
    return html2

#抽取图片相关列表，并下载图片
def getImage(html2):
    reg2=r'http://imgsrc.baidu.com/forum/w%3D580.+\.jpg'
    imglist=re.findall(reg2,html2)
    x=1
    #限制下载的图片数
    for imgurl in imglist:
        if x<=10:
            urllib.request.urlretrieve(imgurl,'%s.jpg'%x)
            x+=1
        else:
            print('超过图片数量限制！')
            break

#调用函数
html2=getHtml2('http://tieba.baidu.com/p/2533674562')
getImage(html2)
