_width=800   # 定义保护类型的全局变量（宽度）
_hight=600   # 定义保护类型的全局变量（高度）
def change(w,h):
    global _width  # 全局变量（宽度）
    _width=w       # 重新给宽度赋值
    global _hight  # 全局变量（高度）
    _hight=h       # 重新给高度赋值
def getWidth():    # 获取宽度的函数
    global _width
    return _width
def getHight():    # 获取高度的函数
    global _hight
    return _hight
