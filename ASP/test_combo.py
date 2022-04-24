from tkinter import *
import tkinter
from tkinter import ttk
import mysql.connector
from tkinter import font as tkfont
import db

a=tkinter.Tk()
a.geometry("1500x900")

#connect database
conn = mysql.connector.connect(user="root", password="", host="Localhost",database="asp_base")
curs = conn.cursor()

#combobox form database
curs.execute('select p_Name from tb_province;')
results = curs.fetchall()
for_combobox1 = [result[0] for result in results]

#combobox form database
curs.execute('select d_Name from tb_district;')
results = curs.fetchall()
for_combobox2 = [result[0] for result in results]

#set font
cbFont = tkfont.Font(family="Saysettha OT", size=16)

#combobox1
cb = ttk.Combobox(a, width=25, value=for_combobox1)
cb.place(x=250, y=520)
cb.config(font=(cbFont), state="readonly")
cb.option_add("*font", cbFont)
cb.current()

#combobox2
cb1 = ttk.Combobox(a, width=25, value=for_combobox2)
cb1.place(x=700, y=520)
cb1.config(font=(cbFont), state="readonly")
cb1.option_add("*font", cbFont)
cb1.current()


a.mainloop()
