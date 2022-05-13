from tkinter import *
import tkinter
import pymysql
from tkinter import ttk
from tkinter import font as tkfont

a = tkinter.Tk()
a.geometry("1500x900")

# connect database
conn = pymysql.connect(user="root", password="", host="Localhost", database="asp_base")
curs = conn.cursor()

curs.execute("select * from tb_room;")
results = curs.fetchall()
combo_r_id = [result[0] for result in results]
combo_r_name = [result[1] for result in results]

variable = StringVar(a)
variable.set(combo_r_name[0])

w = OptionMenu(a, variable, *combo_r_id)
w.pack()


a.mainloop()
