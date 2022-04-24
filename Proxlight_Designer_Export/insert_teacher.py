import tkinter
from tkinter import ttk
from tkinter import font as tkfont
import os
import pymysql
import mysql.connector
from tkinter import messagebox
from tkinter import *
import db

frm = tkinter.Tk()
frm.title("Insert Student")
frm.geometry('1920x1080')
frm.attributes('-fullscreen', True)

def insert():
    # connection = pymysql.connect(host="localhost", user="root", password="", database="asp_base")
    # conn = connection.cursor()
    connection=pymysql.connect(host="Localhost",user="root",password="",database="asp_base")
    conn=connection.cursor()
    t_Id = en_id.get()
    t_Name = en_name.get()
    t_Surname = en_surname.get()
    t_Village = en_village.get()
    t_District = en_district.get()
    t_Province=en_province.get()
    t_Tel=en_tel.get()
    t_Email=en_email.get()
    t_Degree=en_degree.get()

    if(v1.get() == 1):
        t_Gender = "ຊາຍ"
    else:
        t_Gender = "ຍິງ"
    value = messagebox.askquestion("ການຢືນຢັນ", "ທ່ານຕ້ອງການເພີ່ມຂໍ້ມູນແທ້ຫຼືບໍ່?")
    if(value == 'yes'):
        sql_insert = "insert into tb_teacher values('"+t_Id+"','"+t_Name+"','"+t_Surname+"','"+t_Gender+"','"+t_Village+"','"+t_District+"','"+t_Province+"','"+t_Tel+"','"+t_Email+"','"+t_Degree+"');"
        conn.execute(sql_insert)
        connection.commit()
        messagebox.showinfo("ການສະແດງຜົນ","ທ່ານໄດ້ເພີ່ມຂໍ້ມູນນັກສຶກສາສຳເລັດແລ້ວ")
    en_id.delete(0,END)
    en_name.delete(0,END)
    en_surname.delete(0,END)
    en_village.delete(0,END)
    en_district.delete(0,END)
    en_province.delete(0,END)
    en_tel.delete(0,END)
    en_email.delete(0,END)
    en_degree.delete(0,END)


def back():
    l = messagebox.askquestion("Back","ທ່ານຕ້ອງການຈະກັບໄປໜ້າຂໍ້ມູນອາຈານ ຫຼື ບໍ່?")
    if(l == 'yes'):
        frm.withdraw()
        os.system("python teacher.py")



canvas = Canvas(
    frm,
    bg = "#ffffff",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"bg_teacher.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)


lb1 = tkinter.Label(frm, text="ລະຫັດອາຈານ:")
lb1.place(x=20, y=150)
lb1.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb2 = tkinter.Label(frm, text="ຊື່:")
lb2.place(x=530, y=150)
lb2.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb3 = tkinter.Label(frm, text="ນາມສະກຸນ:")
lb3.place(x=980, y=150)
lb3.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb4 = tkinter.Label(frm, text="ເພດ:")
lb4.place(x=20, y=330)
lb4.config(font=("Saysettha OT", 20),bg="#ECF8DC")

lb5 = tkinter.Label(frm, text="ບ້ານ:")
lb5.place(x=430, y=330)
lb5.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb6 = tkinter.Label(frm, text="ເມືອງ:")
lb6.place(x=800, y=330)
lb6.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb7 = tkinter.Label(frm, text="ແຂວງ:")
lb7.place(x=1170, y=330)
lb7.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb9 = tkinter.Label(frm, text="ເບີໂທ:")
lb9.place(x=20, y=520)
lb9.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb10 = tkinter.Label(frm, text="ອີເມວ:")
lb10.place(x=450, y=520)
lb10.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb11 = tkinter.Label(frm, text="ລະດັບການສຶກສາ:")
lb11.place(x=920, y=520)
lb11.config(font=("Saysettha OT", 18),bg="#ECF8DC")


# Entry
en_id = tkinter.Entry(frm,width=18)
en_id.place(x=200, y=150)
# en=enID.get().encode('utf-8')
en_id.config(font=("Saysettha OT",18),width=18)

en_name = tkinter.Entry(frm)
en_name.place(x=600, y=150)
en_name.config(font=("Saysettha OT",18),width=25)

en_surname = tkinter.Entry(frm)
en_surname.place(x=1150, y=150)
en_surname.config(font=("Saysettha OT",18),width=25)

en_email = ttk.Entry(frm)
en_email.place(x=550, y=520)
en_email.config(font=("Saysettha OT", 18))

en_tel = tkinter.Entry(frm)
en_tel.place(x=120, y=520)
en_tel.config(font=("Saysettha OT",18),width=18)

en_degree = tkinter.Entry(frm)
en_degree.place(x=1100, y=520)
en_degree.config(font=("Saysettha OT",18),width=25)

#SET FONT
cbFont = tkfont.Font(family="Saysettha OT", size=16)
#entry
en_village = ttk.Entry(frm)
en_village.place(x=510, y=330)
en_village.config(font=("Saysettha OT", 18))
en_village.option_add("*font", cbFont)

en_district = ttk.Entry(frm)
en_district.place(x=870, y=330)
en_district.config(font=("Saysettha OT", 18))
en_district.option_add("*font", cbFont)

en_province = ttk.Entry(frm)
en_province.place(x=1250, y=330)
en_province.config(font=("Saysettha OT", 18))
en_province.option_add("*font", cbFont)




# RadioButton
v1 = tkinter.IntVar()

rd1 = tkinter.Radiobutton(frm, text="ຊາຍ", variable=v1, value=1)
rd1.place(x=120, y=330)
rd1.config(font=("Saysettha OT", 20),bg="#ECF8DC")

rd2 = tkinter.Radiobutton(frm, text="ຍິງ", variable=v1, value=2)
rd2.place(x=270, y=330)
rd2.config(font=("Saysettha OT", 20),bg="#ECF8DC")

# conn = mysql.connector.connect(user="root", password="", host="Localhost",database="asp_base")
# curs = conn.cursor()
#
# #combobox form database
# curs.execute('select p_Name from tb_province;')
# results = curs.fetchall()
# comboboxProvince = [result[0] for result in results]
#
# #combobox form database
# curs.execute('select d_Name from tb_district;')
# results = curs.fetchall()
# comboboxDistrict = [result[0] for result in results]
#
# #combobox form database
# curs.execute('select v_Name from tb_village;')
# results = curs.fetchall()
# comboboxVillage = [result[0] for result in results]
#



# cbClass = ttk.Combobox(frm, width=18, value=cbList2)
# cbClass.place(x=1250, y=520)
# cbClass.config(font=("Saysettha OT", 18), state="readonly")
# cbClass.current()
# cbClass.option_add("*font", cbFont)

#Button
img1 = PhotoImage(file = f"add.png")
btAdd = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = insert,
    relief = "flat")

btAdd.place(
    x = 900, y = 730,)

img2 = PhotoImage(file = f"back.png")
btBack = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = back,
    relief = "flat")

btBack.place(
    x = 400, y = 730,)


frm.mainloop()
