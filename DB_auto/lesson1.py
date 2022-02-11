#coding=utf-8
"""
Author:多测师_李立伏
time:2022-01-20 17:01
Wechat:xiaoshubass
website:www.duoceshi.cn
"""

import pymysql
class Db_utils(object):
    def __init__(self):
        self.host="192.168.93.128"
        self.user="root"
        self.password="654321"
        self.database="chengdu11"
        self.port=3306
    def get_connect(self):
        db=pymysql.connect(
                            host=self.host,
                            user=self.user,
                           password=self.password,
                           database=self.database,
                           port=self.port
        )
        cursor=db.cursor()
        return cursor
    def get_one(self):
        db1=self.get_connect()
        db1.execute("select * from emp;")
        one=db1.fetchone()
        print(one)
        return one

    def get_all(self,select_sql):
        cursor2=self.get_connect()
        cursor2.execute(select_sql)
        all=cursor2.fetchall()
        print(all)

    def del_sql(self):
        value1=self.get_one()
        cursor=self.get_connect()
        cursor.execute("delete from emp where sid=1568;")
        value2=self.get_one()
        if value1!=value2:
            print("删除成功！")
        else:
            print("删除失败")




if __name__ == '__main__':
    d=Db_utils()
    d.del_sql()

