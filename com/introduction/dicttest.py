name=['张三','李四','王五','刘七']
sign=['水瓶座','双子座','处女座','金牛座']
dictionary=dict(zip(name,sign))             # 转换为字典
print(dictionary)

dictionary_list=dict(张三='水瓶座', 李四='双子座', 王五='处女座', 刘七='金牛座')
print(dictionary_list)


dictionary_new=dict.fromkeys(name)
print(dictionary_new)

name_tuple=('张三','李四','王五','刘七')
dict_new={name_tuple:sign}
print(dict_new)

print(dictionary["李四"])
print("李四的星座是：",dictionary.get("李四","字典里没有这个人"))  # get方法获取值

for item in dictionary.items():
    print(item)

for key,value in dictionary.items():                            # 显示key与value
    print(key,"显示",value)

dictionary["马八"]="双鱼座"                                      # 添加一个字典值
print(dictionary)

dictionary["王五"]="摩羯座"                                      # 修改一个字典值
print(dictionary)

del dictionary["刘七"]                                          # 删除一个字典值
print(dictionary)