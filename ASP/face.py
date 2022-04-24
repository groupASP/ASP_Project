from tkinter import *
from tkinter import  messagebox
import  os
import db

# ຄຳສັ່ງເຊື່ອມຕໍ່
connection = db.pymysql.connect(host="Localhost", user="root", password="", database="asp_base")
conn = connection.cursor()


def back():
    l = messagebox.askquestion("BACK","ທ່ານຕ້ອງການຈະກັບໄປໜ້າຫຼັກ ຫຼື ບໍ່?")
    if(l == 'yes'):
        window.withdraw()
        os.system("D:\ASP_Project\ASP\window1.py")
window = Tk()
window.attributes('-fullscreen', True)
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "ASP/Image/bg_face.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)

bt1 = PhotoImage(file="ASP/Image/scan.png")
button_1 = Button(
    image=bt1,
    borderwidth=0,
    highlightthickness=0,
    #command
    relief="flat")
button_1.place(
    x=280.,
    y=300,
    width=259,
    height=246)

bt2 = PhotoImage(file="ASP/Image/train.png")
button_2 = Button(
    image=bt2,
    borderwidth=0,
    highlightthickness=0,
    #command
    relief="flat"
)
button_2.place(
    x=1000,
    y=300,
    width=259,
    height=246
)

bt3= PhotoImage(file="ASP/Image/back.png")
button_3 = Button(
    image=bt3,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
button_3.place(
    x=650,y=720,
    width=246,
    height=90
)
window.resizable(False, False)
window.mainloop()
