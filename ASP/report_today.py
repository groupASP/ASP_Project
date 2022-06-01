from tkinter import *
import tkinter
from tkinter import ttk
import pymysql
from tkinter import messagebox
import os
from datetime import *

a = tkinter.Tk()
a.geometry("1500x900")
a.attributes("-fullscreen", True)

# ຄຳສັ່ງເຊື່ອມຕໍ່
connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
conn = connection.cursor()

date_today = datetime.now().strftime("%Y-%m-%d")

sql = "select * from tb_attandance where date='" + date_today + "';"
conn.execute(sql)


def back():
    l = messagebox.askquestion("BACK", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າລາຍງານຫຼັກ ຫຼື ບໍ່?")
    if l == "yes":
        a.withdraw()
        os.system("D:\ASP_Project\ASP\\report.py")


# button
canvas = Canvas(
    a, bg="#FFFFFF", height=1080, width=1920, bd=0, highlightthickness=0, relief="ridge"
)

canvas.place(x=0, y=0)

background_img = PhotoImage(file="ASP/Image/bg_report.png")
background = canvas.create_image(950.0, 540.0, image=background_img)

bt1 = PhotoImage(file="ASP/Image/bg_report_today.png")
button_1 = Button(
    image=bt1,
    borderwidth=0,
    highlightthickness=0,
    # command=check_in,
    relief="flat",
)


bt5 = PhotoImage(file="ASP/Image/back.png")
button_5 = Button(
    image=bt5,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat",
)

st = ttk.Style()
st.theme_use("clam")
st.configure("Treeview.Heading", fg="blue", font=("Saysettha OT", 14))
st.configure("Treeview", rowheight=60, font=("Saysettha OT", 12))


tree = ttk.Treeview(a)
tree["columns"] = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
)

tree.column("#0", width=5)
tree.column("#1", width=180)
tree.column("#2", width=100)
tree.column("#3", width=100)
tree.column("#4", width=80)
tree.column("#5", width=250)
tree.column("#6", width=80)
tree.column("#7", width=80)
tree.column("#8", width=80)
tree.column("#9", width=100)
tree.column("#10", width=100)
tree.column("#11", width=100)
tree.column("#12", width=80)
tree.column("#13", width=90)
tree.column("#14", width=120)


tree.heading("#1", text="ລະຫັດນັກສຶກສາ")
tree.heading("#2", text="ຊື່")
tree.heading("#3", text="ນາມສະກຸນ")
tree.heading("#4", text="ມື້ຮຽນ")
tree.heading("#5", text="ວິຊາ")
tree.heading("#6", text="ຫ້ອງ")
tree.heading("#7", text="ຊັ້ນຮຽນ")
tree.heading("#8", text="ພາກ")
tree.heading("#9", text="ສົກຮຽນ")
tree.heading("#10", text="ເວລາເຂົ້າ")
tree.heading("#11", text="ເວລາອອກ")
tree.heading("#12", text="ໝາຍເຂົ້າ")
tree.heading("#13", text="ໝາຍອອກ")
tree.heading("#14", text="ວັນທີ")


# ຄຳສັ່ງສະແດງຜົນ

i = 1
for row in conn:
    tree.insert(
        "",
        i,
        text="",
        values=(
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
            row[8],
            row[9],
            row[10],
            row[11],
            row[12],
            row[13],
            row[14],
        ),
    )
    i = i + 1
tree.place(x=-15, y=80)

button_5.place(x=200, y=750)


a.mainloop()
