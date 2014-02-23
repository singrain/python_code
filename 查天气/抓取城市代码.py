import urllib.request

url1='http://m.weather.com.cn/data5/city.xml'
content1=urllib.request.urlopen(url1).read().decode('utf-8')
provinces=content1.split(',')
#print(provinces)

#抓省份
for p in provinces:
    p_code=p.split('|')[0]
    #print(p.split('|'))
    url2='http://m.weather.com.cn/data3/city%s.xml'%p_code
    content2=urllib.request.urlopen(url2).read().decode('utf-8')
    citys=content2.split(',')

#抓城市，限制了每个省份只抓3个城市
    for c in citys[:3]:
        c_code=c.split('|')[0]
        url3='http://m.weather.com.cn/data3/city%s.xml'%c_code
        content3=urllib.request.urlopen(url3).read().decode('utf-8')
        districts=content3.split(',')

#抓地区，限制每个城市只抓3个地区
        for d in districts[:3]:
            d_code=d.split('|')[0]
            name=d.split('|')[1]
            url4='http://m.weather.com.cn/data3/city%s.xml'%d_code
            content4=urllib.request.urlopen(url4).read().decode('utf-8')
            code=content4.split('|')[1]
            line="'%s':'%s',\n"%(name,code)
            
#保存文件
result='city = {\n%s}'%line
print (result)
f = open('city2.py', 'w')
f.write(result)
f.close()
        
