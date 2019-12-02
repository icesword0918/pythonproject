# 了解形式参数与实际参数
def fun_bmi(person, height, weight):
    """功能：根据身高和体重计算BMI指数

    :param person:姓名
    :param height:身高，单位：米
    :param weight:体重，单位：千克
    :return:
    """
    print(person + "的身高：" + str(height) + "米\t体重：" + str(weight) + "千克")
    bmi = weight / (height * height)
    print("您的BMI指数为：" + str(bmi))
    # 判断身材是否合理
    if bmi < 18.5:
        print("您的体重过轻")
    if 18.5 <= bmi < 24.9:
        print("正常范围，注意保持")
    if 24.5 <= bmi < 29.9:
        print("您的体重过重")
    if bmi >= 29.9:
        print("肥胖")


# **************************************** #
fun_bmi("路人甲", 1.83, 60)
fun_bmi("路人乙", 1.60, 50)

# 位置参数
print()
fun_bmi("路人甲", 60, 1.83)
print()

# 关键字参数
fun_bmi(height=1.83,weight=60,person="路人甲")

# 为参数设置默认值
def demo(obj=None):
    if obj==None:
        obj=[]
    print("obj的值：",obj)
    obj.append(1)

# ******************************* #
print()
demo()
demo()

#可变参数
def fun_bmi_upgrade(*person):
    """
    功能：根据身高和体重计算BMI指数（共享升级版）
    :param person: 可变参数改参数中需要传递3个元素的列表，分别为姓名，身高（单位：米）和体重（单位：千克）
    :return:
    """
    for list_person in person:
        for item in list_person:
            person=item[0]
            height=item[1]
            weight=item[2]
            print("\n"+"="*13,person,"="*13)
            print("身高：" + str(height) + "米\t体重：" + str(weight) + "千克")
            bmi = weight / (height * height)
            print("您的BMI指数为：" + str(bmi))
            # 判断身材是否合理
            if bmi < 18.5:
                print("您的体重过轻")
            if 18.5 <= bmi < 24.9:
                print("正常范围，注意保持")
            if 24.5 <= bmi < 29.9:
                print("您的体重过重")
            if bmi >= 29.9:
                print("肥胖")

# ******************************************* #
list_w=[('绮梦',1.70,65),('零语',1.78,50),('黛兰',1.72,66)]
list_m=[('梓轩',1.80,75),('冷伊一',1.75,70)]
fun_bmi_upgrade(list_w,list_m)

def printsign(**sign):
    print()
    for key,value in sign.items():
        print("["+key+"]的星座是："+value)

# ************************************************** #
printsign(绮梦='水瓶座',冷伊一='射手座')

dict1={'绮梦':'水瓶座','冷伊一':'射手座','香凝':'双鱼座'}
#dict1={'绮梦':'水瓶座','冷伊一':'射手座','香凝':'双鱼座'}
printsign(**dict1)
