import pymysql
import datetime as dt

db = "asp_base"
host = "localhost"
user = "root"
passwd = ""

connection = pymysql.connect(host=host, user=user, passwd=passwd, db=db)
conn = connection.cursor()


date = dt.datetime.now().strftime("%Y-%m-%d")
# print(date)


def convert_time(date):
    date = dt.datetime.strptime(date, "%Y-%m-%d")
    return date


def convertTuple(tup):
    st = "".join(tup)
    return st


def Check_Data():
    sql = "select date from tb_attandance where date='" + date + "' limit 1"
    conn.execute(sql)
    result = conn.fetchall()
    return result


def get_date():
    my_data = Check_Data()
    if my_data:
        # print("Data is already in database")
        return str(my_data[0][0])
    else:
        # print("Data is not in database")
        my_data = dt.date(2022, 1, 1)
        return str(my_data)


# my_data = ((dt.date(2022, 1, 1),),)
my_data = get_date()
# print(my_data)

if my_data != date:
    print("Data is not in database", my_data)
else:
    print("Data is already in database", my_data)
