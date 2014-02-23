import urllib.request
import urllib.parse
import http.cookiejar

i=0
while i<10:
    cookie=http.cookiejar.CookieJar()
    cjhdr=urllib.request.HTTPCookieProcessor(cookie)
    opener=urllib.request.build_opener(cjhdr)
    response=urllib.request.urlopen('http://t.sohu.com/settings/bindMobile/registSendVerificationCode')
    print(response)
    data={'mobileNumber':'15921197597'}
    r=opener.open('http://t.sohu.com/settings/bindMobile/registSendVerificationCode',urllib.parse.urlencode(data).encode('utf-8'))
    print(r.read().decode('gbk'))
    i+=1
