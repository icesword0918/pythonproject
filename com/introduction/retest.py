import re
# 匹配字符串
pattern=r'mr_\w+'
string='MR_SHOP mr_shop'
match=re.match(pattern,string,re.I)
print(match)
print('匹配值的起始位置：',match.start())
print('匹配值的结束位置：',match.end())
print('匹配值位置的元组：',match.span())
print('匹配值的字符串：',match.string)
print('匹配数据：',match.group())
string='项目名称MR_SHOP mr_shop'
match=re.match(pattern,string,re.I)
print(match)

pattern1=r'mr_\w+'
string1='MR_SHOP mr_shop'
match1=re.search(pattern1,string1,re.I)
print(match1)
string1='项目名称MR_SHOP mr_shop'
match1=re.search(pattern1,string1,re.I)
print(match1)

pattern2=r'mr_\w+'
string2='MR_SHOP mr_shop'
match2=re.findall(pattern2,string2,re.I)
print(match2)
string2='项目名称MR_SHOP mr_shop'
match2=re.findall(pattern2,string2,re.I)
print(match2)

# 替换字符串
pattern3=r'1[34578]\d{9}'
string3='中奖号码为84978981 联系电话为13611111111'
result=re.sub(pattern3,'1XXXXXXXXX',string3)
print(result)

# 使用正则表达式分割字符串
pattern4=r'[?|&]'
url='http://www.mingrisfot.com/logon.jsp?username="mr"&pwd=mrsoft'
result1=re.split(pattern4,url)
print(result1)