from tkinter import *
from tkinter import font as tkFont
from datetime import *
from tkinter import ttk
import pymysql

frm = Tk()
frm.title("Calendar")
frm.geometry("1000x800")

connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
conn = connection.cursor()


def report_teacher_today():
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
    tree.column("#3", width=100, anchor="center")
    tree.column("#4", width=100, anchor="center")
    tree.column("#5", width=100, anchor="center")
    tree.column("#6", width=100, anchor="center")
    tree.column("#7", width=100, anchor="center")
    tree.column("#8", width=100, anchor="center")
    tree.column("#9", width=100, anchor="center")
    tree.column("#10", width=100, anchor="center")
    tree.column("#11", width=100, anchor="center")
    tree.column("#12", width=100, anchor="center")

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


bt5 = PhotoImage(file="ASP/Image/bt_report.png")
button_5 = Button(
    image=bt5,
    borderwidth=0,
    highlightthickness=0,
    command=report_teacher_today,
    relief="flat",
)
button_5.place(x=500, y=600)


b = Tk()
b.geometry("1500x900")
b.config(bg="#ECF8DC")
b.withdraw()

cbFont = tkFont.Font(family="Saysettha OT", size=16)


class_lb = Label(frm, text="ກະລຸນາປ້ອນລະຫັດນັກສຶກສາ", font=cbFont)
class_lb.place(x=200, y=350)

st_En = Entry(frm, width=30, font=cbFont)
st_En.place(x=200, y=400)

conn.execute("select s_Name from tb_subject")
results = conn.fetchall()
combo_s_name = [result[0] for result in results]

subject_lb = Label(frm, text="ກະລຸນາເລືອກວິຊາ", font=cbFont)
subject_lb.place(x=200, y=500)

cb_Subject = ttk.Combobox(frm, width=16, values=combo_s_name)
cb_Subject.place(x=200, y=550)
cb_Subject.config(font=(cbFont), state="readonly")
cb_Subject.configure(font=("Saysettha OT", 16))
cb_Subject.option_add("*font", cbFont)
cb_Subject.current(0)

lbShow = Label(b, text="ລາຍງານຂໍ້ມູນນັກສຶກສາ")
lbShow.pack(side="top", fill="x")
lbShow.configure(font=("Saysettha OT", 30), bg="#04C582", fg="white")


frm.mainloop()
