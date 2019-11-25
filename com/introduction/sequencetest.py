# 火车订票系统
title=('车次','出发站-到达站','出发时间','到达时间','历时')
for name in title:
    print(name + '\t\t', end=' ')
print("")
train1=('T40','长春-北京','00：12','12：20','12：08')
for name in train1:
    print(name + '\t\t\t', end=' ')
print("")
train2=('T298','长春-北京',' 00：06','10：50','10：44')
for name in train2:
    print(name + '\t\t', end=' ')
print("")
train3=('Z156','长春-北京','12：48','21：06','08：18')
for name in train3:
    print(name + '\t\t', end=' ')
print("")
train4=('Z62','长春-北京','21：58','06：08','08：20')
for name in train4:
    print(name + '\t\t\t', end=' ')
print("")
print("请输入要购买测车次：")
num=input()
print("请输入乘车人（用逗号分隔）：")
name=input()
if num==train1[0]:
    print("您已购"+train1[0]+"次列车 "+train1[1]+train1[2]+"开，请"+name+"尽快换取纸质车票。【铁路客服】")
elif num==train2[0]:
    print("您已购"+train2[0]+"次列车 "+train2[1]+train2[2]+"开，请"+name+"尽快换取纸质车票。【铁路客服】")
elif num==train3[0]:
    print("您已购"+train3[0]+"次列车 "+train3[1]+train3[2]+"开，请"+name+"尽快换取纸质车票。【铁路客服】")
elif num==train4[0]:
    print("您已购"+train4[0]+"次列车 "+train4[1]+train4[2]+"开，请"+name+"尽快换取纸质车票。【铁路客服】")