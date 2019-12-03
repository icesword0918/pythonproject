import  math
def circlearea(r):
    result=math.pi*r*r
    return result
r=10
print('半径为',r,'的圆面积为：',circlearea(r))

# 使用lambda表达式的代码
r=10
result1=lambda r:math.pi*r*r
print('半径为',r,'的圆面积为：',result1(r))

bookinfo=[('不一样的卡梅拉（全套）',22.50,120),('零基础学AANDRODI',65.10,89.80),('摆渡人',23.40,36.00),('福尔摩斯探案全集8册',22.50,128)]
print('爬到的商品信息:\n',bookinfo,'\n')
bookinfo.sort(key=lambda x:(x[1],x[1]/x[2]))
print('排序后的商品信息：\n',bookinfo)
