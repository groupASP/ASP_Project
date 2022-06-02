import pandas as pd
import pymysql
import tkinter.filedialog as fd


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
file_name = fd.asksaveasfilename(
    filetypes=[("excel file", "*.xlsx")], defaultextension=".xlsx"
)
df.to_excel(file_name, index=False, header=header, encoding="utf-8")
