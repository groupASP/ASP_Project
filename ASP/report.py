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

def report_today():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\report_today.py")

def report_midterm():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\report_midterm.py")

def report_final():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\report_final.py")

def report_no_qualified():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\report_no_qualified.py")

def report_one():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\report_one_student.py")





def back():
    l = messagebox.askquestion("BACK", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າລາຍງານຫຼັກ ຫຼື ບໍ່?")
    if l == "yes":
        a.withdraw()
        os.system("D:\ASP_Project\ASP\\window1.py")


# button
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
    command=report_today,
    relief="flat",
)
button_1.place(x=100, y=100)

bt2 = PhotoImage(file="ASP/Image/report2.png")
button_2 = Button(
    image=bt2,
    borderwidth=0,
    highlightthickness=0,
    command=report_midterm,
    relief="flat",
)
button_2.place(x=590, y=110)

bt6 = PhotoImage(file="ASP/Image/bt_report_one.png")
button_6 = Button(
    image=bt6,
    borderwidth=0,
    highlightthickness=0,
    command=report_one,
    relief="flat",
)
button_6.place(x=1050, y=100)

bt3 = PhotoImage(file="ASP/Image/report3.png")
button_3 = Button(
    image=bt3,
    borderwidth=0,
    highlightthickness=0,
    command=report_final,
    relief="flat",
)
button_3.place(x=200, y=400)

bt4 = PhotoImage(file="ASP/Image/report4.png")
button_4 = Button(
    image=bt4,
    borderwidth=0,
    highlightthickness=0,
    command=report_no_qualified,
    relief="flat",
)
button_4.place(x=950, y=400)

bt5 = PhotoImage(file="ASP/Image/back.png")
button_5= Button(
    image=bt5,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat",
)
button_5.place(x=650, y=730)


a.mainloop()