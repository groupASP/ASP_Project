from tkinter import *
from tkinter import font as tkFont
from tkinter import ttk
import pymysql
from tkinter import messagebox
from datetime import *

frm = Tk()
frm.geometry("900x900")
frm.title("ລາຍງານຂໍ້ມູນລາຍຊື່ນັກຮຽນ")

connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
conn = connection.cursor()


def Get():
    frm.withdraw()
    a.deiconify()
    st = ttk.Style(a)
    st.theme_use("clam")
    st.configure("Treeview.Heading", fg="blue", font=("Saysettha OT", 14))
    st.configure("Treeview", rowheight=60, font=("Saysettha OT", 12))
    cl_Name = cb_class.get()
    today = str(date(2022, 5, 2))
    sql = (
        "select st_Id, Name, Surname, cl_Name, time_In, time_Out, first_Absence, second_Absence, date from tb_attandance where cl_Name = '"
        + cl_Name
        + "' and date = '"
        + today
        + "' ;"
    )
    conn.execute(sql)

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
    )

    tree.column("#0", width=5)
    tree.column("#1", width=150, anchor="center")
    tree.column("#2", width=150, anchor="center")
    tree.column("#3", width=150, anchor="center")
    tree.column("#4", width=150, anchor="center")
    tree.column("#5", width=150, anchor="center")
    tree.column("#6", width=150, anchor="center")
    tree.column("#7", width=150, anchor="center")
    tree.column("#8", width=150, anchor="center")
    tree.column("#9", width=150, anchor="center")

    tree.heading("#1", text="ລະຫັດນັກສຶກສາ")
    tree.heading("#2", text="ຊື່")
    tree.heading("#3", text="ນາມສະກຸນ")
    tree.heading("#4", text="ຊັ້ນຮຽນ")
    tree.heading("#5", text="ເວລາເຂົ້າຮຽນ")
    tree.heading("#6", text="ເວລາອອກຮຽນ")
    tree.heading("#7", text="ໝາຍເຂົ້າຮຽນ")
    tree.heading("#8", text="ໝາຍອອກຮຽນ")
    tree.heading("#9", text="ວັນທີ")

    # ຄຳສັ່ງສະແດງຜົນ

    i = 0
    for row in conn:
        tree.insert(
            "",
            i,
            text="",
            values=(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
            ),
        )
        i = i + 1
    tree.place(x=-15, y=80)


def back():
    l = messagebox.askquestion("Back", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າຫຼັກ ຫຼື ບໍ່?")
    if l == "yes":
        a.withdraw()
        frm.deiconify()


btn = Button(frm, text="ເພີ່ມວິຊາຮຽນ", command=Get)
btn.place(x=450, y=500)


a = Tk()
a.geometry("1500x900")
a.config(bg="#ECF8DC")
a.attributes("-fullscreen", True)
a.withdraw()


cb_Class = ["HCS6B", "HCS6C", "HCS6E"]

cbFont = tkFont.Font(family="Saysettha OT", size=16)

cb_class = ttk.Combobox(frm, width=17, values=cb_Class)
cb_class.place(x=450, y=450)
cb_class.config(font=(cbFont), state="readonly")
cb_class.option_add("*font", cbFont)
cb_class.current(0)

btn = Button(a, text="ກັບໄປ", command=back)
btn.place(x=450, y=500)


frm.mainloop()
