import pymysql
from datetime import datetime


def getProfile():
    global connection, conn
    cl_Name = "CS6B"
    r_Name = "309"
    connection = pymysql.connect(
        host="localhost", user="root", password="", database="asp_base"
    )
    conn = connection.cursor()
    sql = (
        "select st.st_Id, st.st_Name, st.st_Surname, d.d_Name, s.s_Name, \
            r.r_Name, cl.cl_Name, sc.sc_Period, sc.sc_Year, f.Name, f.Surname, sc.start_Class, \
            sc.end_Class \
            from tb_face f inner join tb_student st on f.st_Id = st.st_Id\
            inner join tb_class cl on st.cl_Id = cl.cl_Id\
            inner join tb_schedule sc on sc.cl_Id=cl.cl_Id\
            inner join tb_day d on d.d_Id=sc.d_Id\
            inner join tb_subject s on s.s_Id=sc.s_Id\
            inner join tb_room r on r.r_Id=sc.r_Id\
            where cl.cl_Name='"
        + cl_Name
        + "' and r.r_Name='"
        + r_Name
        + "';"
    )
    conn.execute(sql)
    result = conn.fetchall()
    return result


profile = getProfile()
date = datetime.now().strftime("%Y-%m-%d")
for i in profile:
    # print(i)
    insert_data = "INSERT INTO tb_attandance(a_Id, st_Id, Name, Surname, d_Name, s_Name, r_Name, cl_Name, sc_Period, sc_Year, date) VALUES (0, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    VALUES = (
        str(i[0]),
        str(i[1]),
        str(i[2]),
        str(i[3]),
        str(i[4]),
        str(i[5]),
        str(i[6]),
        str(i[7]),
        str(i[8]),
        date,
    )
    conn.execute(insert_data, VALUES)
    connection.commit()
