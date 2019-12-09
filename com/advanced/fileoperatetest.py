# 创建和打开文件
print("\n","="*10,"蚂蚁庄园动态","="*10)
file=open('message.txt','w')   # 创建或打开保存蚂蚁庄园动态信息的文件
print("\n 即将显示......\n")

# 关闭文件
file.close()

# 打开文件时使用with语句
print("\n","="*10,"蚂蚁庄园动态","="*10)
with open('message.txt','w') as file:  # 创建或打开保存蚂蚁庄园动态信息的文件
     pass
print("\n 即将显示......\n")
file.close()

# 写入文件内容
print("\n","="*10,"蚂蚁庄园动态","="*10)
file=open('message.txt','w')   # 创建或打开保存蚂蚁庄园动态信息的文件
file.write("你使用了1张加速卡，小鸡撸起袖子开始双手吃饲料，进食速度大大加快。\n")
print("\n 写入了一条动态......\n")
file.close()

print("\n","="*10,"蚂蚁庄园动态","="*10)
file=open('message.txt','a')   # 创建或打开保存蚂蚁庄园动态信息的文件
file.write("mingri的小鸡在你的庄园呆了22分钟，吃了6g饲料之后，被你赶走了。\n")
print("\n 追加了一条动态......\n")
file.close()

# 读取文件
# 读取全部
print("\n","="*20,"蚂蚁庄园动态","="*20)
with open('message.txt','r') as file:
    message=file.read()   # 读取全部动态信息
    print(message)
    print("\n","="*20,"over","="*20,"\n")

# 读取一行
print("\n","="*20,"蚂蚁庄园动态","="*20)
with open('message.txt','r') as file:
    number=0
    while True:
        number+=1
        line=file.readline()
        if line=='':
            break
        print(number,line,end="\n")
    print("\n","="*20,"over","="*20,"\n")

# 读取全部的行
print("\n","="*20,"蚂蚁庄园动态","="*20)
with open('message.txt','r') as file:
    message=file.readlines()   # 读取全部动态信息
    print(message)
    print("\n","="*20,"over","="*20,"\n")

print("\n","="*20,"蚂蚁庄园动态","="*20)
with open('message.txt','r') as file:
    messageall=file.readlines()   # 读取全部动态信息
    for message in messageall:
         print(message)          # 输出一条动态信息
print("\n","="*20,"over","="*20,"\n")