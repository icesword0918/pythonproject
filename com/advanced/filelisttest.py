# os和os.path模块
import os
print(os.name)  # 获取操作系统类型
print(os.linesep)   # 获取当前操作系统上的换行符
print(os.sep)  # 获取当前操作系统的路径分隔符

# 路径
print(os.getcwd())  # 输出当前目录
print(os.path.abspath("message.txt")) # 输出绝对路径
print(os.path.join("D:\pythonspace\pythonproject","com\\advanced\message.txt"))  # 拼接字符串

# 判断目录是否存在
print(os.path.exists("C:\\demo"))   # 判断目录是否存在
print(os.path.exists("D:\pythonspace\pythonproject\com\\advanced\message.txt"))   # 判断文件是否存在

# 创建目录
path="D:\\demo"   # 指定要创建的目录
if not os.path.exists(path):   # 判断目录是否存在
    os.mkdir(path)   # 创建目录
    print("目录创建成功！")
else:
    print("该目录已经存在！")

# os.makedirs("D:\\demo\\test\\dir\\mr")  #创建多级目录
path="D:\\demo\\test\\dir\\mr"  # 指定要创建的目录
if not os.path.exists(path):   # 判断目录是否存在
    os.makedirs(path)   # 创建目录
    print("目录创建成功！")
else:
    print("该目录已经存在！")

# 删除目录
path1="D:\\demo\\test\\dir\\mr"   # 指定要创建的目录
if os.path.exists(path1):   # 判断目录是否存在
    os.rmdir(path1)   # 删除目录
    print("目录删除成功！")
else:
    print("该目录不存在！")

# 遍历目录
path2="D:\\pythonspace\\pythonproject\\com"
print("【",path,"】目录下报货文件和目录：")
for root,dirs,files, in os.walk(path2,topdown=True):
    for name in dirs:
        print("●",os.path.join(root,name))
    for name in files:             # 循环输出遍历到的文件
        print("o"),os.path.join(root,name)
