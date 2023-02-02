"""
1、导包
2、建立连接
3、获取游标
4、执行sql语句
5、获取结果
6、关闭游标
7、关闭连接
"""
import pymysql

conn = pymysql.connect(host="localhost", port=3306, user="root",
                password="bear525999", charset="utf8",
                       autocommit=True)
cursor = conn.cursor()
cursor.execute("select version()")  # 查看当前MySQL版本

res = cursor.fetchone()
print(res[0])
cursor.close()
conn.close()