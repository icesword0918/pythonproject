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

# 实例属性
class Geese:
    """大雁类"""
    def __init__(self):
        self.neck="脖子较长"
        self.wing="振翅频率高"
        self.leg="腿位于身体的中心支点，行走自如"
        print("我属于雁类，我有以下的特征：")
        print(self.neck)
        print(self.wing)
        print(self.leg)

geese=Geese()


goose1=Geese()
goose2=Geese()
print()
goose1.neck="脖子没有天鹅的长"
print("goose1的neck属性：",goose1.neck)
print("goose2的neck属性：",goose2.neck)


# 访问限制
class Swan:
    """天鹅类"""
    _neck_swan="天鹅的脖子很长"          # 定义保护属性
    def __init__(self):
        print("_init_():",Swan._neck_swan)   # 在实例方法中访问保护属性
swan=Swan()                                  # 创建Swan类的实例
print("直接访问：",swan._neck_swan)          # 保护属性可以通过实例名访问

class Swan:
    """天鹅类"""
    __neck_swan="天鹅的脖子很长"          # 定义私有属性
    def __init__(self):
        print("_init_():",Swan.__neck_swan)   # 在实例方法中访问私有属性
swan=Swan()                                  # 创建Swan类的实例
print("加入类名：",swan._Swan__neck_swan)          # 私有属性，可以通过“实例名._类名__xxx”方式访问
print("直接访问：",swan.__neck_swan)               # 私有属性不能通过实例名访问，出错