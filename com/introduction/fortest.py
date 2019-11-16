print("计算1-100之和：")
result = 0
for i in range(101):
    result += i
print(result)

print("输出for循环的值：")
for i in range(1, 10):
    print(i, end=' ')

print("\n输出for循环中步长的值：")
for i in range(1, 20, 3):
    print(i, end=' ')

print("\n今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？")
for number in range(100):
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print("答曰：这个数是", number)

string = '不要说我不能'
print(string)
for i in string:
    print(i)
