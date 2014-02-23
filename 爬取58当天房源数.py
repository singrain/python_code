import urllib.request
import re

#获取输入的帖子单页html
def getHtml2(url2):
    html2=urllib.request.urlopen(url2).read().decode('utf-8')
    return html2

#寻找关键字
def getImage(html2):
    reg2=r'今天'
    imglist=re.findall(reg2,html2)
    x=0
    #print (imglist)
    for a in imglist:
        x+=1
    #print(x)
    return x

#调用函数
num=1
i=0
while num<=100:
    url='http://sh.58.com/chuzu/pn%d'%num
    #print(url)
    html2=getHtml2(url)
    pro_num=getImage(html2)
    #print(pro_num)
    if  pro_num<35:
        #i+=1
        print(pro_num)
    else:
        pro_num=35
        #print(pro_num)
    num+=1
    i+=pro_num
else:
    print("完成")

#print((num-1-i)*35)
print(i)
