from tkinter import *
import tkinter
from tkinter import ttk
import pymysql
from tkinter import messagebox
import os
from datetime import *
from tkinter import font as tkfont

a = tkinter.Tk()
a.geometry("1500x900")
a.attributes("-fullscreen", True)


def back():
    l = messagebox.askquestion("BACK", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າລາຍງານຫຼັກ ຫຼື ບໍ່?")
    if l == "yes":
        a.withdraw()
        os.system("D:\ASP_Project\ASP\\report.py")


# SET FONT
cbFont = tkfont.Font(family="Saysetthar OT", size=20)


canvas = Canvas(
    a, bg="#FFFFFF", height=1080, width=1920, bd=0, highlightthickness=0, relief="ridge"
)
canvas.place(x=0, y=0)

background_img = PhotoImage(file="ASP/Image/bg_report_midterm.png")
background = canvas.create_image(950.0, 540.0, image=background_img)


bt_report = PhotoImage(file="ASP/Image/bt_report1.png")
button_rp = Button(
    image=bt_report,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat",
)
button_rp.place(x=900, y=610)

bt_bcak = PhotoImage(file="ASP/Image/back.png")
button_bk = Button(
    image=bt_bcak,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat",
)
button_bk.place(x=400, y=600)


# connect database
conn = pymysql.connect(user="root", password="", host="Localhost", database="asp_base")
curs = conn.cursor()


# combo_dat
curs.execute("select date from tb_attandance;")
results = curs.fetchall()
combo_date = [result[0] for result in results]

# combobox_date1
cb_date1 = ttk.Combobox(a, width=16, values=combo_date)
cb_date1.place(x=400, y=300)
cb_date1.config(font=(cbFont), state="readonly")
cb_date1.option_add("*font", cbFont)
cb_date1.current()

# combobox_date1
cb_date2 = ttk.Combobox(a, width=16, values=combo_date)
cb_date2.place(x=900, y=300)
cb_date2.config(font=(cbFont), state="readonly")
cb_date2.option_add("*font", cbFont)
cb_date2.current()

a.mainloop()
