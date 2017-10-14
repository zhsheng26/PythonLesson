import pymysql

db = pymysql.connect('localhost', 'root', '', 'timeuser')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
# 关闭数据库连接
db.close()
