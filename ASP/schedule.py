import tkinter
from tkinter import ttk
import os
from tkinter import font as tkfont
from tkinter import messagebox
from tkinter import *
import pymysql

a = tkinter.Tk()
a.geometry("1500x900")

# a.title("display from database")
# a.attributes('-fullscreen', True)

frm = tkinter.Tk()
frm.title("Insert Student")
frm.geometry('1920x1080')

# ຄຳສັ່ງເຊື່ອມຕໍ່
connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
conn = connection.cursor()

sql = "select * from tb_schedule;"
conn.execute(sql)

def back():
    l = messagebox.askquestion("Back", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າຫຼັກ ຫຼື ບໍ່?")
    if (l == 'yes'):
        a.withdraw()
        os.system("D:\ASP_Project\ASP\window1.py")


def save():
    tx11.config(state="normal")
    sc_Id=tx11.get()
    sc_Day=tx22.get()
    sc_Period=tx33.get()
    sc_Year=tx44.get()
    r_Id=tx55.get()
    s_Id=tx66.get()
    st_Id=tx77.get()
    t_Id=tx88.get()

    sql_update ="update tb_schedule set sc_Day='"+sc_Day+"', sc_Period='"+sc_Period+"', sc_Year='"+sc_Year+"', r_Id='"+r_Id+"', s_Id='"+s_Id+"', st_Id='"+st_Id+"', t_Id='"+t_Id+"' where sc_Id='"+str(sc_Id)+"';"
    conn.execute(sql_update)
    connection.commit()

    for i in tree.get_children():
        tree.delete(i)

    sql_select="select * from tb_schedule;"
    conn.execute(sql_select)

    i=0
    for row in conn:
        tree.insert('', i,text="",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        i=i+1


    tx11.delete(0, END)
    tx22.delete(0, END)
    tx33.delete(0, END)
    tx44.delete(0, END)
    tx55.delete(0, END)
    tx66.delete(0, END)
    tx77.delete(0, END)
    tx88.delete(0, END)
    combo.current(0)
    messagebox.showinfo("ການແກ້ໄຂຂໍ້ມູນ", "ທ່ານໄດ້ແກ້ໄຂຂໍ້ມູນນັກສຶກສາສຳເລັດແລ້ວ!!!")

def edit():
    data = tree.selection()
    value = tree.item(data)['values'][0]

    sql_select = "select * from tb_schedule where sc_Id='" + str(value) + "';"
    conn.execute(sql_select)

    for row in conn:
        sc_Id = row[0]
        sc_Day = row[1]
        sc_Period = row[2]
        sc_Year = row[3]
        r_Id = row[4]
        s_Id = row[5]
        st_Id = row[6]
        t_Id = row[7]

        tx11.insert(0, sc_Id)
        tx22.insert(0, sc_Day)
        tx33.insert(0, sc_Period)
        tx44.insert(0, sc_Year)
        tx55.insert(0, r_Id)
        tx66.insert(0, s_Id)
        tx77.insert(0, st_Id)
        tx88.insert(0, t_Id)

        a.withdraw()
        b.deiconify()
        tx11.config(state="disabled")


def delete():
    pm = tree.selection()
    mon = tree.item(pm)['values'][0]
    # print(mon)
    sql_delete = "delete from tb_schedule where sc_Id='" + str(mon) + "';"
    conn.execute(sql_delete)
    connection.commit()

    for i in tree.get_children():
        tree.delete(i)

    sql_select = "select * from tb_schedule;"
    conn.execute(sql_select)

    i = 0
    for row in conn:
        tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        i = i + 1
    messagebox.showinfo("ການສະແດງຜົນ", "ທ່ານໄດ້ລົບຂໍ້ມູນນັກສຶກສາສຳເລັດແລ້ວ!!!")


def insert():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\insert_schedule.py")


canvas = Canvas(
    a,
    bg="#ffffff",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"ASP/Image/bg_sche.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)

img1 = PhotoImage(file=f"ASP/Image/add.png")
btAdd = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=insert,
    relief="flat")
btAdd.place(
    x=480, y=650, )

img2 = PhotoImage(file=f"ASP/Image/back.png")
btBack = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat")
btBack.place(
    x=100, y=650, )

img3 = PhotoImage(file=f"ASP/Image/delete.png")
btDelete = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=delete,
    relief="flat")
btDelete.place(
    x=1200, y=650, )

img4 = PhotoImage(file=f"ASP/Image/edit.png")
btEdit = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=edit,
    relief="flat")
btEdit.place(
    x=840, y=650, )

st = ttk.Style()
st.theme_use("clam")
st.configure("Treeview.Heading", fg="blue", font=("Saysettha OT", 14))
st.configure("Treeview", rowheight=50, font=("Saysettha OT", 12))


tree = ttk.Treeview(a)
tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
tree.column("#0", width=5)
tree.column("#1", width=100)
tree.column("#2", width=180)
tree.column("#3", width=180)
tree.column("#4", width=180)
tree.column("#5", width=180)
tree.column("#6", width=180)
tree.column("#7", width=180)

tree.heading("#1", text="ລະຫັດ")
tree.heading("#2", text="ມື້")
tree.heading("#3", text="ຄາບຮຽນ")
tree.heading("#4", text="ສົກຮຽນ")
tree.heading("#5", text="ລະຫັດຫ້ອງ")
tree.heading("#6", text="ລະຫັດວິຊາ")
tree.heading("#7", text="ລະຫັດນັກສຶກສາ")
tree.heading("#8", text="ລະຫັດອາຈານ")

# ຄຳສັ່ງສະແດງຜົນ

i = 0
for row in conn:
    tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    i = i + 1
tree.place(x=30, y=80)

############################################################################################################
############################################################################################################

# ໜ້າທີ່2
b = tkinter.Tk()
b.geometry("1500x900")
b.config(bg="#ECF8DC")
b.attributes('-fullscreen', True)
b.withdraw()

lbShow = tkinter.Label(b, text="ແກ້ໄຂຂໍ້ມູນ")
lbShow.pack(side='top', fill='x')
lbShow.configure(font=("Saysettha OT", 30), bg="#04C582", fg="white")

def ex():
    exit()

def back1():
    tx11.delete(0, END)
    tx22.delete(0, END)
    tx33.delete(0, END)
    tx44.delete(0, END)
    tx55.delete(0, END)
    tx66.delete(0, END)
    tx77.delete(0, END)
    tx88.delete(0, END)
    a.deiconify()
    b.withdraw()

lb11 = tkinter.Label(b, text="ລະຫັດນັກສຶກສາ:")
lb11.place(x=20, y=150)
lb11.config(font=("Saysettha OT", 18), bg="#ECF8DC")

lb22 = tkinter.Label(b, text="ຊື່:")
lb22.place(x=550, y=150)
lb22.config(font=("Saysettha OT", 18), bg="#ECF8DC")

lb33 = tkinter.Label(b, text="ນາມສະກຸນ:")
lb33.place(x=1000, y=150)
lb33.config(font=("Saysettha OT", 18), bg="#ECF8DC")

lb44 = tkinter.Label(b, text="ເພດ:")
lb44.place(x=20, y=330)
lb44.config(font=("Saysettha OT", 20), bg="#ECF8DC")

lb55 = tkinter.Label(b, text="ວັນເດືອນປີເກີດ:")
lb55.place(x=480, y=330)
lb55.config(font=("Saysettha OT", 18), bg="#ECF8DC")

lb66 = tkinter.Label(b, text="ເບີໂທ:")
lb66.place(x=1050, y=330)
lb66.config(font=("Saysettha OT", 18), bg="#ECF8DC")

lb77 = tkinter.Label(b, text="ບ້ານ:")
lb77.place(x=30, y=520)
lb77.config(font=("Saysettha OT", 18), bg="#ECF8DC")

lb88 = tkinter.Label(b, text="ເມືອງ:")
lb88.place(x=410, y=520)
lb88.config(font=("Saysettha OT", 18), bg="#ECF8DC")

lb99 = tkinter.Label(b, text="ແຂວງ:")
lb99.place(x=800, y=520)
lb99.config(font=("Saysettha OT", 18), bg="#ECF8DC")

###entryyyyy

tx11 = tkinter.Entry(b)
tx11.place(x=200, y=150)
tx11.config(font=("Saysettha OT", 18),width=18)

tx22 = tkinter.Entry(b)
tx22.place(x=600, y=150)
tx22.config(font=("Saysettha OT", 18),width=18)

tx33 = tkinter.Entry(b)
tx33.place(x=1150, y=150)
tx33.config(font=("Saysettha OT", 18),width=18)

tx44 = tkinter.Entry(b)
tx44.place(x=650, y=330)
tx44.config(font=("Saysettha OT", 18),width=18)

tx55 = tkinter.Entry(b)
tx55.place(x=1150, y=330)
tx55.config(font=("Saysettha OT", 18),width=18)

tx66 = tkinter.Entry(b)
tx66.place(x=110, y=520)
tx66.config(font=("Saysettha OT", 18),width=18)

tx77 = tkinter.Entry(b)
tx77.place(x=490, y=520)
tx77.config(font=("Saysettha OT", 18),width=18)

tx88 = tkinter.Entry(b)
tx88.place(x=890, y=520)
tx88.config(font=("Saysettha OT", 18),width=18)

######combo
cbList = ["ຊາຍ", "ຍິງ"]
cbfont=tkfont.Font(family="Saysettha OT", size=20)

combo = ttk.Combobox(b, width=15,value=cbList)
combo.place(x=150, y=330)
combo.configure(font=("Saysettha OT", 20),state="readonly")
combo.current(0)
combo.option_add("*font", cbfont)

# button
bts = tkinter.Button(b, text="Update",command=save,width=20)
bts.place(x=900, y=650)
bts.configure(font=("Saysettha OT", 18), bg="green", fg="white")

bt = tkinter.Button(b, text="BACK",command=back1,width=20)
bt.place(x=300, y=650)
bt.configure(font=("Saysettha OT", 18), bg="gray", fg="black")




a.mainloop()