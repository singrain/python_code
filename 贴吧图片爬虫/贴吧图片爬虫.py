import urllib.request
import re

#获取方式一：符合要求的帖子单页html
def getHtml1(id):
    #限制获取的帖子数（这个函数写错了，只有有符合要求的就会跳函数了,考虑定义两个函数）
    url1='http://tieba.baidu.com/p/%s'%id
    html1=urllib.request.urlopen(url1).read().decode('gbk')
    reg1=r'tieba.baidu.com/f\?kw=%C9%E3%D3%B0'
    resultlist=re.findall(reg1,html1)
    if resultlist:
        return html1
        


#获取方式二：输入的帖子单页html
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
            print('超过图片数量限制，请付费！')
            break

#调用第二种获取方式
#html2=getHtml2('http://tieba.baidu.com/p/2533674562')
#getImage(html2)

#调用第一种获取方式
#id=input()
#while id<=2537728262:
    
html1=getHtml1(2537728260)
#print(html1)
if html1:
    getImage(html1)
    print('下载成功！')
else:
    print('没有找到符合要求的帖子！')
