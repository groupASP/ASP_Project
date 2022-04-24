from tkinter import *
from tkinter import  messagebox
import  os

window = Tk()

window.geometry("1200x700")
window.configure(bg = "#ffffff")
window.title("LOGIN")

def showpw():
    if(var1.get()==1):
        entry1.config(show="")
    else:
        entry1.config(show="*")

def login():
    user = "admin"
    pw = "1234"

    txtu = entry0.get()
    txtp = entry1.get()

    if(txtu == "") or (txtp == ""):
        messagebox.showerror("LOGIN!!!", "Please input User and Password")

    elif(txtu == user) and (txtp == pw):
        window.withdraw()
        os.system("D:\ASP_Project\ASP\window1.py")


    elif(txtu != user) and (txtp != pw):
        messagebox.showerror("LOGIN!!!", "Your User and Password incorrect!!!")
        entry0.delete(0, 'end')
        entry1.delete(0, 'end')
        entry0.focus()


    elif(txtu != user):
        messagebox.showerror("LOGIN!!!", "Your User incorrect!!!")
        entry0.delete(0, 'end')
        entry0.focus()


    elif(txtp != pw):
        messagebox.showerror("LOGIN!!!", "Your Password incorrect!!!")
        entry1.delete(0, 'end')
        entry1.focus()
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 700,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"ASP/Image/background_login.png")
background = canvas.create_image(
    600.0, 337.5,
    image=background_img)

img0 = PhotoImage(file = f"ASP/Image/login.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = login,
    relief = "flat")

b0.place(
    x = 111, y = 578,
    width = 392,
    height = 62)

entry0_img = PhotoImage(file = f"ASP/Image/img_textBox0.png")
entry0_bg = canvas.create_image(
    305.5, 357.0,
    image = entry0_img)

entry0 = Entry(
    font=("Times New Roman",20),
    bd = 0,
    bg = "#e5e5e5",
    highlightthickness = 0)

entry0.place(
    x = 118.0, y = 327,
    width = 375.0,
    height = 58)

entry1_img = PhotoImage(file = f"ASP/Image/img_textBox1.png")
entry1_bg = canvas.create_image(
    305.5, 473.0,
    image = entry1_img)

entry1 = Entry(
    font=("Times New Roman",20),
    bd = 0,
    bg = "#e5e5e5",
    highlightthickness = 0)

entry1.place(
    x = 118.0, y = 443,
    width = 375.0,
    height = 58)
entry1.config(show='*')


#checkBotton
var1 = IntVar()

cb1 = Checkbutton(window, text="Show Password", variable=var1, onvalue=1, offvalue=0, command=showpw)
cb1.place(x=118, y=510)
cb1.configure(font=("Times New Roman", 16), bg="#E27676",fg="white")

window.resizable(False, False)
window.mainloop()
