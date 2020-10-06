from random import choice,randint

print('~随机写歌V1.0爱上了SOTB~\nBY OdorajBotoj')

lst = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
with open('out.txt','w',encoding='utf-8') as f:
    for i in range(randint(60,300)):
        f.write(choice(lst))
print('完成!')