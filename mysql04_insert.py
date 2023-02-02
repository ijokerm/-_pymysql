"""
新增一条数据（'013', '甄姬', '女', '北京', 33, '2班', '110101199003157666'）
insert into students(studentNo, name, sex,hometown,age,class,card) values('001', '王昭君', '女', '北京', 30, '1班', '110101199003157654');
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
        "insert into students(studentNo, name, sex,hometown,age,class,card) values('001', '王昭君', '女', '北京', 30, '1班', '110101199003157654');")
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







