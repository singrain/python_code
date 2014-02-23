from random import randint
num=randint(1,100)
a=1
while a==1:
    answer=int(input('请输入100以内的数字：'))
    if answer>num:
        if answer-num>10:
            print('大了10以上')
        else:
            print('大了10以内')
    if answer<num:
        if num-answer>10:
            print('小了10以上')
        else:
            print('小了10以内')
    if answer==num:
        print('bingo')
        break
