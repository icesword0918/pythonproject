python={'绮梦','冷伊一','香凝','梓轩'}
c={'冷伊一','零语','梓轩','圣博'}
print('选择python语言的学生有：',python,'\n')
print('选择c语言的学生有：',c)

set1=set("命运给予我们的不是失望之酒，而是机会之杯")
set2=set([2,3,6,5,4,7,8,1,2,4,5])
print(set1)
print(set2)

python=set(['绮梦','冷伊一','香凝','梓轩'])
print('选择python语言的学生有：',python,'\n')
c=set(['冷伊一','零语','梓轩','圣博'])
print('选择c语言的学生有：',c)

python.add('零语')
c.remove('零语')
print('选择python语言的学生有：',python,'\n')
print('选择c语言的学生有：',c)

print('交集运算：',python&c)
print('并集运算：',python|c)
print('差集运算：',python-c)
