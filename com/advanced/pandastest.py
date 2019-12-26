import pandas as pd
# Series数据结构
S1=pd.Series(["a","b","c","d"])
print(S1)
print(S1.index)
print(S1.values)

# DataFrame表格型数据结构
df1=pd.DataFrame(["a","b","c","d"])
print(df1)
df2=pd.DataFrame([["a","A"],["b","B"],["c","C"],["d","D"]],columns=["小写","大写"])
print(df2)
print(df2.index)


#导入.xlsx文件
df=pd.read_excel(r"D:\pythonspace\test.xlsx",sheet_name="Sheet1")
print(df)  # 展示数据
print(df.head(2))  # 预览前几行数据
print(df.shape)  # 数据表的大小
print(df.info())  # 获取数据类型
print(df.describe()) # 数值类型字段的分布值
print(df.isnull)  # 判断哪个值是缺失值
print(df.dropna())  # 默认删除含有缺失值的行
print(df.dropna(how ="all"))  # 删除空白行
print(df.fillna({"性别":"男"}))  # 缺失值进行填充
print(df.drop_duplicates())  # 删除重复数据
print(df.drop_duplicates(subset="性别"))  # 某一列或某几列进行重复值删除的判断
print(df.drop_duplicates(keep="first")) # 保留第一个重复数据
print(df.drop_duplicates(keep="last"))  # 保留最后一个重复数据
print(df.drop_duplicates(keep=False))  # 删除所有重复数据
print(df["性别"].dtype)  # 获取某一列的数据类型
print(df["年龄"].astype("float64"))  # 数据类型进行转换
print(df.set_index("编号"))  # 重置索引值

df3=pd.read_excel(r"D:\pythonspace\test.xlsx",sheet_name="Sheet2")
print(df3)
print(df3.reset_index()) # 默认将index全部转化为colums
print(df3.reset_index(level=0))
print(df3.reset_index(drop=True))