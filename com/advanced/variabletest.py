# 局部变量
def f_demo():
    message='唯有在被追赶的时候，你才能真正的奔跑。'
    print('局部变量message=',message)
f_demo()
# print('局部变量message=',message)  #在函数体外输出局部变量的值

# 全局变量
message = '唯有在被追赶的时候，你才能真正的奔跑。'  # 全局变量
def f_demo1():
    print('局部变量message=',message)
f_demo1()
print('局部变量message=',message)

message = '唯有在被追赶的时候，你才能真正的奔跑。'  # 全局变量
def f_demo2():
    message='命运给予我们的不是失望之酒，而是机会之杯。'    # 局部变量
    print('局部变量message=',message)
f_demo2()
print('局部变量message=',message)

message = '唯有在被追赶的时候，你才能真正的奔跑。'  # 全局变量
def f_demo3():
    global  message
    message='命运给予我们的不是失望之酒，而是机会之杯。'    # 局部变量
    print('局部变量message=',message)
f_demo3()
print('局部变量message=',message)