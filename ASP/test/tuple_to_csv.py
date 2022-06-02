import pandas as pd
import pymysql


local = "localhost"
user = "root"
password = ""
db = "asp_base"


connection = pymysql.connect(host=local, user=user, password=password, db=db)
conn = connection.cursor()


def data():
    conn.execute(
        "SELECT st_Id, Name, Surname, s_Name, r_Name, cl_Name, sc_Period, sc_Year FROM tb_attandance"
    )
    rows = conn.fetchall()
    df = pd.DataFrame(rows)
    df.to_csv("ASP\\test\\cs.csv", index=False, header=False)


sql = "SELECT st_Id, Name, Surname, s_Name, r_Name, cl_Name, sc_Period, sc_Year FROM tb_attandance"
df = pd.read_sql(sql, connection)
header = [
    "ລະຫັດນັກສຶກສາ",
    "ຊື່",
    "ນາມສະກຸນ",
    "ວິຊາ",
    "ຫ້ອງ",
    "ຊັ້ນຮຽນ",
    "ພາກ",
    "ສົກຮຽນ",
]
filename = input("ກະລຸນາປ້ອນຊື່ໄຟລ໌ໃຫ້ກົດປຸ່ມ Enter: ")
df.to_excel(
    "ASP\\test\\" + filename + ".xlsx", index=False, header=header, encoding="utf-8"
)
