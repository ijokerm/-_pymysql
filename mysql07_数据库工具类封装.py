import pymysql

# 数据库工具类的封装
class DBUtil(object):
    # 添加类属性
    conn = None

    # 创建/关闭连接 --私有方法
    @classmethod
    def __get_conn(cls):
        # 连接只需要建立一次
        if cls.conn == None:
            cls.conn = pymysql.connect(host="localhost", port=3306, user="root",
                        database="test", password="bear525999", charset="utf8")

        return cls.conn

    @classmethod
    def __close_conn(cls):
        if cls.conn is not None:
            cls.conn.close()
            cls.conn = None
    # 常用方法 --查询
    @classmethod
    def select_one(cls,sql):
        cursor = None
        res = None
        try:
            # 获取连接
            cls.conn = cls.__get_conn()
            # 获取游标
            cursor = cls.conn.cursor()
            # 执行语句
            cursor.execute(sql)
            # 提取一条结果
            res = cursor.fetchone()
        except Exception as e:
            print("查询错误：",e)
        finally:
            # 关闭游标/连接
            cursor.close()

            cls.__close_conn()
            return res

    # 常用方法 --增删改
    @classmethod
    def uid_db(cls,sql):
        cursor = None
        res = None
        try:
            # 获取连接
            cls.conn = cls.__get_conn()
            # 获取游标
            cursor = cls.conn.cursor()
            # 执行语句
            cursor.execute(sql)
            # 提取一条结果
            res = cursor.fetchone()
            print("影响的行数：",cls.conn.affected_rows())
            cls.conn.commit()
        except Exception as e:
            cls.conn.rollback()
            print("执行错误：", e)
        finally:
            # 关闭游标/连接
            cursor.close()
            cls.__close_conn()


if __name__ == '__main__':
    test = DBUtil()
    res = test.select_one("select * from students")
    t2 = DBUtil.select_one("select * from students")
    print(t2)
    # DBUtil.u vbid_db("update students set hometown = '四川' where name = '诸葛亮';")