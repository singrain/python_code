import random

num=input('请输入游戏参与人数：')

x=1
while True:
    if x<=int(num):
        id=input('请第%s位玩家查看词语，按“enter”键'%x)
        name=random.choice(['贱人','基佬','禽兽','屌丝','变态'])
        print(name)
        x+=1
    else:
        print('全部玩家已经完成查看，游戏开始！')
        break


