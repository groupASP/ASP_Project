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


def logout():
    l = messagebox.askquestion("LOGOUT", "ທ່ານຕ້ອງການຈະອອກໄປໜ້າເຂົ້າສູ່ລະບົບ ຫຼື ບໍ່?")
    if l == "yes":
        a.withdraw()
        os.system("D:\ASP_Project\ASP\\window.py")


def ex():
    v = messagebox.askquestion("ການອອກຈາກລະບົບ", "ທ່ານຕ້ອງການອອກຈາກລະບົບ ຫຼື ບໍ່?")
    if v == "yes":
        exit()


canvas = Canvas(
    a, bg="#FFFFFF", height=1080, width=1920, bd=0, highlightthickness=0, relief="ridge"
)

canvas.place(x=0, y=0)

background_img = PhotoImage(file="ASP/Image/bg_report.png")
background = canvas.create_image(950.0, 540.0, image=background_img)

bt1 = PhotoImage(file="ASP/Image/report1.png")
button_1 = Button(
    image=bt1,
    borderwidth=0,
    highlightthickness=0,
    # command=check_in,
    relief="flat",
)
button_1.place(x=200, y=100)

bt2 = PhotoImage(file="ASP/Image/report2.png")
button_2 = Button(
    image=bt2,
    borderwidth=0,
    highlightthickness=0,
    # command=Exit_Room,
    relief="flat",
)
button_2.place(x=950, y=100)

bt3 = PhotoImage(file="ASP/Image/report3.png")
button_3 = Button(
    image=bt3,
    borderwidth=0,
    highlightthickness=0,
    # command=auto_att,
    relief="flat",
)
button_3.place(x=200, y=400)

bt4 = PhotoImage(file="ASP/Image/report4.png")
button_4 = Button(
    image=bt4,
    borderwidth=0,
    highlightthickness=0,
    # command=auto_att,
    relief="flat",
)
button_4.place(x=950, y=400)

img1 = PhotoImage(file=f"ASP/Image/logout.png")
b1 = Button(
    image=img1, borderwidth=0, highlightthickness=0, command=logout, relief="flat"
)

b1.place(
    x=450,
    y=750,
)

img0 = PhotoImage(file=f"ASP/Image/exit.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=ex, relief="flat")

b0.place(
    x=850,
    y=750,
)

a.mainloop()
