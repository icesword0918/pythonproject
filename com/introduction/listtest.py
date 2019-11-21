import random
string = list(range(10, 20, 2))
print(string)

team = ["火箭", "勇士", "开拓者", "雷霆", "爵士", "公牛", "马刺", "森林狼"]
for index, item in enumerate(team):
    if index % 2 == 0:
        print(item + "\t\t", end=' ')
    else:
        print(item + "\n")

phone=["三星","小米","oppo","vivo"]
len(phone)
phone.append("华为")    # 插入一个新的元素
len(phone)
print(phone)

newphone=["锤子","苹果","诺基亚"]
phone.extend(newphone)  # 插入一个新的列表
print(phone)

phone[7]="联想"  # 修改一个元素
print(phone)

del phone[7]    # 删除一个元素
print(phone)

value="锤子"
if phone.count(value)>0:
    phone.remove(value)
print(phone)

phone.append("华为")
num=phone.count("华为")    # 显示元素出现的次数
print(num)

position=phone.index("小米")       # 显示元素的下角标
print(position)

grade=[98,87,100,89,92,97,95,94]
total=sum(grade)                     # 列表求和
print("语文的总分数为：",total)

print("原顺序：",grade)
grade.sort()                   # 升序
print("升序",grade)
grade.sort(reverse=True)      # 降序
print("降序",grade)

newgrade=[98,87,100,89,92,97,95,94]
grade_as=sorted(newgrade)
print("升序",grade_as)
grade_des=sorted(newgrade,reverse=True)
print("降序",grade_des)
print("原序列",newgrade)

randomnumber=[random.randint(10,100) for i in range(10)]
print("生成的随机数为：",randomnumber)

price=[1200,5894,2345,8986,2356,9874,7653]
sale=[int(x*0.5) for x in price]
print("原价格：",price)
print("打五折价格：",sale)

newsale=[x for x in price if x>5000]
print("原价格：",price)
print("大于5000的价格：",newsale)