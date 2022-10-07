import pymysql
from pymysql.cursors import DictCursor


class DBHandler:

    def __init__(self,
                 host='',
                 port=3306,
                 user='',
                 password='',
                 # 不要写成utf-8
                 charset='utf8',
                 # 指定数据库
                 database='',
                 cursorclass=DictCursor
                 ):
        self.conn = pymysql.connect(host=host,
                               port=port,
                               user=user,
                               password=password,
                               # 不要写成utf-8
                               charset=charset,
                               # 指定数据库
                               database=database,
                               cursorclass=cursorclass)


    def query_one(self, sql):
        """数据库查询"""
        # 'SELECT * FROM futureloan.member LIMIT 10;'
        self.cursor = self.conn.cursor()
        # 事务提交
        self.conn.commit()
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        self.cursor.close()
        return data

    def query_all(self, sql):
        self.cursor = self.conn.cursor()
        # 事务提交
        self.conn.commit()
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        self.cursor.close()
        return data

    def query(self, sql, one=True):

        # self.cursor.execute(sql)
        if one:
            return self.query_one(sql)
        return self.query_all(sql)

    # def insert(self, sql):
    #     self.cursor.execute('insert')
    #     # 提交
    #     self.conn.commit()

    def close(self):
        # self.cursor.close()
        self.conn.close()


# if __name__ == '__main__':
#
#     """
#     host='8.129.91.152',
#                  port=3306,
#                  user='future',
#                  password='123456',
#                  # 不要写成utf-8
#                  charset='utf8',
#                  # 指定数据库
#                  database='futureloan',
#                  cursorclass=DictCursor
#     """
#
#
#     db = DBHandler(host='8.129.91.152',
#                  port=3306,
#                  user='future',
#                  password='123456',
#                  # 不要写成utf-8
#                  charset='utf8',
#                  # 指定数据库
#                  database='futureloan',
#                  cursorclass=DictCursor)
#     data = db.query('SELECT * FROM futureloan.member LIMIT 10;', one=False)
#     print(data)
#     db.close()