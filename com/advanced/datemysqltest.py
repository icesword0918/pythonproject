# 连接数据库
import pymysql

# 打开数据库连接，参数1:主机名活IP；参数2：用户名；参数3：密码；参数4：数据库名称
db=pymysql.connect('152.136.194.98','root','Admin_0820!','test')
# 使用cursor()方法创建一个游标对象cursor
cursor=db.cursor()
# 使用execute()方法执行SQL查询
cursor.execute('select version()')
# 使用fetchone()方法获取单条数据
data=cursor.fetchone()
print("Database version: %s"%data)
# 关闭数据库连接
db.close()


# 打开数据库连接，参数1:主机名活IP；参数2：用户名；参数3：密码；参数4：数据库名称
db=pymysql.connect('152.136.194.98','root','Admin_0820!','test')
# 使用cursor()方法创建一个游标对象cursor
cursor=db.cursor()
# 数据列表
data=[('零基础学Python','Python','79.80','2018-5-20'),
      ('Python从入门到精通','Python','69.80','2018-6-18'),
      ('零基础学PHP','PHP','69.80','2017-5-21'),
      ('PHP项目开发实战入门','PHP','79.80','2016-5-21'),
      ('零基础学Java','Java','69.80','2017-5-21'),]
try:
    # 执行sql语句，插入多条数据
    cursor.executemany("insert into books(name,category,price,publish_time) values (%s,%s,%s,%s)",data)
    # 提交数据
    db.commit()
    print("数据提交成功！")
except:
    # 发生错误回滚
    db.rollback()
    print("数据提交失败，回滚操作。")
# 关闭数据库连接
db.close()
