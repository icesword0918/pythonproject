# 使用BoxSizer布局

# _*_ conding:utf-8 _*_
import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, title="用户登录", size=(400, 300))
        # 创建面板
        panel = wx.Panel(self)
        # 创建“确定”和“取消”按钮，并绑定事件
        self.bt_confirm = wx.Button(panel, label="确定")
        self.bt_confirm.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label="取消")
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
        # 创建文本，左对齐
        self.title = wx.StaticText(panel, label="请输入用户名和密码")
        self.label_user=wx.StaticText(panel,label="用户名:")
        self.text_uesr=wx.TextCtrl(panel,style=(wx.TE_LEFT))
        self.label_pwd=wx.StaticText(panel,label="密   码:")
        self.text_password=wx.TextCtrl(panel,style=wx.TE_PASSWORD)
        # 添加容器，容器中空间横向排列
        hsizer_user=wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user,proportion=0,flag=wx.ALL,border=5)
        hsizer_user.Add(self.text_uesr,proportion=1,flag=wx.ALL, border=5)
        hsizer_pwd=wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd,proportion=0,flag=wx.ALL,border=5)
        hsizer_pwd.Add(self.text_password, proportion=1, flag=wx.ALL, border=5)
        hsizer_button=wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm,proportion=0,flag=wx.ALIGN_CENTER,border=5)
        hsizer_button.Add(self.bt_cancel, proportion=1, flag=wx.ALIGN_CENTER, border=5)
        # 添加容器，容器中空间按纵向排列
        vsizer_all=wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title,proportion=0,flag=wx.TOP|wx.ALIGN_CENTER,border=15)
        vsizer_all.Add(hsizer_user,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)
        vsizer_all.Add(hsizer_pwd, proportion=0,flag=wx.EXPAND | wx.LEFT |wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER|wx.TOP, border=15)
        panel.SetSizer(vsizer_all)

    # 点击函数
    def OnclickSubmit(self,event):
        """
        单击确定按钮，执行方法
        :param event:
        :return:
        """
        username=self.text_uesr.GetValue()  # 获取输入的用户名
        password=self.text_password.GetValue()  # 获取输入的密码
        if username=="" or password=="":
            message="用户名或密码不能为空"
        elif username=='mr' and password=='123':
            message="登录成功"
        else:
            message="用户名和密码不匹配"
        wx.MessageBox(message)  # 弹出提示框
    def OnclickCancel(self,event):
        """
        单击取消按钮，执行方法
        :param event:
        :return:
        """
        self.text_uesr.SetValue("")  # 清空输入的用户名
        self.text_password.SetValue("")  #  清空输入的密码

if __name__=='__main__':
    app=wx.App()
    frame=MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()