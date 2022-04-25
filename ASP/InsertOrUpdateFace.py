from tkinter import *
from tkinter import messagebox
import os
import pymysql

frm = Tk()
frm.geometry("1500x900")
frm.attributes("-fullscreen", True)
frm.configure(background='snow')


# def err_screen1():
#     global sc2
#     sc2 = Tk()
#     sc2.geometry('300x100')
#     sc2.iconbitmap('AMS.ico')
#     sc2.title('Warning!!')
#     sc2.configure(background='snow')
#     Label(sc2,text='Please enter your subject name!!!',fg='red',bg='white',font=('times', 16, ' bold ')).pack()
#     Button(sc2,text='OK',command=del_sc2,fg="black"  ,bg="lawn green"  ,width=9  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold ')).place(x=90,y= 50)
# def del_sc2():
#     sc2.destroy()
def clear():
    en_id.delete(first=0, last=22)
    en_name.delete(first=0, last=22)
    en_surname.delete(first=0, last=22)
    en_id.focus()

def getId():
    connection = pymysql.connect(host="localhost", user="root", password="", database="asp_base")
    conn = connection.cursor()
    sql = "SELECT F_ID FROM tb_face order by F_ID desc limit 1;"
    conn.execute(sql)
    profile=None
    for row in conn:
        profile=row
    connection.close()
    c = int(''.join(map(str, profile)))
    return c

def insertOrUpdate():
    import cv2

    oid = getId()
    Id = oid+1
    Name=en_name.get()
    Surname=en_surname.get()
    S_Id = en_id.get()
    faceDetect = cv2.CascadeClassifier('ASP/Detect/haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    connection = pymysql.connect(host="localhost", user="root", password="", database="asp_base")
    conn = connection.cursor()
    sql = "Select * from tb_face;"
    conn.execute(sql)

    sql="Insert into tb_face(F_ID, Name, SURNAME, S_ID) values('"+str(Id)+"', '"+str(Name)+"', '"+str(Surname)+"', '"+str(S_Id)+"');"
    conn.execute(sql)
    connection.commit()
    conn.close()
    SampleNum = 0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            SampleNum=SampleNum+1
            cv2.imwrite("ASP/ImageData/ "+Name+"."+Surname+"."+str(Id)+"."+str(SampleNum)+".jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.waitKey(100)
        cv2.imshow("Face", img)
        cv2.waitKey(1)
        if(SampleNum>120):
            break
    cam.release()
    cv2.destroyAllWindows()

def back():
    l = messagebox.askquestion("BACK","ທ່ານຕ້ອງການຈະກັບໄປໜ້າຂໍ້ມູນໃບໜ້າ ຫຼື ບໍ່?")
    if(l == 'yes'):
        frm.withdraw()
        os.system("D:\ASP_Project\ASP\\face.py")

Notification = Label(frm, text="All things are good", bg="Green", fg="white", width=15,
                height=3, font=('times', 17, 'bold'))





#button
canvas = Canvas(
    frm,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "ASP/Image/bg_insert_face.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)

bt1 = PhotoImage(file="ASP/Image/bt_clear.png")
button_1 = Button(
    image=bt1,
    borderwidth=0,
    highlightthickness=0,
    command=clear,
    relief="flat")
button_1.place(
    x=1100.,
    y=300,
    width=220,
    height=80)

bt2 = PhotoImage(file="ASP/Image/bt_takeImage.png")
button_2 = Button(
    image=bt2,
    borderwidth=0,
    highlightthickness=0,
    command=insertOrUpdate,
    relief="flat"
)
button_2.place(
    x=900,
    y=600,
    width=272,
    height=95
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
    x=200,
    y=600,
    width=246,
    height=90
)

#label
lb1 = Label(frm, text="ຊື່ນັກສຶກສາ:")
lb1.place(x=250, y=200)
lb1.config(font=("Saysettha OT", 20),bg="#ECF8DC")

lb2 = Label(frm, text="ນາມສະກຸນນັກສຶກສາ:")
lb2.place(x=250, y=300)
lb2.config(font=("Saysettha OT", 20),bg="#ECF8DC")

lb3 = Label(frm, text="ລະຫັດນັກສຶກສາ:")
lb3.place(x=250, y=400)
lb3.config(font=("Saysettha OT", 20),bg="#ECF8DC")

#entry
en_name = Entry(frm)
en_name.place(x=550, y=210)
en_name.config(font=("Saysettha OT",18),width=30)

en_surname = Entry(frm)
en_surname.place(x=550, y=310)
en_surname.config(font=("Saysettha OT",18),width=30)

en_id = Entry(frm)
en_id.place(x=550, y=410)
en_id.config(font=("Saysettha OT",18),width=30)

frm.mainloop()