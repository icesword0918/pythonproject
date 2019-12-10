# 删除文件
import os
# os.remove("message.txt")
path="message.txt"
if os.path.exists(path):  # 判断文件是否存在
    os.remove(path)   # 删除文件
    print("文件删除完毕！")
else:
    print("文件不存在！")

# 重命名文件和目录
src="D:\\demo\\test\\dir"
dst="D:\\demo\\test\\mr"
#  os.rename(src,dst)
if os.path.exists(src):
    os.rename(src,dst)   # 重命名文件
    print("文件重命名完毕！")
else:
    print("文件不存在！")

# 获取文件的基本信息
def formatTime(longtime):
    """
    格式化日期时间的函数
    :param longtime: 要格式化的时间
    :return:
    """
    import time
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime((longtime)))
def formatByte(number):
    """
    格式化文件大小的函数
    :param number: 要格式化的字节数
    :return:
    """
    for (scale,label) in [(1024*1024*1024,"GB"),(1024*1024,"MB"),(1024,"KB")]:
        if number>=scale:
            return "%.2f %s"%(number*1.0/scale,label)
        elif number==1:
            return "1 字节"
        else:
            byte="%.2f"%(number or 0)
    # 去掉结尾的.00，并且加上单位“字节”
    return (byte[:-3] if byte.endswith('.00') else byte)+"字节"
if __name__=='__main__':
    fileinfo=os.stat("f:\\CSGO序列号.png")
    print("文件的完整路径：",os.path.abspath("f:\\CSGO序列号.png"))
    # 输出文件基本信息
    print("索引号:",fileinfo.st_ino)
    print("设备号：",fileinfo.st_dev)
    print("文件大写：",formatByte(fileinfo.st_size))
    print("最后一次访问时间：",formatTime(fileinfo.st_atime))
    print("最后一次修改时间",formatTime(fileinfo.st_mtime))
    print("最后一次状态变化时间：",formatTime(fileinfo.st_ctime))