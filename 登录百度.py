#coding:utf-8
import urllib.request,urllib.parse
import time
import re
import http.cookiejar

url='https://passport.baidu.com/v2/?login'

values={'staticpage':'https://passport.baidu.com/static/passpc-account/html/v3Jump.html',
'charset':'UTF-8',
'token':'fc6e5deee8ae36d466aed1917cc599fb',
'tpl':'pcs',
'apiver':'v3',
'tt':'1386250007209',
'codestring':'',
'safeflg':'0',
'u':'http://www.baidu.com/p/sys/redirect?url=w5132008',
'isPhone':'false',
'quick_user':'0',
'loginmerge':'true',
'logintype':'basicLogin',
'username':'360370783@qq.com',
'password':'d9pemc4p',
'verifycode':'',
'mem_pass':'on',
'ppui_logintime':'9707',
'callback':'parent.bd__pcbs__ycserf'}

data=urllib.parse.urlencode(values).encode('ISO-8859-1')
print(data)

headers={'POST':'https://passport.baidu.com/v2/api/?login',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'passport.baidu.com',
'Referer':'https://passport.baidu.com/v2/?login&tpl=pcs&u=http%3A//www.baidu.com/p/sys/redirect%3Furl%3Dw5132008',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36'}

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

req=urllib.request.Request(url,data,headers)
html=urllib.request.urlopen(req).read().decode('utf-8')
print(html)
