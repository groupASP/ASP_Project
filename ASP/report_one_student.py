from tkinter import *
from tkinter import font as tkFont
from datetime import *
from tkinter import ttk
import tkinter
import pymysql
from tkinter import messagebox
import os
import pandas as pd
import tkinter.filedialog as fd

frm = Tk()
frm.geometry("1000x800")
frm.attributes("-fullscreen", True)

connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
conn = connection.cursor()


def report_one_student():
    frm.withdraw()
    b.deiconify()
    st = ttk.Style(b)
    st.theme_use("clam")
    st.configure("Treeview.Heading", fg="blue", font=("Saysettha OT", 14))
    st.configure("Treeview", rowheight=60, font=("Saysettha OT", 12))
    st_Id = st_En.get()
    s_Name = cb_Subject.get()
    sql = (
        "SELECT st_Id, Name, Surname, s_Name, cl_Name, sc_Period, sc_Year, time_In, time_Out, first_Absence, second_Absence, date from tb_attandance where st_Id='"
        + st_Id
        + "' and s_Name='"
        + str(s_Name)
        + "' GROUP BY a_Id, date"
    )
    conn.execute(sql)

    tree = ttk.Treeview(b)
    tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")

    tree.column("#0", width=5)
    tree.column("#1", width=180, anchor="center")
    tree.column("#2", width=100, anchor="center")
    tree.column("#3", width=150, anchor="center")
    tree.column("#4", width=230, anchor="center")
    tree.column("#5", width=100, anchor="center")
    tree.column("#6", width=100, anchor="center")
    tree.column("#7", width=120, anchor="center")
    tree.column("#8", width=100, anchor="center")
    tree.column("#9", width=100, anchor="center")
    tree.column("#10", width=100, anchor="center")
    tree.column("#11", width=100, anchor="center")
    tree.column("#12", width=180, anchor="center")

    tree.heading("#1", text="ລະຫັດນັກສຶກສາ")
    tree.heading("#2", text="ຊື່")
    tree.heading("#3", text="ນາມສະກຸນ")
    tree.heading("#4", text="ວິຊາ")
    tree.heading("#5", text="ຊັ້ນຮຽນ")
    tree.heading("#6", text="ພາກ")
    tree.heading("#7", text="ສົກຮຽນ")
    tree.heading("#8", text="ເວລາເຂົ້າ")
    tree.heading("#9", text="ເວລາອອກ")
    tree.heading("#10", text="ໝາຍເຂົ້າ")
    tree.heading("#11", text="ໝາຍອອກ")
    tree.heading("#12", text="ວັນທີ່")

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
                row[9],
                row[10],
                row[11],
            ),
        )
        i = i + 1
    tree.place(x=-15, y=80)

    def export_data():
        sql = (
            "SELECT st_Id, Name, Surname, s_Name, cl_Name, sc_Period, sc_Year, time_In, time_Out, first_Absence, second_Absence, date from tb_attandance where st_Id='"
            + st_Id
            + "' and s_Name='"
            + str(s_Name)
            + "' GROUP BY a_Id, date"
        )
        df = pd.read_sql(sql, connection)
        header = [
            "ລະຫັດນັກສຶກສາ",
            "ຊື່",
            "ນາມສະກຸນ",
            "ວິຊາ",
            "ຊັ້ນຮຽນ",
            "ພາກ",
            "ສົກຮຽນ",
            "ເວລາເຂົ້າຮຽນ",
            "ເວລາອອກຮຽນ",
            "ໝາຍເຂົ້າຮຽນ",
            "ໝາຍອອກຮຽນ",
            "ວັນທີ",
        ]
        file_name = fd.asksaveasfilename(
            filetypes=[("excel file", "*.xlsx")], defaultextension=".xlsx"
        )
        df.to_excel(file_name, index=False, header=header, encoding="utf-8")

    bt_export = tkinter.Button(b, text="Export", command=export_data, width=16)
    bt_export.place(x=900, y=750)
    bt_export.configure(font=("Times New Roman", 25), bg="green", fg="white")


def back1():
    l = messagebox.askquestion("BACK", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າລາຍງານຫຼັກ ຫຼື ບໍ່?")
    if l == "yes":
        frm.withdraw()
        os.system("D:\ASP_Project\ASP\\report.py")


def back():
    b.withdraw()
    frm.deiconify()


canvas = Canvas(
    frm,
    bg="#FFFFFF",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)

background_img = PhotoImage(file="ASP/Image/bg_report_one.png")
background = canvas.create_image(950.0, 540.0, image=background_img)


bt5 = PhotoImage(file="ASP/Image/bt_report.png")
button_5 = Button(
    image=bt5,
    borderwidth=0,
    highlightthickness=0,
    command=report_one_student,
    relief="flat",
)
button_5.place(x=900, y=700)

img0 = PhotoImage(file=f"ASP/Image/back.png")
b0 = Button(
    image=img0, borderwidth=0, highlightthickness=0, command=back1, relief="flat"
)

b0.place(x=400, y=700)

################################################################################################
################################################################################################


b = Tk()
b.config(bg="#ECF8DC")
b.attributes("-fullscreen", True)
b.withdraw()


cbFont = tkFont.Font(family="Saysettha OT", size=18)


class_lb = Label(frm, text="ກະລຸນາປ້ອນລະຫັດນັກສຶກສາ", font=cbFont, bg="#ECF8DC")
class_lb.place(x=300, y=200)

st_En = Entry(frm, width=30, font=cbFont)
st_En.place(x=700, y=200)

conn.execute("select s_Name from tb_subject")
results = conn.fetchall()
combo_s_name = [result[0] for result in results]

subject_lb = Label(frm, text="ກະລຸນາເລືອກວິຊາ", font=cbFont, bg="#ECF8DC")
subject_lb.place(x=300, y=450)

cb_Subject = ttk.Combobox(frm, width=30, values=combo_s_name)
cb_Subject.place(x=700, y=450)
cb_Subject.config(font=(cbFont), state="readonly")
cb_Subject.configure(font=("Saysettha OT", 18))
cb_Subject.option_add("*font", cbFont)
cb_Subject.current(0)

lbShow = Label(b, text="ລາຍງານຂໍ້ມູນນັກສຶກສາ")
lbShow.pack(side="top", fill="x")
lbShow.configure(font=("Saysettha OT", 30), bg="#04C582", fg="white")

bts = tkinter.Button(b, text="Back", command=back, width=16)
bts.place(x=300, y=750)
bts.configure(font=("Times New Roman", 25), bg="#CEC2C2", fg="black")

frm.mainloop()
