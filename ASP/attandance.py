from tkinter import *
import tkinter
from tkinter import ttk
import pymysql
from tkinter import messagebox
import os
from datetime import *

a = tkinter.Tk()
a.geometry("1500x900")
a.attributes("-fullscreen", True)


# def auto_att():
#     import cv2
#     import pymysql

#     faceDetect = cv2.CascadeClassifier("ASP/Detect/haarcascade_frontalface_default.xml")
#     cam = cv2.VideoCapture(0)
#     rec = cv2.face.LBPHFaceRecognizer_create()
#     rec.read("ASP\\Data\\trainingImage.yml")
#     fontface = cv2.FONT_HERSHEY_SIMPLEX
#     fontScale = 2
#     fontColor = (255, 0, 0)
#     try:

#         def auto():
#             def getProfile(Id):
#                 connection = pymysql.connect(
#                     host="localhost", user="root", password="", database="asp_base"
#                 )
#                 conn = connection.cursor()
#                 sql = (
#                     "select st.st_Id, st.st_Name, st.st_Surname, d.d_Name, s.s_Name, \
#                     r.r_Name, cl.cl_Name, sc.sc_Period, sc.sc_Year, f.Name, f.Surname\
#                     from tb_face f inner join tb_student st on f.st_Id = st.st_Id\
#                     inner join tb_class cl on st.cl_Id = cl.cl_Id\
#                     inner join tb_schedule sc on sc.cl_Id=cl.cl_Id\
#                     inner join tb_day d on d.d_Id=sc.d_Id\
#                     inner join tb_subject s on s.s_Id=sc.s_Id\
#                     inner join tb_room r on r.r_Id=sc.r_Id\
#                     where f_Id = '"
#                     + str(Id)
#                     + "';"
#                 )
#                 conn.execute(sql)
#                 profile = None
#                 for row in conn:
#                     profile = row
#                 conn.close()
#                 return profile

#             while True:
#                 ret, img = cam.read()
#                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                 faces = faceDetect.detectMultiScale(gray, 1.3, 5)
#                 for (x, y, w, h) in faces:
#                     Id, conf = rec.predict(gray[y : y + h, x : x + w])
#                     if conf < 38:
#                         print(conf)
#                         global profile
#                         profile = getProfile(Id)
#                         if profile != None:
#                             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                             cv2.putText(
#                                 img,
#                                 str(profile[9]),
#                                 (x, y + h + 30),
#                                 fontface,
#                                 fontScale,
#                                 fontColor,
#                             )
#                             cv2.putText(
#                                 img,
#                                 str(profile[10]),
#                                 (x, y + h + 80),
#                                 fontface,
#                                 fontScale,
#                                 fontColor,
#                             )
#                     else:
#                         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                         cv2.putText(
#                             img,
#                             "Unknown",
#                             (x, y + h + 30),
#                             fontface,
#                             fontScale,
#                             fontColor,
#                         )
#                 cv2.imshow("Face", img)
#                 key = cv2.waitKey(1) & 0xFF == ord("q")
#                 if key or conf <= 38:
#                     break
#             try:
#                 connection = pymysql.connect(
#                     host="localhost", user="root", password="", database="asp_base"
#                 )
#                 conn = connection.cursor()
#                 if str(profile[5]) == "309" and str(profile[6]) == "CS6B":
#                     time = datetime.now().strftime("%H:%M:%S")
#                     date_Today = datetime.now().strftime("%Y-%m-%d")

#                     insert_data = "INSERT INTO tb_attandance(a_Id, st_Id, Name, Surname, d_Name, s_Name, r_Name, cl_Name, sc_Period, sc_Year, time_In, date) VALUES (0, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
#                     VALUES = (
#                         str(profile[0]),
#                         str(profile[1]),
#                         str(profile[2]),
#                         str(profile[3]),
#                         str(profile[4]),
#                         str(profile[5]),
#                         str(profile[6]),
#                         str(profile[7]),
#                         str(profile[8]),
#                         time,
#                         date_Today,
#                     )
#                     conn.execute(insert_data, VALUES)
#                     connection.commit()
#             except Exception as e:
#                 print(e)

#             cam.release()
#             cv2.destroyAllWindows()

#         auto()
#     except Exception as e:
#         print(e)


# def Exit_Room():
#     import cv2
#     import pymysql

#     faceDetect = cv2.CascadeClassifier("ASP/Detect/haarcascade_frontalface_default.xml")
#     cam = cv2.VideoCapture(0)
#     rec = cv2.face.LBPHFaceRecognizer_create()
#     rec.read("ASP\\Data\\trainingImage.yml")
#     fontface = cv2.FONT_HERSHEY_SIMPLEX
#     fontScale = 2
#     fontColor = (255, 0, 0)
#     try:

#         def auto():
#             def getProfile(Id):
#                 connection = pymysql.connect(
#                     host="localhost", user="root", password="", database="asp_base"
#                 )
#                 conn = connection.cursor()
#                 sql = (
#                     "select st.st_Id, st.st_Name, st.st_Surname, d.d_Name, s.s_Name, \
#                     r.r_Name, cl.cl_Name, sc.sc_Period, sc.sc_Year, f.Name, f.Surname\
#                     from tb_face f inner join tb_student st on f.st_Id = st.st_Id\
#                     inner join tb_class cl on st.cl_Id = cl.cl_Id\
#                     inner join tb_schedule sc on sc.cl_Id=cl.cl_Id\
#                     inner join tb_day d on d.d_Id=sc.d_Id\
#                     inner join tb_subject s on s.s_Id=sc.s_Id\
#                     inner join tb_room r on r.r_Id=sc.r_Id\
#                     where f_Id = '"
#                     + str(Id)
#                     + "';"
#                 )
#                 conn.execute(sql)
#                 profile = None
#                 for row in conn:
#                     profile = row
#                 conn.close()
#                 return profile

#             while True:
#                 ret, img = cam.read()
#                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                 faces = faceDetect.detectMultiScale(gray, 1.3, 5)
#                 for (x, y, w, h) in faces:
#                     Id, conf = rec.predict(gray[y : y + h, x : x + w])
#                     if conf < 38:
#                         print(conf)
#                         global profile
#                         profile = getProfile(Id)
#                         if profile != None:
#                             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                             cv2.putText(
#                                 img,
#                                 str(profile[9]),
#                                 (x, y + h + 30),
#                                 fontface,
#                                 fontScale,
#                                 fontColor,
#                             )
#                             cv2.putText(
#                                 img,
#                                 str(profile[10]),
#                                 (x, y + h + 80),
#                                 fontface,
#                                 fontScale,
#                                 fontColor,
#                             )
#                     else:
#                         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                         cv2.putText(
#                             img,
#                             "Unknown",
#                             (x, y + h + 30),
#                             fontface,
#                             fontScale,
#                             fontColor,
#                         )
#                 cv2.imshow("Face", img)
#                 key = cv2.waitKey(1) & 0xFF == ord("q")
#                 if key or conf <= 38:
#                     break
#             try:
#                 connection = pymysql.connect(
#                     host="localhost", user="root", password="", database="asp_base"
#                 )
#                 conn = connection.cursor()
#                 time = datetime.now().strftime("%H:%M:%S")
#                 date_Today = datetime.now().strftime("%Y-%m-%d")
#                 st_Id = str(profile[0])
#                 r_Name = str(profile[5])
#                 cl_Name = str(profile[6])

#                 update_data = " UPDATE tb_attandance set time_Out = '"+time+"' where st_Id = '"+str(st_Id)+"' and r_Name = '"+str(r_Name)+"' and cl_Name = '"+str(cl_Name)+"' and date = '"+date_Today+"';"
#                 conn.execute(update_data)
#                 connection.commit()
#             except Exception as e:
#                 print(e)

#             cam.release()
#             cv2.destroyAllWindows()

#         auto()
#     except Exception as e:
#         print(e)


def go_307():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\room_307.py")


def go_308():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\room_308.py")


def go_309():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\room_309.py")


def go_401():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\room_401.py")


def go_406():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\room_406.py")


def go_502():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\room_502.py")


def go_503():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\room_503.py")


def go_507():
    a.withdraw()
    os.system("D:\ASP_Project\ASP\\room_507.py")


def back():
    l = messagebox.askquestion("BACK", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າຫຼັກ ຫຼື ບໍ່?")
    if l == "yes":
        a.withdraw()
        os.system("D:\ASP_Project\ASP\\window1.py")


# button
canvas = Canvas(
    a, bg="#FFFFFF", height=1080, width=1920, bd=0, highlightthickness=0, relief="ridge"
)

canvas.place(x=0, y=0)

background_img = PhotoImage(file="ASP/Image/bg_attan.png")
background = canvas.create_image(950.0, 540.0, image=background_img)

bt1 = PhotoImage(file="ASP/Image/bt307.png")
button_1 = Button(
    image=bt1,
    borderwidth=0,
    highlightthickness=0,
    command=go_307,
    relief="flat",
)
button_1.place(x=30, y=100)

bt2 = PhotoImage(file="ASP/Image/bt308.png")
button_2 = Button(
    image=bt2,
    borderwidth=0,
    highlightthickness=0,
    command=go_308,
    relief="flat",
)
button_2.place(x=410, y=100)

bt3 = PhotoImage(file="ASP/Image/bt309.png")
button_3 = Button(
    image=bt3,
    borderwidth=0,
    highlightthickness=0,
    command=go_309,
    relief="flat",
)
button_3.place(x=810, y=100)

bt4 = PhotoImage(file="ASP/Image/bt401.png")
button_4 = Button(
    image=bt4,
    borderwidth=0,
    highlightthickness=0,
    command=go_401,
    relief="flat",
)
button_4.place(x=1210, y=100)

bt5 = PhotoImage(file="ASP/Image/bt406.png")
button_5 = Button(
    image=bt5,
    borderwidth=0,
    highlightthickness=0,
    command=go_406,
    relief="flat",
)
button_5.place(x=30, y=450)

bt6 = PhotoImage(file="ASP/Image/bt502.png")
button_6 = Button(
    image=bt6,
    borderwidth=0,
    highlightthickness=0,
    command=go_502,
    relief="flat",
)
button_6.place(x=410, y=450)

bt7 = PhotoImage(file="ASP/Image/bt503.png")
button_7 = Button(
    image=bt7,
    borderwidth=0,
    highlightthickness=0,
    command=go_503,
    relief="flat",
)
button_7.place(x=810, y=450)

bt8 = PhotoImage(file="ASP/Image/bt507.png")
button_8 = Button(
    image=bt8,
    borderwidth=0,
    highlightthickness=0,
    command=go_507,
    relief="flat",
)
button_8.place(x=1210, y=450)

bt_back = PhotoImage(file="ASP/Image/back.png")
button_back = Button(
    image=bt_back, borderwidth=0, highlightthickness=0, command=back, relief="flat"
)
button_back.place(x=200, y=700, width=246, height=90)

a.mainloop()
