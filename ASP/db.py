import pymysql

connection = pymysql.connect(host="localhost", user="root", password="", database="asp_base")
conn = connection.cursor()

print(connection)