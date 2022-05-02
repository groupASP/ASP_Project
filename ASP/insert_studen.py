from math import comb
import tkinter
from tkinter import ttk
from tkinter import font as tkfont
import os
from tkinter import messagebox
from tkinter import *
import pymysql

frm = tkinter.Tk()
frm.title("Insert Student")
frm.geometry('1920x1080')
frm.attributes('-fullscreen', True)

def insert():
    import pymysql
    connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
    conn = connection.cursor()

    st_Id = en.get()
    st_Name = en1.get()
    st_Surname = en2.get()
    st_DOB = en3.get()
    st_Tel = en4.get()
    st_village=en_village.get()
    st_district=en_district.get()
    st_province=en_province.get()
    st_Gender=cbGender.get()
    cl_Id=cb.get()
    value = messagebox.askquestion("ການຢືນຢັນ", "ທ່ານຕ້ອງການເພີ່ມຂໍ້ມູນແທ້ຫຼືບໍ່?")
    if(value == 'yes'):
        sql_insert = "insert into tb_student values('"+st_Id+"','"+st_Name+"','"+st_Surname+"','"+st_Gender+"','"+cl_Id+"','"+st_DOB+"','"+st_Tel+"','"+st_village+"','"+st_district+"','"+st_province+"');"
        conn.execute(sql_insert)
        connection.commit()
        messagebox.showinfo("ການສະແດງຜົນ","ທ່ານໄດ້ເພີ່ມຂໍ້ມູນນັກສຶກສາສຳເລັດແລ້ວ")
    en.delete(0,END)
    en1.delete(0,END)
    en2.delete(0,END)
    en3.delete(0,END)
    en4.delete(0,END)
    en_village.delete(0,END)
    en_district.delete(0,END)
    en_province.delete(0,END)
    cbGender.set("")


def back():
    l = messagebox.askquestion("Back","ທ່ານຕ້ອງການຈະກັບໄປໜ້າຂໍ້ມູນນັກສຶກສາ ຫຼື ບໍ່?")
    if(l == 'yes'):
        frm.withdraw()
        os.system("D:\ASP_Project\ASP\student.py")



canvas = Canvas(
    frm,
    bg = "#ffffff",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"ASP/Image/bg_insert.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)


lb1 = tkinter.Label(frm, text="ລະຫັດນັກສຶກສາ:")
lb1.place(x=20, y=150)
lb1.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb2 = tkinter.Label(frm, text="ຊື່:")
lb2.place(x=550, y=150)
lb2.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb3 = tkinter.Label(frm, text="ນາມສະກຸນ:")
lb3.place(x=1000, y=150)
lb3.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb4 = tkinter.Label(frm, text="ເພດ:")
lb4.place(x=20, y=330)
lb4.config(font=("Saysettha OT", 20),bg="#ECF8DC")

lb5 = tkinter.Label(frm, text="ວັນເດືອນປີເກີດ:")
lb5.place(x=480, y=330)
lb5.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb6 = tkinter.Label(frm, text="ເບີໂທ:")
lb6.place(x=1050, y=330)
lb6.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb7 = tkinter.Label(frm, text="ບ້ານ:")
lb7.place(x=30, y=520)
lb7.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb9 = tkinter.Label(frm, text="ເມືອງ:")
lb9.place(x=410, y=520)
lb9.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb10 = tkinter.Label(frm, text="ແຂວງ:")
lb10.place(x=800, y=520)
lb10.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb11 = tkinter.Label(frm, text="ຊັ້ນຮຽນ:")
lb11.place(x=1200, y=520)
lb11.config(font=("Saysettha OT", 18),bg="#ECF8DC")


# Entry
en = tkinter.Entry(frm,width=18)
en.place(x=200, y=150)
# en=enID.get().encode('utf-8')
en.config(font=("Saysettha OT",18),width=18)

en1 = tkinter.Entry(frm)
en1.place(x=600, y=150)
en1.config(font=("Saysettha OT",18),width=25)

en2 = tkinter.Entry(frm)
en2.place(x=1150, y=150)
en2.config(font=("Saysettha OT",18),width=25)

en3 = tkinter.Entry(frm)
en3.place(x=650, y=330)
en3.config(font=("Saysettha OT",18),width=25)

en4 = tkinter.Entry(frm)
en4.place(x=1150, y=330)
en4.config(font=("Saysettha OT",18),width=25)



#SET FONT
cbFont = tkfont.Font(family="Saysettha OT", size=16)
#
en_village = ttk.Entry(frm)
en_village.place(x=110, y=520)
en_village.config(font=("Saysettha OT", 18))
en_village.option_add("*font", cbFont)

en_district = ttk.Entry(frm)
en_district.place(x=490, y=520)
en_district.config(font=("Saysettha OT", 18))
en_district.option_add("*font", cbFont)

en_province = ttk.Entry(frm)
en_province.place(x=870, y=520)
en_province.config(font=("Saysettha OT", 18))
en_province.option_add("*font", cbFont)

# ComboList
cbList = ["ຊາຍ", "ຍິງ"]

cbGender = ttk.Combobox(frm, width=15, value=cbList)
cbGender.place(x=200, y=330)
cbGender.config(font=("Saysettha OT", 18), state="readonly")
cbGender.current(0)
cbGender.option_add("*font", cbFont)

#connect database
conn = pymysql.connect(user="root", password="", host="Localhost",database="asp_base")
curs = conn.cursor()

#combo_student_id form database
curs.execute('select cl_Id from tb_class;')
results = curs.fetchall()
combo_cl_id = [result[0] for result in results]

#combobox_student_id
cb =ttk.Combobox(frm, width=16,values=combo_cl_id)
cb.place(x=1300, y=520)
cb.config(font=(cbFont), state="readonly")
cb.option_add("*font", cbFont)
cb.current()

#Button
img1 = PhotoImage(file = f"ASP/Image/add.png")
btAdd = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = insert,
    relief = "flat")

btAdd.place(
    x = 900, y = 690,)

img2 = PhotoImage(file = f"ASP/Image/back.png")
btBack = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = back,
    relief = "flat")

btBack.place(
    x = 400, y = 690,)


frm.mainloop()