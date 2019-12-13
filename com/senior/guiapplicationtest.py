# 创建一个wx.app的子类
# -*- coding:utf-8 -*-
import wx    # 导入wyPython
"""
class App(wx.App):
    # 初始化方法
    def OnInit(self):
        frame=wx.Frame(parent=None,title='Hello wyPython')   # 创建窗口
        frame.Show()    # 显示窗口
        return True     # 返回值
if __name__=='__main__':
    app=App()  # 创建app类的实例
    app.MainLoop()   # 调用app类的MainLoop()主循环方法
"""
# 直接使用wx.App
"""
app=wx.App()
frame=wx.Frame(None,title='Hello wyPython')
frame.Show()
app.MainLoop()
app.MainLoop()
"""
# 使用wx.Frame框架
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="创建Frame",pos=(100,100),size=(300,300))

if __name__=='__main__':
    app=wx.App()    # 初始化应用
    frame=MyFrame(parent=None,id=-1)   # 实例MyFrame类，并传递参数
    frame.Show()    # 显示窗口
    app.MainLoop()  #  调用MainLoop()主循环方法