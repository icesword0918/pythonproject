# s使用encode()方法编码
verse='野渡无人舟自横'
byte=verse.encode('GBK')
print('原字符串：',verse)
print("转换后：",byte)
byte1=verse.encode('UTF-8')
print(byte1)

# 使用decode()方法解码
print('解码后：',byte.decode('GBK'))
print('解码后：',byte1.decode('UTF-8'))