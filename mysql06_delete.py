"""
删除扁鹊那条数据
delete from students where name ='扁鹊';
导包--创建连接--执行insert
提交/回滚事务--关闭游标、连接
加上异常处理
"""
import pymysql
# 设置全局变量
conn = None
cursor = None

try:
    conn = pymysql.connect(host="localhost", port=3306, user="root",
                           password="bear525999", database="test", charset="utf8")
    cursor = conn.cursor()
    cursor.execute(
        "delete from students where name ='扁鹊';")
    # 查看sql执行 影响多少行 conn.affected_rows()
    print("影响的行数：", conn.affected_rows())
    # 提交事务
    conn.commit()
except Exception as e:
    # 出错 回滚事务
    print("执行出错：",e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()







