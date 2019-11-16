print("输入1，查询当前余额","\n输入2，查询当前剩余流量","\n输入3，查询当前剩余通话","\n输入0，退出自助查询系统！")
number=int(input())
if number==0:
    print("退出自助查询系统！")
elif number==1:
    print("当前余额为：45元")
elif number==2:
    print("当前剩余流浪为：3G")
elif number==3:
    print("当前剩余通话为：50分钟")
else:
   print("不符合条件数字，请重新输入")