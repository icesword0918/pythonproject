from com.advanced.custemsettingtest import *  # 导入custemsettingtest模块下的所有函数
if __name__=='__main__':           # 注意main前后是双下划线
    change(1024,768)               # 调用change()函数改变尺寸
    print("宽度：",getWidth())     # 输出宽度
    print("高度：",getHight())     # 输出高度