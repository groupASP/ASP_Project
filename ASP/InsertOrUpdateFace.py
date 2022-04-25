from tkinter import *
from tkinter import messagebox
import os
import pymysql

frm = Tk()
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
    txt.delete(first=0, last=22)
    txt2.delete(first=0, last=22)
    txt3.delete(first=0, last=22)
    txt.focus()

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
    Name=txt.get()
    Surname=txt2.get()
    S_Id = txt3.get()
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
    l = messagebox.askquestion("BACK","ທ່ານຕ້ອງການຈະກັບໄປໜ້າຫຼັກ ຫຼື ບໍ່?")
    if(l == 'yes'):
        frm.withdraw()
        os.system("D:\ASP_Project\ASP\\face.py")

Notification = Label(frm, text="All things are good", bg="Green", fg="white", width=15,
                height=3, font=('times', 17, 'bold'))



lbl = Label(frm, text="Name:", width=20, height=2, fg="black", bg="snow", font=('times', 15, ' bold '))
lbl.place(x=200, y=200)

txt = Entry(frm, validate="key", width=20, bg="lightblue", fg="red", font=('times', 25, ' bold '))
txt.place(x=550, y=210)

lbl2 = Label(frm, text="Surname:", width=20, fg="black", bg="snow", height=2, font=('times', 15, ' bold '))
lbl2.place(x=200, y=300)

txt2 = Entry(frm, width=20, bg="lightblue", fg="red", font=('times', 25, ' bold '))
txt2.place(x=550, y=310)

lbl3 = Label(frm, text="Surname:", width=20, fg="black", bg="snow", height=2, font=('times', 15, ' bold '))
lbl3.place(x=200, y=400)

txt3 = Entry(frm, width=20, bg="lightblue", fg="red", font=('times', 25, ' bold '))
txt3.place(x=550, y=410)

takeImg = Button(frm, text="Take Images",command=insertOrUpdate, fg="black"  ,bg="lightgreen"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=800, y=500)

back = Button(frm, text="Back",command=back, fg="black"  ,bg="lightgray"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
back.place(x=200, y=500)

clearButton = Button(frm, text="Clear",command=clear,fg="black"  ,bg="deep pink"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=950, y=310)

frm.mainloop()