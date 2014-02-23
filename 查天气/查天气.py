import urllib.request
import json
import time
from city import city


exit=False

while not exit: 
    #输入城市
    cityname=input('输入你想要查询的城市(按Q退出)：')
    #退出功能
    if cityname=='q'or cityname=='Q':
        print('退出')
        exit=True
    else:
        #校验城市名
        citycode=city.get(cityname)

        #调用查询接口
        if citycode:
            try:
                url='http://www.weather.com.cn/data/cityinfo/%s.html' % citycode
                content=urllib.request.urlopen(url).read().decode('utf-8')
                #把json转换成字典格式
                data=json.loads(content)
                result=data['weatherinfo']
                str_temp=('%s\n%s~%s')%(result['weather'],result['temp1'],result['temp2'])
                print(str_temp)
                #保留查询记录，当前时间、城市、天气
                
                f=open('天气查询记录.txt','a')
                f.write(('%s\n%s\n%s\n')%(time.strftime('%Y-%m-%d',time.localtime(time.time())),cityname,str_temp))
                f.close()
            except:
                print('查询失败！')
                
        else:
            print('没有找到您输入的城市！')
        


