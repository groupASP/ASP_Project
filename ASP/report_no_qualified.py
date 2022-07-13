import tkinter
from matplotlib.ft2font import BOLD
from tkcalendar import *
from tkinter import *
from tkinter import font as tkFont
from datetime import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import os
import pandas as pd
import tkinter.filedialog as fd

frm = Tk()
frm.title("Calendar")
# frm.geometry("1000x800")
frm.attributes("-fullscreen", True)

connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
conn = connection.cursor()


def back1():
    b.withdraw()
    frm.deiconify()


def back():
    l = messagebox.askquestion("BACK", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າລາຍງານຫຼັກ ຫຼື ບໍ່?")
    if l == "yes":
        frm.withdraw()
        os.system("D:\ASP_Project\ASP\\report.py")


def report_no_qualified():
    frm.withdraw()
    b.deiconify()
    st = ttk.Style(b)
    st.theme_use("clam")
    st.configure("Treeview.Heading", fg="blue", font=("Saysettha OT", 14))
    st.configure("Treeview", rowheight=60, font=("Saysettha OT", 12))
    cl_Name = cb_class.get()
    s_Name = cb_Subject.get()
    sql = (
        "SELECT st.st_Id, st.st_Name, st.st_Surname, att.s_Name, att.cl_Name, att.sc_Period, att.sc_Year, SUM(att.first_Absence + att.second_Absence),\
        (\
        CASE\
            WHEN SUM(att.first_Absence + att.second_Absence) <= 7 THEN 'ມີສິດເສັງ'\
            ELSE 'ບໍ່ມີສິດເສັງ'\
        END\
        )\
        FROM tb_student st LEFT JOIN tb_attandance att ON st.st_Id = att.st_Id WHERE att.cl_Name='"
        + str(cl_Name)
        + "' and att.s_Name='"
        + str(s_Name)
        + "' GROUP BY st.st_Id;"
    )
    conn.execute(sql)

    tree = ttk.Treeview(b)
    tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

    tree.column("#0", width=5)
    tree.column("#1", width=180, anchor="center")
    tree.column("#2", width=150, anchor="center")
    tree.column("#3", width=150, anchor="center")
    tree.column("#4", width=250, anchor="center")
    tree.column("#5", width=100, anchor="center")
    tree.column("#6", width=180, anchor="center")
    tree.column("#7", width=180, anchor="center")
    tree.column("#8", width=180, anchor="center")
    tree.column("#9", width=180, anchor="center")

    tree.heading("#1", text="ລະຫັດນັກສຶກສາ")
    tree.heading("#2", text="ຊື່")
    tree.heading("#3", text="ນາມສະກຸນ")
    tree.heading("#4", text="ວິຊາ")
    tree.heading("#5", text="ຊັ້ນຮຽນ")
    tree.heading("#6", text="ພາກ")
    tree.heading("#7", text="ສົກຮຽນ")
    tree.heading("#8", text="ຜົນລວມການຂາດຮຽນ")
    tree.heading("#9", text="ສະຖານະ")

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

    def export_data():
        sql = (
            "SELECT st.st_Id, st.st_Name, st.st_Surname, att.s_Name, att.cl_Name, att.sc_Period, att.sc_Year, SUM(att.first_Absence + att.second_Absence),\
        (\
        CASE\
            WHEN SUM(att.first_Absence + att.second_Absence) <= 7 THEN 'ມີສິດເສັງ'\
            ELSE 'ບໍ່ມີສິດເສັງ'\
        END\
        )\
        FROM tb_student st LEFT JOIN tb_attandance att ON st.st_Id = att.st_Id WHERE att.cl_Name='"
            + str(cl_Name)
            + "' and att.s_Name='"
            + str(s_Name)
            + "' GROUP BY st.st_Id;"
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
            "ຜົນລວມການຂາດຮຽນ",
            "ສະຖານະ",
        ]
        file_name = fd.asksaveasfilename(
            filetypes=[("excel file", "*.xlsx")], defaultextension=".xlsx"
        )
        df.to_excel(file_name, index=False, header=header, encoding="utf-8")

    bt_export = tkinter.Button(b, text="Export", command=export_data, width=16)
    bt_export.place(x=900, y=750)
    bt_export.configure(font=("Times New Roman", 25), bg="green", fg="white")


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
background_img = PhotoImage(file="ASP/Image/bg_report_exam.png")
background = canvas.create_image(950.0, 540.0, image=background_img)

bt5 = PhotoImage(file="ASP/Image/bt_report.png")
button_5 = Button(
    image=bt5,
    borderwidth=0,
    highlightthickness=0,
    command=report_no_qualified,
    relief="flat",
)
button_5.place(x=900, y=700)

bt4 = PhotoImage(file="ASP/Image/back.png")
button_4 = Button(
    image=bt4,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat",
)
button_4.place(x=250, y=700)


def back1():
    b.withdraw()
    frm.deiconify()


#################################################################################
#################################################################################


b = Tk()
# b.geometry("1500x900")
b.config(bg="#ECF8DC")
b.attributes("-fullscreen", True)
b.withdraw()

cbFont = tkFont.Font(family="Saysettha OT", size=18)

conn.execute("select cl_Name from tb_class;")
results = conn.fetchall()
combo_cl_name = [result[0] for result in results]


class_lb = Label(frm, text="ກະລຸນາເລືອກຊັ້ນຮຽນ : ", font=cbFont, bg="#ECF8DC")
class_lb.place(x=450, y=200)

cb_class = ttk.Combobox(frm, width=25, values=combo_cl_name)
cb_class.place(x=700, y=200)
cb_class.config(font=(cbFont), state="readonly")
cb_class.configure(font=("Saysettha OT", 16))
cb_class.option_add("*font", cbFont)
cb_class.current(0)

conn.execute("select s_Name from tb_subject")
results = conn.fetchall()
combo_s_name = [result[0] for result in results]

subject_lb = Label(frm, text="ກະລຸນາເລືອກວິຊາ : ", font=cbFont, bg="#ECF8DC")
subject_lb.place(x=450, y=450)

cb_Subject = ttk.Combobox(frm, width=25, values=combo_s_name)
cb_Subject.place(x=700, y=450)
cb_Subject.config(font=(cbFont), state="readonly")
cb_Subject.configure(font=("Saysettha OT", 16))
cb_Subject.option_add("*font", cbFont)
cb_Subject.current(0)

lbShow = Label(b, text="ລາຍງານຂໍ້ມູນນັກສຶກສາບໍ່ມີສິດເສັງ")
lbShow.pack(side="top", fill="x")
lbShow.configure(font=("Saysettha OT", 30), bg="#04C582", fg="white")

bts = tkinter.Button(b, text="Back", command=back1, width=16)
bts.place(x=300, y=750)
bts.configure(font=("Times New Roman", 25), bg="#CEC2C2", fg="black")


frm.mainloop()
