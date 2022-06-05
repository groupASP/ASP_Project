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

cl_Name = "HCS6B"
d_Name = "Friday"


def Insert_Student():
    cl_Id = "cl_HCS6B"
    d_Id = "d_Friday"
    r_Id = "r_309"
    connection = pymysql.connect(
        host="localhost", user="root", password="", database="asp_base"
    )
    conn = connection.cursor()
    sql = (
        "select st.st_Id, st.st_Name, st.st_Surname, d.d_Name, s.s_Name, r.r_Name, cl.cl_Name, sc.sc_Period, sc.sc_Year from \
        tb_schedule sc LEFT JOIN tb_class cl on sc.cl_Id=cl.cl_Id\
        INNER join tb_student st on st.cl_Id=cl.cl_Id\
        INNER JOIN tb_day d on d.d_Id=sc.d_Id\
        INNER JOIN tb_subject s on s.s_Id=sc.s_Id\
        INNER JOIN tb_room r on r.r_Id=sc.r_Id\
        where r.r_Id='"
        + r_Id
        + "' and cl.cl_Id='"
        + cl_Id
        + "' and d.d_Id='"
        + d_Id
        + "'"
    )
    conn.execute(sql)
    result = conn.fetchall()
    return result


profile = Insert_Student()

print(profile[0][3])
print(profile[0][6])


def convert_time(date):
    date = dt.datetime.strptime(date, "%Y-%m-%d")
    return date


def convertTuple(tup):
    st = ", ".join(map(str, tup))
    return st


def Check_Data():
    sql = (
        "select d_Name, cl_Name, date from tb_attandance where date='"
        + date
        + "' and cl_Name='"
        + str(cl_Name)
        + "' and d_Name='"
        + str(d_Name)
        + "'LIMIT 1"
    )
    conn.execute(sql)
    result = conn.fetchall()
    return result


def get_date():
    my_data = Check_Data()
    if my_data:
        # print("Data is already in database")
        day = str(my_data[0][0])
        clas = str(my_data[0][1])
        date = str(my_data[0][2])
        return day, clas, date
    else:
        # print("Data is not in database")
        my_day = ""
        my_class = ""
        my_data = dt.date(2022, 1, 1)
        return str(my_day), str(my_class), str(my_data)


data = Check_Data()
# print(data)

result = get_date()
# result = convertTuple(result)
print(result)

if result != (d_Name, cl_Name, date):
    print("Data is not in database")
    print(result)
else:
    print("Data is already in database")
    print(result)
