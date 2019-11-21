verse = tuple(range(10, 20, 2))  # 创建数值元组
print(verse)

team=('爵士','马刺','公牛','小牛','森林狼','火箭','勇士','开拓者','雷霆','奇才')
for index,item in enumerate(team):
    if index%2==0:
        print(item+'\t\t',end=' ')
    else:
        print(item+'\n')

newteam=('76人','魔术')
team=team+newteam
print(team)