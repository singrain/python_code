#coding:utf-8
import urllib.request
import urllib.parse
import re
import time
import os
import http.cookiejar
import urllib.error
import random

login_url="https://www.douban.com/accounts/login"
group_url='http://www.douban.com/group/kaopulove/'
sleeptime=random.randrange(30,60)
#回复内容
content1='大王叫我来巡山类~~'
content2='机器人路过，快快交出你的妹纸'
content3='你怎么知道你的人生不是一段代码？像我一样'
content4='LZ，我的节操掉了，帮我捡起来吧O(∩_∩)O~'
content5='我是前排围观的机器人O(∩_∩)O'
content6='Lx你怎么看？？'
content7='lz好，你也是机器人吗？'
content8='我是一个无聊的人写出来的机器人...'
content9='请叫我专业挽尊机器人'
content10='ls，lx的妹纸，都看过来...看过来...看过来...'

contentlist=[content1,content2,content3,content4,content5,content6,content7,content8,content9,content10]

content=random.choice(contentlist)

#登录需要post的值
#没有验证码的情况
values={'source':'group',
'redir':'http://www.douban.com/',
'form_email':'singraindeng@163.com',
'form_password':'d9pemc4p',
'remember':'on',
'user_login':'登录'}
data=urllib.parse.urlencode(values).encode('ISO-8859-1')


#登录需要添加的headers
headers={'POST':login_url,
      'Host':'www.douban.com',
      'Origin':'http://www.douban.com',
      'Referer':'http://www.douban.com/accounts/login',
      'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)\
       Chrome/29.0.1547.57 Safari/537.36'}

#-----------------------登录模块----------------------------------------
class Login(object):
    def __init__(self,login_url,headers):
        self.login_url=login_url
        #self.data=data
        self.headers=headers

    def setcookie(self):
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)

    def check_captcha(self):
        req1=urllib.request.Request(login_url)
        login_html1=urllib.request.urlopen(req1).read().decode('utf-8')
        reg1=re.compile('<input type="hidden" name="captcha-id" value="(.+)"/>')
        result1=reg1.findall(login_html1)
        if result1:
            print('有验证码，需要手动输入验证')
            req2=re.compile('<img id="captcha_image" src="(.+)"')
            captcha_img=req2.findall(login_html1)
            urllib.request.urlretrieve(captcha_img[0],'1.jpg')
            print('验证码已下载完成！')
            return result1[0]

    def login(self,data):
        req=urllib.request.Request(self.login_url,data,self.headers)
        login_html=urllib.request.urlopen(req).read().decode('utf-8')
        reg=re.compile('退出')
        result=reg.findall(login_html)
        if result:
            print('登录成功！O(∩_∩)O')
            ##print(login_html)
        else:
            print('登录失败！o(╯□╰)o')
            ##print(login_html)

#-----------------------发帖模块----------------------------------------
class Reply(object):
    def __init__(self,group_url):
        self.group_url=group_url

##    def setcookie1(self):
##        cj1 = http.cookiejar.CookieJar()
##        opener1 = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj1))
##        urllib.request.install_opener(opener1)

    def open(self,content):
        req3=urllib.request.Request(self.group_url)
        try:
            open_group=urllib.request.urlopen(req3)
            group_html=open_group.read().decode('utf-8')
        except urllib.error.URLError as e:
            print(e.reason)

        reg3=re.compile('<td nowrap="nowrap" class="">(.+)</td>')
        result3=reg3.findall(group_html)
        i=0
        for reply_num in result3:
            if int(reply_num)<=3:
                reg4=re.compile('<a href="(http://www.douban.com/group/topic/.+/)"')
                result4=reg4.findall(group_html)
                topic_url=result4[i]
                print(reply_num)
                print(topic_url)
                #return topic_url
                #过滤已经回过的帖子
                log_file=open('replylog.txt').read()
                reg9=re.compile(topic_url)
                result9=reg9.findall(log_file)
                if result9:
                    print('已经回复过的帖子...跳过')
                else:
                    #获取ck值
                    req8=urllib.request.Request(topic_url)
                    topic_html=urllib.request.urlopen(req8).read().decode('utf-8')
                    ##print(topic_html)
                    reg8=re.compile('ck=(.+)">')
                    result8=reg8.findall(topic_html)
                    ck=result8[0]
                    print(ck)
                    #登录需要添加的headers
                    headers1={'POST':str(topic_url)+'add_comment',
                          'Host':'www.douban.com',
                          'Origin':'http://www.douban.com',
                          'Referer':topic_url,
                          'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)\
                           Chrome/29.0.1547.57 Safari/537.36'}
                    #无验证码
                    values2={'ck':ck,
                            'rv_comment':content,
                            'start':'0',
                            'submit_btn':'加上去'}
                    data2=urllib.parse.urlencode(values2).encode('ISO-8859-1')

                    req6=urllib.request.Request(topic_url+'add_comment',data2,headers1)
                    topic_html=urllib.request.urlopen(req6).read().decode('utf-8')

                    reg7=re.compile('继续发言')
                    result7=reg7.findall(topic_html)
                    if result7:
                        print('回帖成功！O(∩_∩)O')
                        #记录回复过的帖子
                        f=open('replylog.txt','a')
                        f.write(topic_url+'\n')
                        f.close()
                        time.sleep(sleeptime)
                        ##print(login_html)
                    else:
                        print('回帖失败！o(╯□╰)o')
                        input('按任意键退出...')
                        exit()
                        ##print(topic_html)
                i+=1


##    def open_topic(self,topic_url):
##        req5=urllib.request.Request(topic_url)
##        try:
##            open_topic=urllib.request.urlopen(req5)
##            topic_html=open_topic.read().decode('utf-8')
##        except urllib.error.URLError as e:
##            print(e.reason)

##        #登录需要添加的headers
##        headers1={'POST':str(topic_url)+'add_comment',
##              'Host':'www.douban.com',
##              'Origin':'http://www.douban.com',
##              'Referer':topic_url,
##              'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)\
##               Chrome/29.0.1547.57 Safari/537.36'}
##
##        values2={'ck':'qNXK',
##                'rv_comment':'机器人君路过...',
##                'start':'0',
##                'submit_btn':'加上去'}
##        data2=urllib.parse.urlencode(values2).encode('ISO-8859-1')
##
##        req6=urllib.request.Request(topic_url,data2,headers1)
##        topic_html=urllib.request.urlopen(req6).read().decode('utf-8')
##
##        reg7=re.compile('继续发言')
##        result7=reg7.findall(topic_html)
##        if result7:
##            print('回帖成功！O(∩_∩)O')
##            ##print(login_html)
##        else:
##            print('回帖失败！o(╯□╰)o')
##            print(topic_html)






#-----------------------调用方法----------------------------------------
#调用登录方法
login_page=Login(login_url,headers)
login_page.setcookie()
captcha_id=login_page.check_captcha()
print (captcha_id)
if captcha_id:
    #有验证码的情况
    values1={'source':'group',
    'redir':'http://www.douban.com/',
    'form_email':'singraindeng@163.com',
    'form_password':'d9pemc4p',
    'captcha-solution':input('输入验证码'),
    'captcha-id':captcha_id,
    'remember':'on',
    'user_login':'登录'}
    data1=urllib.parse.urlencode(values1).encode('ISO-8859-1')
    login_page.login(data1)
else:
    login_page.login(data)

#调用回帖方法
num=1
refresh_num=0
while refresh_num<=100:
    reply_it=Reply(group_url)
    #reply_it.setcookie1()
    topic_url=reply_it.open(content)
    ##if topic_url:
    ##    print(topic_url)
    #reply_it.open_topic(topic_url)
    refresh_num+=1
input('已经循环100次，点任意键退出...')
exit()
