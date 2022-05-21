import pymysql
from datetime import *


# def getProfile(Id):
#     connection = pymysql.connect(
#         host="localhost", user="root", password="", database="asp_base"
#     )
#     conn = connection.cursor()
#     sql = (
#         "select st.st_Id, st.st_Name, st.st_Surname, d.d_Name, s.s_Name, \
#         r.r_Name, cl.cl_Name, sc.sc_Period, sc.sc_Year, f.Name, f.Surname, sc.start_Class, \
#         sc.end_Class \
#         from tb_face f inner join tb_student st on f.st_Id = st.st_Id\
#         inner join tb_class cl on st.cl_Id = cl.cl_Id\
#         inner join tb_schedule sc on sc.cl_Id=cl.cl_Id\
#         inner join tb_day d on d.d_Id=sc.d_Id\
#         inner join tb_subject s on s.s_Id=sc.s_Id\
#         inner join tb_room r on r.r_Id=sc.r_Id\
#         where f_Id = '"
#         + str(Id)
#         + "';"
#     )
#     conn.execute(sql)
#     profile = None
#     for row in conn:
#         profile = row
#     conn.close()
#     return profile


# timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# time = datetime.now().strftime("%H:%M:%S")
# my_time = str(timedelta(hours=8, minutes=45, seconds=00))
# my_time2 = my_time.split(":")

# print("timestamp =", my_time2)
a = 0
b = 1
date_Today = datetime.now().strftime("%Y-%m-%d")
time = datetime.now().strftime("%H:%M:%S")
start_Class = str(timedelta(8, 45, 00))
if start_Class < time:
    print("time =", time)
else:
    print("timeex =", time)
