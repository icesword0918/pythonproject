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
