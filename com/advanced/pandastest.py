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

# 获取数据
#导入.xlsx文件
df=pd.read_excel(r"..\assets\test.xlsx",sheet_name="Sheet1")
print(df)  # 展示数据
print(df.head(2))  # 预览前几行数据
print(df.shape)  # 数据表的大小
print(df.info())  # 获取数据类型
print(df.describe()) # 数值类型字段的分布值

# 数据预处理
print(df.isnull())  # 判断哪个值是缺失值
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

df3=pd.read_excel(r"..\assets\test.xlsx",sheet_name="Sheet2")
print(df3)
print(df3.reset_index()) # 默认将index全部转化为colums
print(df3.reset_index(level=0))
print(df3.reset_index(drop=True))

# 数据选择
df4=pd.read_excel(r"..\assets\test.xlsx",sheet_name="Sheet3")
print(df4)
print(df4.iloc[:,[0,2]])  #获取第1列和第3列的数值
print(df4.iloc[:,0:3])  #获取第1列到第4列的数值
print(df4.loc[0])  # 选择1行
print(df4.loc[[0,1]])  # 选择1行和2行
print(df4.loc[0:2])  # 选择1行到3行
print(df4[df4["年龄"]<200])  # 选择年龄小于200的数据
print(df4.loc[[0,2],["订单编号","唯一识别码"]])   # 行列同时选择
print(df4.iloc[[0,1],[0,2]])  # 获取第一行，第二行和第一列、第三列数据
print(df4[df4["年龄"]<200][["订单编号","年龄"]])   # 布尔索引+普通索引
print(df4.iloc[0:3,1:3])  # 选择第一到第三行，第二列到第三列
# print(df4.ix[0:2,["客户姓名","唯一识别码"]])

# 数值操作
print(df4["年龄"].replace(240,33))  # 对某个值进行替换
print(df4["年龄"].replace([240,260],33))  # 对某几个值进行替换
print(df4["年龄"].replace({240:32,260:33}))  # 实现多对多的替换
print(df4.sort_values(by=["销售ID"]))  # 按照销售ID升序排列
print(df4.sort_values(by=["销售ID"],ascending=False))  # 按照销售ID降序排列
print(df4.sort_values(by=["销售ID"],na_position="first"))  # 将缺失值显示在最前面
print(df4.sort_values(by=["销售ID","成交时间"],ascending=[True,False]))  # 先按照销售ID升序排列，再按成交时间降序排列
print(df4["销售ID"].rank(method="average"))  # Excel中RANK.AVG函数的一致
print(df4["销售ID"].rank(method="first"))   # 销售ID为1的值有两个，第一个出现的排名为1，第二个出现的排名为2
print(df4["销售ID"].rank(method="min"))  # Excel中RANK.EQ函数的一致
print(df4["销售ID"].rank(method="max"))  # 与method取值min时相反
print(df4.drop(["销售ID","成交时间"],axis=1))   #待删除列的列名，加一个参数axis=1，表示删除列
print(df4.drop([1,2],axis=0))   #待删除行的行号，加一个参数axis=0，表示删除行
print(df4["销售ID"].value_counts())   # 对某些值的出现次数进行计数
print(df4["销售ID"].value_counts(normalize=True))  # 不同值出现的占比
print(df4["销售ID"].value_counts(normalize=True,sort=False))  # 不按计数值降序排列
print(df4["销售ID"].unique())   # 取唯一值
print(df4["年龄"].isin([45,23]))  # 查看数据表中是否包含某个值
# print(pd.cut(df4["年龄"],3,bins=[24,36,46,241]))
print(pd.qcut(df4["年龄"],3))  # 把待切分数据切成几份
print(df4.insert(2,"商品类别",["cat01","cat02","cat03","cat04","cat05"]))  # 插入的位置、插入后新列的列名，以及要插入的数据
print(df4)
print(df4.T)  # 行列互换（转置）
print(df4["年龄"].apply(lambda x:x+1))  # 某一column或row中的元素执 行相同的函数操作
# print(df3.applymap(lambda x:x+1))  # 每一个元素执行相同的函数操作

# 数据运算
df5=pd.read_excel(r"..\assets\test.xlsx",sheet_name="Sheet4")
print(df5["C1"]+df5["C2"])  # 两列相加
print(df5["C1"]-df5["C2"])  # 两列相减
print(df5["C1"]*df5["C2"])  # 两列相乘
print(df5["C1"]/df5["C2"])  # 两列相除
print(df5["C1"]+2)   # 列与常数加减乘除
print(df5["C1"]-2)
print(df5["C1"]*2)
print(df5["C1"]/2)
print(df5["C1"]>df5["C2"])   # 比较运算
print(df5["C1"]!=df5["C2"])
print(df5.count())   # 每列的非空值的个数
print(df5.count(axis=1))  # 每一行的非空数值的个数
print(df5.sum())   # 每列的求和结果
print(df5.sum(axis=1))  # 每行的求和结果
print(df5.mean())   # 每列的平均值
print(df5.mean(axis=1))  # 每行的平均值
print(df5.max())   # 每列的最大值
print(df5.max(axis=1))  # 每行的最大值
print(df5.min())   # 每列的最小值
print(df5.min(axis=1))  # 每行的最小值
print(df5.median())   # 每列的中位数
print(df5.median(axis=1))  # 每行的中位数
# print(df5.mode())   # 每列的众数
# print(df5.mode(axis=1))  # 每行的众数
print(df5.var())   # 每列的方差
print(df5.var(axis=1))  # 每行的方差
print(df5.std())   # 每列的标准差
print(df5.std(axis=1))  # 每行的标准差
print(df5.quantile(0.25))   # 每列的4分之一分位数
print(df5.quantile(0.25,axis=1))  # 每行的4分之一分位数
print(df5.corr())  # 表中各字段两两之间的相关性
print(df5["C1"].corr(df5["C2"]))  # c1列与c2列之间的相关性


# 时间序列
from datetime import datetime
print(datetime.now())  # 显示当前的日期和时间
print(datetime.now().year)  # 返回当前时刻的年
print(datetime.now().month)  # 返回当前时刻的月
print(datetime.now().day)  # 返回当前时刻的日
print(datetime.now().weekday()+1)  # 返回当前周几
print(datetime.now().isocalendar())  # 返回当前时刻所在周数
print(datetime.now().date())  # 返回当前时间只展示日期
print(datetime.now().time())  # 返回当前时间只展示时间
