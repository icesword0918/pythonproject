# StaticText文本类
# TextCtrl输入文本类
# Button 按钮类

# _*_ conding:utf-8 _*_
import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="创建TextCtrl类",size=(400,300))
        # 创建面板
        panel=wx.Panel(self)
        # 创建文本和输入框
        self.title=wx.StaticText(panel,label="请输入用户名和密码",pos=(140,20))
        self.label_user=wx.StaticText(panel,label="用户名:",pos=(50,50))
        self.text_uesr=wx.TextCtrl(panel,pos=(100,50),size=(235,25),style=(wx.TE_LEFT))
        self.label_pwd=wx.StaticText(panel,label="密  码:",pos=(50,90))
        self.text_password=wx.TextCtrl(panel,pos=(100,90),size=(235,25),style=wx.TE_PASSWORD)
        # 创建“确定”和“取消”按钮
        self.bt_confirm=wx.Button(panel,label="确定",pos=(105,130))
        self.bt_cancel=wx.Button(panel,label="取消",pos=(205,130))

if __name__=='__main__':
    app=wx.App()
    frame=MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()