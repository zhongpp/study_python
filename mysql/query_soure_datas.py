#!/usr/bin/python3

import pymysql

# 打开数据库连接
# 数据库类型，用户，密码，数据库名称
db = pymysql.connect("mysql", "xx", "xx", "xx")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM tokens WHERE created_at < '%s'" % '2017-11-06 00:00:00'
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        print(row)
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" %
              (fname, lname, age, sex, income))
except Exception as exception:
    print("查询出现异常：%s" % exception)

# 关闭数据库连接
db.close()
