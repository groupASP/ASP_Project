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
a.attributes('-fullscreen', True)

# ຄຳສັ່ງເຊື່ອມຕໍ່
connection = pymysql.connect(host="localhost", user="root", password="", db="asp_base")
conn = connection.cursor()

sql = "select* from tb_teacher"
conn.execute(sql)


def back():
    l = messagebox.askquestion("Back", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າຫຼັກ ຫຼື ບໍ່?")
    if (l == 'yes'):
        a.withdraw()
        os.system("D:\ASP_Project\ASP\window1.py")


def save():
    global t_Gender
    en_id.config(state="normal")
    t_Id=en_id.get()
    t_Name=en_name.get()
    t_Surname=en_surname.get()
    t_Village=en_village.get()
    t_District=en_district.get()
    t_Province=en_province.get()
    t_Tel=en_tel.get()
    t_Email=en_email.get()
    t_Degree=en_degree.get()
    t_Gender=combo.get()
    sql_update ="update tb_teacher set t_Name='"+t_Name+"',t_Surname='"+t_Surname+"',t_Gender='"+t_Gender+"',t_Village='"+t_Village+"',t_District='"+t_District+"',t_Province='"+t_Province+"',t_Tel='"+t_Tel+"',t_Email='"+t_Email+"',t_Degree='"+t_Degree+"' where t_Id='"+t_Id+"';"
    conn.execute(sql_update)
    connection.commit()

    for i in tree.get_children():
        tree.delete(i)

    sql_select="select * from tb_teacher;"
    conn.execute(sql_select)

    i=0
    for row in conn:
        tree.insert('', i,text="",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
        i=i+1

    # sc =tkinter.Label(a, text="Edit successfully!!!!!!")
    # sc.pack()
    # sc.config(font=("Times New Roman", 30), fg="red",bg="#04C582")
    en_id.delete(0, END)
    en_name.delete(0, END)
    en_surname.delete(0, END)
    en_village.delete(0, END)
    en_district.delete(0, END)
    en_province.delete(0, END)
    en_tel.delete(0, END)
    en_email.delete(0, END)
    en_degree.delete(0, END)
    messagebox.showinfo("ການແກ້ໄຂຂໍ້ມູນ", "ທ່ານໄດ້ແກ້ໄຂຂໍ້ມູນນັກສຶກສາສຳເລັດແລ້ວ!!!")

def edit():
    data = tree.selection()
    value = tree.item(data)['values'][0]

    sql_select = "select * from tb_teacher where t_Id='" + value + "';"
    conn.execute(sql_select)

    for row in conn:
        t_Id = row[0]
        t_Name = row[1]
        t_Surname = row[2]
        t_Gender = row[3]
        t_Village = row[4]
        t_District = row[5]
        t_Province = row[6]
        t_Tel = row[7]
        t_Email = row[8]
        t_Degree = row[9]

        en_id.insert(0, t_Id)
        en_name.insert(0, t_Name)
        en_surname.insert(0, t_Surname)
        en_village.insert(0, t_Village)
        en_district.insert(0, t_District)
        en_province.insert(0, t_Province)
        en_tel.insert(0, t_Tel)
        en_email.insert(0, t_Email)
        en_degree.insert(0, t_Degree)
    
        #####ເພດ
        cbList = ["ຊາຍ", "ຍິງ"]
        if(t_Gender == cbList[0]):
            combo.current(0)

        elif(t_Gender == cbList[1]):
            combo.current(1)

        a.withdraw()
        b.deiconify()
        en_id.config(state="disabled")


def delete():
    pm = tree.selection()
    mon = tree.item(pm)['values'][0]
    # print(mon)
    sql_delete = "delete from tb_teacher where t_Id='" + mon + "';"
    conn.execute(sql_delete)
    connection.commit()


    for i in tree.get_children():
        tree.delete(i)

    sql_select = "select * from tb_student;"
    conn.execute(sql_select)

    i = 0
    for row in conn:
        tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
        i = i + 1
    messagebox.showinfo("ການສະແດງຜົນ", "ທ່ານໄດ້ລົບຂໍ້ມູນນັກອາຈານສຳເລັດແລ້ວ!!!")


def insert():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\insert_teacher.py")


'''lb=tkinter.Label(a,text="ລາຍຊື່ນັກສຶກສາ")
lb.place(x=50,y=20)
lb.config(font=("Saysettha OT",20),fg="red")'''
canvas = Canvas(
    a,
    bg="#ffffff",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"ASP/Image/bg_teach.png")
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


sql = "select* from tb_teacher"
conn.execute(sql)

tree = ttk.Treeview(a)
tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
tree.column("#0", width=1)
tree.column("#1", width=100)
tree.column("#2", width=150)
tree.column("#3", width=180)
tree.column("#4", width=60)
tree.column("#5", width=150)
tree.column("#6", width=150)
tree.column("#7", width=180)
tree.column("#8", width=150)
tree.column("#9", width=180)
tree.column("#10", width=180)

tree.heading("#1", text="ລະຫັດ")
tree.heading("#2", text="ຊື່")
tree.heading("#3", text="ນາມສະກຸນ")
tree.heading("#4", text="ເພດ")
tree.heading("#5", text="ບ້ານ")
tree.heading("#6", text="ເມືອງ")
tree.heading("#7", text="ແຂວງ")
tree.heading("#8", text="ເບີໂທ")
tree.heading("#9", text="ອີເມວ")
tree.heading("#10", text="ລະດັບການສຶກສາ")

# ຄຳສັ່ງສະແດງຜົນ

i = 0
for row in conn:
    tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    i = i + 1
tree.place(x=1, y=80)

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
# lbShow.place(x=1,y=1000)
lbShow.configure(font=("Saysettha OT", 30), bg="#04C582", fg="white")

def ex():
    exit()

def back1():
    en_id.delete(0, END)
    en_name.delete(0, END)
    en_surname.delete(0, END)
    en_village.delete(0, END)
    en_district.delete(0, END)
    en_province.delete(0, END)
    en_tel.delete(0, END)
    en_email.delete(0, END)
    en_degree.delete(0, END)
    a.deiconify()
    b.withdraw()

lb_id = tkinter.Label(b, text="ລະຫັດອາຈານ:")
lb_id.place(x=20, y=150)
lb_id.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb_name = tkinter.Label(b, text="ຊື່:")
lb_name.place(x=530, y=150)
lb_name.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb_surname = tkinter.Label(b, text="ນາມສະກຸນ:")
lb_surname.place(x=980, y=150)
lb_surname.config(font=("Saysettha OT", 18),bg="#ECF8DC")


lb_gender = tkinter.Label(b, text="ເພດ:")
lb_gender.place(x=20, y=330)
lb_gender.config(font=("Saysettha OT", 20),bg="#ECF8DC")

lb_village = tkinter.Label(b, text="ບ້ານ:")
lb_village.place(x=430, y=330)
lb_village.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb_district = tkinter.Label(b, text="ເມືອງ:")
lb_district.place(x=800, y=330)
lb_district.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb_province = tkinter.Label(b, text="ແຂວງ:")
lb_province.place(x=1170, y=330)
lb_province.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb_tel = tkinter.Label(b, text="ເບີໂທ:")
lb_tel.place(x=20, y=520)
lb_tel.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb_email = tkinter.Label(b, text="ອີເມວ:")
lb_email.place(x=450, y=520)
lb_email.config(font=("Saysettha OT", 18),bg="#ECF8DC")

lb_degree = tkinter.Label(b, text="ລະດັບການສຶກສາ:")
lb_degree.place(x=920, y=520)
lb_degree.config(font=("Saysettha OT", 18),bg="#ECF8DC")

###entryyyyy
# Entry
en_id = tkinter.Entry(b,width=18)
en_id.place(x=200, y=150)
en_id.config(font=("Saysettha OT",18),width=18)

en_name = tkinter.Entry(b)
en_name.place(x=600, y=150)
en_name.config(font=("Saysettha OT",18),width=25)

en_surname = tkinter.Entry(b)
en_surname.place(x=1150, y=150)
en_surname.config(font=("Saysettha OT",18),width=25)

en_email = ttk.Entry(b)
en_email.place(x=550, y=520)
en_email.config(font=("Saysettha OT", 18))

en_tel = tkinter.Entry(b)
en_tel.place(x=120, y=520)
en_tel.config(font=("Saysettha OT",18),width=18)

en_degree = tkinter.Entry(b)
en_degree.place(x=1100, y=520)
en_degree.config(font=("Saysettha OT",18),width=25)

#SET FONT
cbFont = tkfont.Font(family="Saysettha OT", size=16)
#entry
en_village = ttk.Entry(b)
en_village.place(x=510, y=330)
en_village.config(font=("Saysettha OT", 18))
en_village.option_add("*font", cbFont)

en_district = ttk.Entry(b)
en_district.place(x=870, y=330)
en_district.config(font=("Saysettha OT", 18))
en_district.option_add("*font", cbFont)

en_province = ttk.Entry(b)
en_province.place(x=1250, y=330)
en_province.config(font=("Saysettha OT", 18))
en_province.option_add("*font", cbFont)

######combo
cbList = ["ຊາຍ", "ຍິງ"]
cbfont=tkfont.Font(family="ASP/font/Saysettha OT", size=20)

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