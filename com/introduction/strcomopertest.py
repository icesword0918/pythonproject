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