#coding:utf-8
import urllib.request
import urllib.parse
import re
import time
import os
import http.cookiejar
import urllib.error
from random import randint
#-----------------------所需参数----------------------------------------
login_url='http://wotanbai.com/account/login?came_from=http%3A//wotanbai.com/'

#登录需要post的值
values={'email':'360370783@qq.com',
'passwd':'19901028',
'csrf_token':'cf9f7085c2a7d4b23a174af71af0afd26814acd4',
'form.submitted':'登录'}
data=urllib.parse.urlencode(values).encode('ISO-8859-1')

#登录需要添加的headers
headers={'POST':login_url,
      'Host':'wotanbai.com',
      'Referer':'http://wotanbai.com/account/login?came_from=http%3A//wotanbai.com/',
      'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)\
       Chrome/29.0.1547.57 Safari/537.36'}

#-----------------------休眠时间----------------------------------------
sleeptime=randint(1,3)
#-----------------------登录模块----------------------------------------
class Login(object):
    def __init__(self,login_url,data,headers):
        self.login_url=login_url
        self.data=data
        self.headers=headers

    def setcookie(self):
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)

    def login(self):
        req=urllib.request.Request(self.login_url,self.data,self.headers)
        login_html=urllib.request.urlopen(req).read().decode('utf-8')
        reg=re.compile('退出')
        result=reg.findall(login_html)
        if result:
            print('登录成功！O(∩_∩)O')
        else:
            print('登录失败！o(╯□╰)o')

#-----------------------下载模块----------------------------------------
class Download(object):
    def __init__(self,page_url,page_html,title,album_html):
        self.page_url=page_url
        self.page_html=page_html
        self.title=title
        self.album_html=album_html

    def open(self,num):
        req=urllib.request.Request(self.page_url)
        try:
            open_page=urllib.request.urlopen(req)
            self.page_html=open_page.read().decode('utf-8')
        except urllib.error.URLError as e:
            print(e.reason)
        #self.page_html=open_page.read().decode('utf-8')
        reg=re.compile('<div>女<\/div>')
        result=reg.findall(self.page_html)
        if result:
            print('活捉妹纸%s枚~~O(∩_∩)O~'%num)
        return result

    #下载头像
    def download(self,id):
        reg=re.compile('src="(\/photo\/\d{10})" alt="头像"')
        result=reg.findall(self.page_html)
        if result:
            print('找到照片！')
            reg2=re.compile('<p>(.+)</p>')
            result2=reg2.findall(self.page_html)
            result2[0]=result2[0].replace('/','_')

            #新建文件夹
            path = "D:\\python\\code\\wotanbai"
            self.title = result2[0]+'_'+str(id)
            new_path = os.path.join(path, self.title)
            if not os.path.isdir(new_path):
                os.makedirs(new_path)

            #下载头像
            try:
                download=urllib.request.urlretrieve('http://www.wotanbai.com'+result[0],'D:\\python\\code\\wotanbai\\'+self.title+'\\'+result2[0]+'_'+str(id)+'.jpg')
            except urllib.error.URLError as e:
                print(e.reason)
        else:
            print('草，没有照片！')

    #下载相册
    def download_album(self,album_url):
        try:
            open_album=urllib.request.urlopen(album_url)
            self.album_html=open_album.read().decode('utf-8')
        except urllib.error.URLError as e:
            print(e.reason)
        #album_html=open_album.read().decode('utf-8')
        ##print(album_html)
        reg=re.compile('<a href="/.+/photos/photo/(.+)">')
        result=reg.findall(self.album_html)
        if result:
            print('找到相册！')
            i=1
            for album_img in result:
                ##print(album_img)
                #下载相册
                try:
                    download_album=urllib.request.urlretrieve('http://www.wotanbai.com/photo/10000'+album_img+'','D:\\python\\code\\wotanbai\\'+self.title+'\\'+'%s.jpg'%i)
                except urllib.error.URLError as e:
                    print(e.reason)
                i+=1
        else:
            print('草！没找到相册！')

#-----------------------调用方法----------------------------------------

starttime=time.time()
#调用登录方法
login_page=Login(login_url,data,headers)
login_page.setcookie()
login_page.login()

#调用图片下载方法
num=1
id=20045
while id<30000:
    page_url='http://wotanbai.com/%s/profile'%id
    album_url='http://wotanbai.com/%s/photos'%id
    download_img=Download(page_url,'','','')
    result=download_img.open(num)
    if result:
        num+=1
        #调用头像下载方法
        download_img.download(id)
        #调用相册下载方法
        download_img.download_album(album_url)
        time.sleep(sleeptime)
    id+=1
    print(id)
    if (id==12000)or(id==15000)or(id==20000)or(id==22000)or(id==25000):
        time.sleep(sleeptime)
else:
    endtime=time.time()
    print('采集完成,耗时：%s'%(endtime-starttime))






