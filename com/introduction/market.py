print("\n手机店正在打折，活动进行中....")                  #提示信息
strWeek = input("请输入中文星期（如星期一）:")               #输入星期，例如：星期一
intTime = int(input("请输入时间中的小时（范围：0-23）："))   #输入时间
#判断是否满足活动参与条件（使用if判断语句）
if((strWeek == "星期二") and (intTime >= 10 and intTime <= 11)) or ((strWeek == "星期五") and (intTime >= 14 and intTime <= 15)):
    print("恭喜您，获取了折扣活动参与资格，快来选购吧！")
else:
    print("对不起，您来晚一步，期待下次活动......")