height=1.70
print("您的身高："+str(height))
weight=88.5
print("您的体重："+str(weight))
bmi=weight/(height*height)
print("您的BMI指数为："+str(bmi))
#判断身材是否合理
if bmi<18.5:
    print("您的体重过轻")
if bmi>=18.5 and bmi<24.9:
    print("正常范围，注意保持")
if bmi>=24.5 and bmi<29.9:
    print("您的体重过重")
if bmi>=29.9:
    print("肥胖")