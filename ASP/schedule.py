from sre_parse import State
import tkinter
from tkinter import ttk
import os
from tkinter import font as tkfont
from tkinter import messagebox
from tkinter import *
import pymysql

a = tkinter.Tk()
a.geometry("1500x900")

a.title("display from database")
a.attributes('-fullscreen', True)

# ຄຳສັ່ງເຊື່ອມຕໍ່
connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
conn = connection.cursor()

sql = "select * from tb_schedule;"
conn.execute(sql)

def back():
    l = messagebox.askquestion("Back", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າຫຼັກ ຫຼື ບໍ່?")
    if (l == 'yes'):
        a.withdraw()
        os.system("D:\ASP_Project\ASP\window1.py")


def save():
    sc_Id = en_scid.get()
    d_Id = cb_day.get()
    sc_Period = cb_period.get()
    sc_Year = en_year.get()
    r_Id = cb_room.get()
    cl_Id = cb_cl.get()
    s_Id = cb_subject.get()
    t_Id = cb_teacher.get()
    
    sc_Id.config(state="disabled")

    connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
    conn = connection.cursor()

    sql_update ="update tb_schedule set d_Id='"+d_Id+"', sc_Period='"+sc_Period+"', sc_Year='"+sc_Year+"', r_Id='"+r_Id+"', cl_Id='"+cl_Id+"', s_Id='"+s_Id+"', t_Id='"+t_Id+"' where sc_Id='"+str(sc_Id)+"';"
    conn.execute(sql_update)
    connection.commit()

    for i in tree.get_children():
        tree.delete(i)

    sql_select="select * from tb_schedule;"
    conn.execute(sql_select)

    i=0
    for row in conn:
        tree.insert('', i,text="",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        i=i+1


    en_scid.delete(0, END)
    en_year.delete(0, END)
    cb_room.current(0)
    cb_cl.current(0)
    cb_period.current(0)
    cb_subject.current(0)
    cb_teacher.current(0)
    cb_day.current(0)
    messagebox.showinfo("ການແກ້ໄຂຂໍ້ມູນ", "ທ່ານໄດ້ແກ້ໄຂຂໍ້ມູນນັກສຶກສາສຳເລັດແລ້ວ!!!")

def edit():
    data = tree.selection()
    value = tree.item(data)['values'][0]

    connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
    conn = connection.cursor()

    sql_select = "select * from tb_schedule where sc_Id='" + str(value) + "';"
    conn.execute(sql_select)

    for row in conn:
        sc_Id = row[0]
        d_Id = row[1]
        sc_Period = row[2]
        sc_Year = row[3]
        r_Id = row[4]
        cl_Id = row[6]
        s_Id = row[5]
        t_Id = row[7]

        en_scid.insert(0, sc_Id)
        cb_day.insert(0, d_Id)
        cb_period.insert(0, sc_Period)
        en_year.insert(0, sc_Year)
        cb_room.insert(0, r_Id)
        cb_cl.insert(0, cl_Id)
        cb_subject.insert(0, s_Id)
        cb_teacher.insert(0, t_Id)
    en_scid.config(state="disabled")
    a.withdraw()
    b.deiconify()


def delete():
    data = tree.selection()
    value = tree.item(data)['values'][0]
    
    connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
    conn = connection.cursor()

    sql_delete = "delete from tb_schedule where sc_Id='" + str(value) + "';"
    conn.execute(sql_delete)
    connection.commit()

    for i in tree.get_children():
        tree.delete(i)

    sql_select = "select * from tb_schedule;"
    conn.execute(sql_select)

    i = 0
    for row in conn:
        tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        i = i + 1
    messagebox.showinfo("ການສະແດງຜົນ", "ທ່ານໄດ້ລົບຂໍ້ມູນນັກສຶກສາສຳເລັດແລ້ວ!!!")


def insert():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\insert_schedule.py")


canvas = Canvas(
    a,
    bg="#ffffff",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"ASP/Image/bg_sche.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)

img1 = PhotoImage(file=f"ASP/Image/add.png")
btAdd = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=insert,
    relief="flat")
btAdd.place(
    x=480, y=650, )

img2 = PhotoImage(file=f"ASP/Image/back.png")
btBack = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat")
btBack.place(
    x=100, y=650, )

img3 = PhotoImage(file=f"ASP/Image/delete.png")
btDelete = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=delete,
    relief="flat")
btDelete.place(
    x=1200, y=650, )

img4 = PhotoImage(file=f"ASP/Image/edit.png")
btEdit = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=edit,
    relief="flat")
btEdit.place(
    x=840, y=650, )

st = ttk.Style()
st.theme_use("clam")
st.configure("Treeview.Heading", fg="blue", font=("Saysettha OT", 14))
st.configure("Treeview", rowheight=50, font=("Saysettha OT", 12))


tree = ttk.Treeview(a)
tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
tree.column("#0", width=5)
tree.column("#1", width=100)
tree.column("#2", width=180)
tree.column("#3", width=180)
tree.column("#4", width=180)
tree.column("#5", width=180)
tree.column("#6", width=180)
tree.column("#7", width=180)

tree.heading("#1", text="ລະຫັດ")
tree.heading("#2", text="ມື້")
tree.heading("#3", text="ຄາບຮຽນ")
tree.heading("#4", text="ສົກຮຽນ")
tree.heading("#5", text="ລະຫັດຫ້ອງ")
tree.heading("#7", text="ລະຫັດຊັ້ນຮຽນ")
tree.heading("#6", text="ລະຫັດວິຊາ")
tree.heading("#8", text="ລະຫັດອາຈານ")

# ຄຳສັ່ງສະແດງຜົນ

i = 0
for row in conn:
    tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    i = i + 1
tree.place(x=30, y=80)

############################################################################################################
############################################################################################################

# ໜ້າທີ່2
b = tkinter.Tk()
b.geometry("1500x900")
b.config(bg="#ECF8DC")
b.attributes('-fullscreen', True)
b.withdraw()

lbShow = tkinter.Label(b, text="ແກ້ໄຂຂໍ້ມູນ")
lbShow.pack(side='top', fill='x')
lbShow.configure(font=("Saysettha OT", 30), bg="#04C582", fg="white")



def ex():
    exit()

def back1():
    en_scid.delete(0, END)
    en_year.delete(0, END)
    cb_room.set("")
    cb_cl.set("")
    cb_period.set("")
    cb_day.set("")
    cb_subject.set("")
    cb_teacher.set("")
    a.deiconify()
    b.withdraw()

lb = tkinter.Label(b, text="ລະຫັດ:")
lb.place(x=40, y=50)
lb.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb1 = tkinter.Label(b, text="ມື້ຮຽນ:")
lb1.place(x=40, y=150)
lb1.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb2 = tkinter.Label(b, text="ຮອບຮຽນ:")
lb2.place(x=500, y=150)
lb2.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb3 = tkinter.Label(b, text="ສົກຮຽນ:")
lb3.place(x=1050, y=150)
lb3.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb4 = tkinter.Label(b, text="ຫ້ອງຮຽນ:")
lb4.place(x=20, y=450)
lb4.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb5 = tkinter.Label(b, text="ຊັ້ນຮຽນ:")
lb5.place(x=390, y=450)
lb5.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb6 = tkinter.Label(b, text="ວິຊາຮຽນ:")
lb6.place(x=800, y=450)
lb6.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb7 = tkinter.Label(b, text="ລະຫັດອາຈານ:")
lb7.place(x=1180, y=450)
lb7.config(font=("Saysettha OT", 18),bg="#ECF8DC")

# Entry
en_year = tkinter.Entry(b)
en_year.place(x=1150, y=150)
en_year.config(font=("Saysettha OT",18),width=20)

en_scid = tkinter.Entry(b)
en_scid.place(x=800, y=50)
en_scid.config(font=("Saysettha OT",18),width=20)


#SET FONT
cbFont = tkfont.Font(family="Saysettha OT", size=16)


# combo peroid
cb_list_period = ["ພາກເຊົ້າ", "ພາກບ່າຍ", "ພາກຄ່ຳ"]

cb_period = ttk.Combobox(b, width=15, value=cb_list_period)
cb_period.place(x=650, y=150)
cb_period.config(font=("Saysettha OT", 18), state="readonly")
cb_period.current(0)
cb_period.option_add("*font", cbFont)

#connect database
conn = pymysql.connect(user="root", password="", host="Localhost",database="asp_base")
curs = conn.cursor()


# combo day
curs.execute('select d_Id from tb_day;')
results = curs.fetchall()
combo_d_id = [result[0] for result in results]

cb_day = ttk.Combobox(b, width=15, value=combo_d_id)
cb_day.place(x=150, y=150)
cb_day.config(font=("Saysettha OT", 18), state="readonly")
cb_day.option_add("*font", cbFont)
cb_day.current()

#combo_room_id form database
curs.execute('select r_Id from tb_room;')
results = curs.fetchall()
combo_r_id = [result[0] for result in results]

#combobox_room_id
cb_room =ttk.Combobox(b, width=12,values=combo_r_id)
cb_room.place(x=150, y=450)
cb_room.config(font=(cbFont), state="readonly")
cb_room.option_add("*font", cbFont)
cb_room.current()

#combo_subject_id form database
curs.execute('select s_Id from tb_subject;')
results = curs.fetchall()
combo_s_id = [result[0] for result in results]

#combobox_subject_id
cb_subject =ttk.Combobox(b, width=18,values=combo_s_id)
cb_subject.place(x=910, y=450)
cb_subject.config(font=(cbFont), state="readonly")
cb_subject.option_add("*font", cbFont)
cb_subject.current()

#combo_class_id form database
curs.execute('select cl_Id from tb_class;')
results = curs.fetchall()
combo_cl_id = [result[0] for result in results]

#combobox_class_id
cb_cl =ttk.Combobox(b, width=17,values=combo_cl_id)
cb_cl.place(x=520, y=450)
cb_cl.config(font=(cbFont), state="readonly")
cb_cl.option_add("*font", cbFont)
cb_cl.current()

#combo_teacher_id form database
curs.execute('select t_Id from tb_teacher;')
results = curs.fetchall()
combo_t_id = [result[0] for result in results]

#combobox_student_id
cb_teacher =ttk.Combobox(b, width=13,values=combo_t_id)
cb_teacher.place(x=1330, y=450)
cb_teacher.config(font=(cbFont), state="readonly")
cb_teacher.option_add("*font", cbFont)
cb_teacher.current()

# button
bts = tkinter.Button(b, text="Update",command=save,width=20)
bts.place(x=900, y=650)
bts.configure(font=("Saysettha OT", 18), bg="green", fg="white")

bt = tkinter.Button(b, text="BACK",command=back1,width=20)
bt.place(x=300, y=650)
bt.configure(font=("Saysettha OT", 18), bg="gray", fg="black")



a.mainloop()