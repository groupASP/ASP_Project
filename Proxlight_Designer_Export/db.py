import pymysql
import mysql.connector

connection = pymysql.connect(host="localhost", user="root", password="", database="asp_base")
conn = connection.cursor()


def getAll(tb_name):
    sql = "select * from "+tb_name
    return conn.execute(sql)


