import pymysql
import tkinter
from tkinter import ttk
import os
from tkinter import  font as tkfont
from tkinter import  messagebox
from tkinter import *

a=tkinter.Tk()
a.attributes('-fullscreen', True)

def ex():
   v = messagebox.askquestion("ການອອກຈາກລະບົບ","ທ່ານຕ້ອງການອອກຈາກລະບົບ ຫຼື ບໍ່?")
   if(v == 'yes'):
       exit()

canvas = Canvas(
    a,
    bg = "#ffffff",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background_edit.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)

img0 = PhotoImage(file = f"back.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = ex,
    relief = "flat")

b0.place(
    x = 100, y = 750,
    width = 290,
    height = 75)

#ເຊື່ອມຕໍ່ຖານຂໍ້ມູນ
connection=pymysql.connect(host="Localhost",user="root",password="",database="cs4b")
conn=connection.cursor()
sql="select * from student;"
conn.execute(sql)

a.resizable(False, False)
a.mainloop()
