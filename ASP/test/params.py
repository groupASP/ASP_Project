import pymysql


def getId():
    connection = pymysql.connect(
        host="localhost", user="root", password="", database="asp_base"
    )
    conn = connection.cursor()
    sql = "SELECT sc_Id FROM tb_schedule order by sc_Id desc limit 1;"
    conn.execute(sql)
    profile = None
    for row in conn:
        profile = row
    connection.close()
    c = int("".join(map(str, profile)))
    return c


a = getId()
print(a)
b = a + 1
print(b)
