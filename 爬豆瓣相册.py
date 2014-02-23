#coding: utf-8
import urllib.request
import urllib.parse
import urllib.error
import re
import time

x=1
album_id=34035687
num=int(input('请输入你需要跑多少页：'))

starttime=time.time()
while album_id<=(34035687*num):
    url='http://www.douban.com/photos/album/%d/'%album_id
    req=urllib.request.Request(url)
    try:
        response=urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
        #print(e.read().decode("utf8"))

    html=response.read().decode('utf-8')

    album_id+=1
    reg=re.compile('真相')
    result=reg.findall(html)
    if result:
        print('找到对象！')
        reg2=re.compile('http://img3.douban.com/view/photo/thumb/public/p\d{9}.jpg')
        result2=reg2.findall(html)
        for img in result2:
            if result2:
                urllib.request.urlretrieve(img,'D:\python\code\girls\%s.jpg'%x)
                print('已下载%s张'%x)
                x+=1
    else:
        print('没有找到对象！')
    time.sleep(1)

endtime=time.time()

print(endtime-starttime)


