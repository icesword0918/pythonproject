# 拼接字符串
str1='我今天一共走了'
num=12098
str2='步'
print(str1+str(num)+str2)
print("")

# 计算字符串的长度
str3='人生苦短，我用python!'
print(len(str3))                # 不区分
print(len(str3.encode()))       # 计算UTF-8编码的字符串的长度
print(len(str3.encode('gbk')))  # 计算GBK编码的字符串长度

# 截取字符串
substr1=str3[1]
substr2=str3[5:]
substr3=str3[:5]
substr4=str3[2:5]
print(substr1+'\n'+substr2+'\n'+substr3+'\n'+substr4)

# 分割、合并字符串
str4='明 日 学 院 官 网 >>> www.mingrisoft.com'
print('原字符串：'+str4)
list1=str4.split()                  # 采用默认分隔符进行分割
list2=str4.split('>>>')             # 采用多个字符进行分割
list3=str4.split('.')               # 采用.号进行分割
list4=str4.split(' ',4)             # 采用空格进行分割，并且值分割前4个
list5=str4.split('>')               # 采用》进行分割
print(str(list1)+'\n'+str(list2)+'\n'+str(list3)+'\n'+str(list4)+'\n'+str(list5))

list_friend=['明日科技','扎克伯格','俞敏洪','马云','马化腾','丁磊']
str_friend='@'.join(list_friend)
at='@'+str_friend
print('您要@的好友为：'+at)

# 检索字符串
str5='@明日科技@扎克伯格@俞敏洪@马云@马化腾@丁磊'
print('字符串包含',str5.count('@'),'个@符号')                      # 使用count查询个数
print('字符串中@斧蛤首次出现的位置索引为：',str5.find('@'))         # 使用find查询字符串出现的索引
print('字符串中@斧蛤首次出现的位置索引为：',str5.index('@'))        # 使用index查询字符串出现的索引，不存在抛异常
print('判断字符串是否以@符号开头，结果为：',str5.startswith('@'))   # 使用startswith查询字符串是否以符号开头
print('判断字符串是否以“磊”结尾，结果为：',str5.endswith("磊"))     # 使用endswith查询字符串是否以符号结尾

# 字母的大小写转换
str6='WWWW.Mingrisoft.com'
print('原字符串：',str6)
print('转换小写为：',str6.lower())
print('转换大写为：',str6.upper())

# 去除字符串中的空格和特殊字符
str7=' http://www.mingrisoft.com \t\n\r'
print('原字符串：'+str7+'。')
print('字符串:'+str7.strip()+'。')
str8='@明日科技.@.'
print('原字符串：'+str8+'。')
print('字符串:'+str8.strip('@.')+'。')

# 格式化字符串
template='编号：%09d\t公司名称： %s \t官网： http://www.%s.com'
context1=(7,'百度','baidu')
context2=(8,'明日学院','mingrisoft')
print(template%context1)
print(template%context2)

template1='编号：{:0>9s}\t公司名称： {:s}\t官网： http://www.{:s}.com'
context3=template1.format('7','百度','baidu')
context4=template1.format('8','明日学院','mingrisoft')
print(context3)
print(context4)