from tkinter import *
from tkinter import  messagebox
import os

#fucntion exit
def ex():
   v = messagebox.askquestion("ການອອກຈາກລະບົບ","ທ່ານຕ້ອງການອອກຈາກລະບົບ ຫຼື ບໍ່?")
   if(v == 'yes'):
       exit()
def btn_clicked():
    print("Button Clicked")
#function logout
def logout():
    l = messagebox.askquestion("LOGOUT","ທ່ານຕ້ອງການຈະອອກໄປໜ້າເຂົ້າສູ່ລະບົບ ຫຼື ບໍ່?")
    if(l == 'yes'):
        window1.withdraw()
        os.system("python window.py")
def stu():
    window1.withdraw()
    os.system("python student.py")

window1 = Tk()
window1.attributes('-fullscreen', True)

window1.geometry("1500x780")
window1.configure(bg = "#ffffff")
canvas = Canvas(
    window1,
    bg = "#ffffff",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"bgm.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)

img0 = PhotoImage(file = f"exit.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = ex,
    relief = "flat")

b0.place(
    x = 850, y = 750,
    width = 250,
    height = 73)

img1 = PhotoImage(file = f"logout.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = logout,
    relief = "flat")

b1.place(
    x = 450, y = 750,
    width = 250,
    height = 73)

img2 = PhotoImage(file = f"report.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 1160, y = 520,
    width = 180,
    height = 180)

img3 = PhotoImage(file = f"sub.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 150, y = 520,
    width = 180,
    height = 180)

img4 = PhotoImage(file = f"room.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 1160, y = 300,
    width = 180,
    height = 180)

img5 = PhotoImage(file = f"class.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 660, y = 300,
    width = 180,
    height = 180)

img6 = PhotoImage(file = f"face.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 150, y = 300,
    width = 180,
    height = 180)

img7 = PhotoImage(file = f"attan.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 1160, y = 80,
    width = 180,
    height = 180)

img8 = PhotoImage(file = f"t.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
    x = 660, y = 80,
    width = 180,
    height = 180)

img9 = PhotoImage(file = f"st.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = stu,
    relief = "flat")

b9.place(
    x = 150, y = 80,
    width = 180,
    height = 180)

img10 = PhotoImage(file = f"table.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b10.place(
    x = 660, y = 520,
    width = 180,
    height = 180)
###############################################################################


window1.resizable(False, False)
window1.mainloop()
