import tkinter
from tkinter import font as tkfont
import os
import db
from tkinter import messagebox
from tkinter import *

frm = tkinter.Tk()
frm.title("Insert Room")
frm.geometry('1920x1080')
frm.attributes('-fullscreen', True)

def insert():
    conn = db.connection.cursor()
    connection = db.connection.commit()
    r_Id = en.get()
    r_Name = en1.get()
    value = messagebox.askquestion("ການຢືນຢັນ", "ທ່ານຕ້ອງການເພີ່ມຂໍ້ມູນແທ້ຫຼືບໍ່?")
    if(value == 'yes'):
        sql_insert = "insert into tb_room values('"+r_Id+"','"+r_Name+"');"
        conn.execute(sql_insert)
        connection
        messagebox.showinfo("ການສະແດງຜົນ","ທ່ານໄດ້ເພີ່ມຂໍ້ມູນສຳເລັດແລ້ວ")
    en.delete(0,END)
    en1.delete(0,END)

def back():
    l = messagebox.askquestion("Back","ທ່ານຕ້ອງການຈະກັບໄປໜ້າຂໍ້ມູນຊັ້ນຮຽນ ຫຼື ບໍ່?")
    if(l == 'yes'):
        frm.withdraw()
        os.system("D:\ASP_Project\Proxlight_Designer_Export\Room.py")



canvas = Canvas(
    frm,
    bg = "#ffffff",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Proxlight_Designer_Export/Image/bg_insert.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)


lb1 = tkinter.Label(frm, text="ລະຫັດຫ້ອງຮຽນ:")
lb1.place(x=20, y=150)
lb1.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb2 = tkinter.Label(frm, text="ຊື່ຫ້ອງຮຽນ:")
lb2.place(x=20, y=300)
lb2.config(font=("Saysettha OT", 18),bg="#ECF8DC")

# Entry
en = tkinter.Entry(frm,width=18)
en.place(x=200, y=150)
en.config(font=("Saysettha OT",18),width=18)

en1 = tkinter.Entry(frm)
en1.place(x=200, y=300)
en1.config(font=("Saysettha OT",18),width=25)


#Button
img1 = PhotoImage(file = f"Proxlight_Designer_Export/Image/add.png")
btAdd = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = insert,
    relief = "flat")

btAdd.place(
    x = 900, y = 650,)

img2 = PhotoImage(file = f"Proxlight_Designer_Export/Image/back.png")
btBack = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = back,
    relief = "flat")

btBack.place(
    x = 400, y = 650,)


frm.mainloop()