"""
演示异常捕获
"""
import pymysql

# 定义conn/cursor全局变量
conn = None
cursor = None

try:
    # 建立连接
    conn = pymysql.connect(host="localhost", port=3306, user="root",
                           password="bear525999", charset="utf8",
                           database="test", autocommit=True)
    # 创建游标
    cursor = conn.cursor()  # 初始指向0号位置
    cursor.execute("select * from students")  # 查看当前MySQL版本
    # 获取第一条结果
    res = cursor.fetchone()
    # 获取 前两条结果  --首先要修改游标位置
    cursor.rownumber = 0
    res1 = cursor.fetchmany(2)
    # 获取 全部数据   --还是要先回0 修改游标位置
    cursor.rownumber = 0
    res2 = cursor.fetchall()
    # 获取第三条和第四条 --首先要修改游标指向第二条
    cursor.rownumber = 2
    res3 = cursor.fetchmany(2)
    print(res2)
except Exception as e:
    print("执行查询出错：",e)
finally:
    cursor.close()
    conn.close()



