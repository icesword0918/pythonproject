# 继承的基本语法
class Fruit:  # 定义水果类（基类）
    color = "绿色"  # 定义类属性

    def harvest(self, color):
        print("水果是：" + color + "的！")  # 输出的是形式参数color
        print("水果已经收获......")
        print("水果原来是：" + Fruit.color + "的！")  # 输出的是类属性color


class Apple(Fruit):  # 定义苹果类（派生类）
    color = "红色"

    def __init__(self):
        print("我是苹果")


class Orange(Fruit):
    color = "橙色"

    def __init__(self):
        print("\n我是橘子")


apple = Apple()  # 创建类的实例（苹果）
apple.harvest(apple.color)  # 调用基类的harvest()方法
orange = Orange()  # 创建类的实例（橘子）
orange.harvest(orange.color)  # 调用基类的harves() 方法


# 方法重写
class Orange(Fruit):
    color = "橙色"

    def __init__(self):
        print("\n我是橘子")

    def harvest(self, color):
        print("橘子是：" + color + "的！")  # 输出的是形式参数color
        print("橘子已经收获......")
        print("橘子原来是：" + Fruit.color + "的！")  # 输出的是类属性color


orange = Orange()  # 创建类的实例（橘子）
orange.harvest(orange.color)  # 调用基类的harves() 方法


# 派生类中调用基类的__init__()方法
class Fruit:
    def __init__(self, color="绿色"):
        Fruit.color = color

    def harvest(self):
        print("水果原来是：" + Fruit.color + "的！")


class Apple(Fruit):
    def __init__(self):
        print("我是苹果")
        super().__init__()  # 调用基类的__init__()方法


apple = Apple()
apple.harvest()

class FruitTest:
    def __init__(self,color="绿色"):
        FruitTest.color=color
    def harvest(self, color):
        print("水果是：" + color + "的！")  # 输出的是形式参数color
        print("水果已经收获......")
        print("水果原来是：" + FruitTest.color + "的！")  # 输出的是类属性color
class Apple(FruitTest):  # 定义苹果类（派生类）
    color = "红色"

    def __init__(self):
        print("我是苹果")
        super().__init__()
class Sapodilla(FruitTest):
    def __init__(self,color):
        print("\n我是人参果")
        super().__init__(color)
    def harvest(self, color):
        print("人参果是：" + color + "的！")  # 输出的是形式参数color
        print("人参果已经收获......")
        print("人参果原来是：" + FruitTest.color + "的！")  # 输出的是类属性color

apple=Apple()
apple.harvest(apple.color)
sapodilla=Sapodilla("白色")
sapodilla.harvest("金黄色带紫色条纹")