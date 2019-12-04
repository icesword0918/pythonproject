# 定义类
class Geese:
    """大雁类"""
    pass

# 创建类的实例
wildGoose=Geese()
print(wildGoose)

# 创建_init_()方法
class GeeseTest:
    """大雁类测试"""
    def __init__(self):        # 构造方法
        print("我是大雁类！")

wildGooseTest=GeeseTest()    #创建大雁类的实例

class GeeseTest:
    """大雁类测试"""
    def __init__(self,beak,wing,claw):        # 构造方法
        print("我是大雁类！我有以下的特征：")
        print(beak)
        print(wing)
        print(claw)
brak_1="喙的基部较高，长度和头部的长度几乎相等"
wing_1="翅膀长而尖"
claw_1="爪子是蹼状的"
wildGooseTest=GeeseTest(brak_1,wing_1,claw_1)    #创建大雁类的实例

# 创建类的成员并访问
class Geese:
    """大雁类测试"""
    def __init__(self,beak,wing,claw):        # 构造方法
        print("我是大雁类！我有以下的特征：")
        print(beak)
        print(wing)
        print(claw)
    def fly(self,state):
        print(state)
brak_1="喙的基部较高，长度和头部的长度几乎相等"
wing_1="翅膀长而尖"
claw_1="爪子是蹼状的"
wildGoose=Geese(brak_1,wing_1,claw_1)    #创建大雁类的实例
wildGoose.fly("我奉行的时候，一会儿排成个人字，一会排成一字")

class Geese:
    """大雁类"""
    neck="脖子较长"
    wing="振翅频率高"
    leg="腿位于身体的中心支点，行走自如"
    number=0
    def __init__(self):
        Geese.number+=1
        print("\n我是第"+str(Geese.number)+"只大雁，我属于雁类！我有以下的特征：")
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)

# 创建4个雁类的对象（相当于有4只大雁）
list1=[]
for i in range(4):
    list1.append(Geese())
print("一共有"+str(Geese.number)+"只大雁")

Geese.beak="喙的基部较高，长度和头部的长度几乎相等"   #添加类属性
print("第二只大雁的喙：",list1[1].beak)             #访问类属性