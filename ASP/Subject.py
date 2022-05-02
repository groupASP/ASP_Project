import pymysql
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

frm = tk.Tk()
frm.title('Database')
frm.geometry('1200x700')
frm.attributes('-fullscreen', True)


connection = pymysql.connect(host='localhost', user='root', password='', db='asp_base')
conn = connection.cursor()

sql = "select * from tb_subject;"
conn.execute(sql)

def save_update():
    txtId.config(state="normal")

    n_id = txtId.get()
    n_name = txtName.get()

    sql_update = "update tb_subject set s_name='"+n_name+"' where s_id='"+n_id+"';"
    conn.execute(sql_update)
    connection.commit()

    for i in tree.get_children():
        tree.delete(i)

    sql_select = "select * from tb_subject;"
    conn.execute(sql_select)

    i=0
    for row in conn:
        tree.insert('', i, text='', values=(row[0], row[1]))
        i += 1

    txtId.delete(0, 'end')
    txtName.delete(0, 'end')
    messagebox.showinfo("ການແກ້ໄຂຂໍ້ມູນ", "ທ່ານໄດ້ແກ້ໄຂຂໍ້ມູນວິຊາຮຽນສຳເລັດແລ້ວ!!!")
    btEdit.config(state="normal")

def update():
    data = tree.selection()
    value = tree.item(data)['values'][0]

    sql_select = "select * from tb_subject where s_Id='"+str(value)+"';"
    conn.execute(sql_select)

    for row in conn:
        o_id = row[0]
        o_name = row[1]

        txtId.insert(0, o_id)
        txtName.insert(0, o_name)
    
    btEdit.config(state="disabled")
    txtId.config(state="disabled")


def delete():
    data = tree.selection()
    value = tree.item(data)['values'][0]

    sql_delete = "delete from tb_subject where s_Id = '"+str(value)+"';"
    conn.execute(sql_delete)
    connection.commit()

    for i in tree.get_children():
        tree.delete(i)

    sql_select = "select * from tb_subject;"
    conn.execute(sql_select)

    i=0
    for row in conn:
        tree.insert('', i, text='', values=(row[0], row[1]))
        i += 1

def open():
    frm.withdraw()
    os.system("D:\ASP_Project\ASP\insert_Subject.py")

def back():
    l = messagebox.askquestion("Back", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າຫຼັກ ຫຼື ບໍ່?")
    if (l == 'yes'):
        frm.withdraw()
        os.system("D:\ASP_Project\ASP\window1.py")

canvas = tk.Canvas(
    frm,
    bg = "#ffffff",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = tk.PhotoImage(file = f"ASP/Image/bg_subject.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)
img1 = tk.PhotoImage(file=f"ASP/Image/add.png")
btAdd = tk.Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=open,
    relief="flat")
btAdd.place(
    x=480, y=700, )

img2 = tk.PhotoImage(file=f"ASP/Image/back.png")
btBack = tk.Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat")
btBack.place(
    x=100, y=700, )

img3 = tk.PhotoImage(file=f"ASP/Image/delete.png")
btDelete = tk.Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=delete,
    relief="flat")
btDelete.place(
    x=1200, y=700, )

img4 = tk.PhotoImage(file=f"ASP/Image/edit.png")
btEdit = tk.Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=update,
    relief="flat")
btEdit.place(
    x=840, y=700, )

img5 = tk.PhotoImage(file=f"ASP/Image/bt_update.png")
btSaveUpdate = tk.Button(
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    command=save_update,
    relief="flat")
btSaveUpdate.place(
    x=1200, y=500, )

st = ttk.Style()
st.theme_use("clam")
st.configure("Treeview.Heading", foreground="blue", font=("Saysettha OT", 16))
st.configure('Treeview', rowheight=50, font=("Saysettha OT", 14))

tree = ttk.Treeview(frm)
tree['columns'] = ('1', '2')

tree.column('#0', width=0)
tree.column('#1', width=100)
tree.column('#2', width=800)

tree.heading('#1', text='ລະຫັດ', anchor='w')
tree.heading('#2', text='ຊື່ວິຊາ', anchor='w')



i = 0
for row in conn:
    tree.insert('', i, text="", values=(row[0], row[1]))
    i = i+1

tree.place(x=150, y=100)

############################################################################

frm.geometry('1600x700')

lb2 = tk.Label(frm, text="ຟອມແກ້ໄຂຂໍ້ມູນວິຊາຮຽນ")
lb2.place(x=1150, y=100)
lb2.configure(font=("Saysettha OT", 20), fg="red", bg="#ECF8DC")

lb2 = tk.Label(frm, text="ລະຫັດວິຊາ:")
lb2.place(x=1100, y=200)
lb2.configure(font=("Saysettha OT", 14), bg="#ECF8DC")

lb3 = tk.Label(frm, text="ຊື່ວິຊາ:")
lb3.place(x=1100, y=270)
lb3.configure(font=("Saysettha OT", 14), bg="#ECF8DC")

txtId = tk.Entry(frm)
txtId.place(x=1230, y=200)
txtId.config(font=("Saysettha OT", 14))

txtName = tk.Entry(frm)
txtName.place(x=1230, y=270)
txtName.config(font=("Saysettha OT", 14))

frm.mainloop()