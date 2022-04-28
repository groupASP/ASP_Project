from asyncio import exceptions
from tkinter import *
import tkinter
from tkinter import ttk
import pymysql
from tkinter import font as tkfont
from tkinter import messagebox
import os

a=tkinter.Tk()
# a.geometry("1500x900")
a.attributes("-fullscreen", True)

# def scan_face():
#     import cv2
#     import pymysql

#     faceDetect = cv2.CascadeClassifier('ASP/Detect/haarcascade_frontalface_default.xml')
#     cam = cv2.VideoCapture(0)
#     rec = cv2.face.LBPHFaceRecognizer_create()
#     rec.read("ASP/Data/trainingImage.yml")
#     fontface=cv2.FONT_HERSHEY_SIMPLEX
#     fontScale = 2
#     fontColor = (255,0,0)

#     def getProfile(Id):
#         connection = pymysql.connect(host="localhost", user="root", password="", database="asp_base")
#         conn = connection.cursor()
#         sql = "SELECT * FROM tb_face where f_Id='"+str(Id)+"';"
#         conn.execute(sql)
#         profile=None
#         for row in conn:
#             profile=row
#         conn.close()
#         return profile

#     while(True):
#         ret, img = cam.read()
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = faceDetect.detectMultiScale(gray, 1.3, 5)
#         for(x, y, w, h) in faces:
#                 Id, conf = rec.predict(gray[y:y+h, x:x+w])
#                 if(conf<38):
#                     print(conf)
#                     global profile
#                     profile = getProfile(Id)
#                     if(profile!=None):
#                         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#                         cv2.putText(img, str(profile[0]), (x, y+h+30), fontface, fontScale, fontColor)
#                         cv2.putText(img, str(profile[1]), (x, y+h+80), fontface, fontScale, fontColor)
#                 else:
#                     print("Unknown "+str(conf))
#                     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#                     cv2.putText(img, "Unknown", (x, y+h+30), fontface, fontScale, fontColor)
#         cv2.imshow("Face", img)
#         key=cv2.waitKey(30) & 0xff == ord('q')
#         if key:
#             break
#     cam.release()
#     cv2.destroyAllWindows()

def auto_att():
    import cv2
    import pymysql

    faceDetect = cv2.CascadeClassifier('ASP/Detect/haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read("ASP\\Data\\trainingData.yml")
    fontface=cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    fontColor = (255,0,0)
    try:
        def auto():
            def getProfile(Id):
                connection = pymysql.connect(host="localhost", user="root", password="", database="asp_base")
                conn = connection.cursor()
                sql = "SELECT * FROM tb_face where f_Id='"+str(Id)+"';"
                conn.execute(sql)
                profile=None
                for row in conn:
                    profile=row
                conn.close()
                return profile
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = faceDetect.detectMultiScale(gray, 1.3, 5)
                for(x, y, w, h) in faces:
                    Id, conf = rec.predict(gray[y:y+h, x:x+w])
                    if(conf<70):
                        print(conf)
                        global profile
                        profile = getProfile(Id)
                        if(profile!=None):
                            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                            cv2.putText(img, str(profile[0]), (x, y+h+30), fontface, fontScale, fontColor)
                            cv2.putText(img, str(profile[1]), (x, y+h+80), fontface, fontScale, fontColor)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        cv2.putText(img, "Unknown", (x, y+h+30), fontface, fontScale, fontColor)
                cv2.imshow("Face", img)
                key = cv2.waitKey(1) & 0xFF == ord('q')
                if key:
                    break
                elif conf < 38:
                    break
            try:
                connection = pymysql.connect(host="localhost", user="root", password="", database="asp_base")
                conn = connection.cursor()
            except Exception as e:
                print(e)

            insert_data =  "INSERT INTO tb_attandance VALUES (0, %s, %s, %s)"
            VALUES = (str(profile[0]),str(profile[1]), str(profile[2]), str(profile[3]))
            try:
                conn.execute(insert_data, VALUES)
                connection.commit()
            except Exception as ex:
                print(ex)
            cam.release()
            cv2.destroyAllWindows()
    except Exception as e:
        print(e)

def back():
    l = messagebox.askquestion("BACK","ທ່ານຕ້ອງການຈະກັບໄປໜ້າຫຼັກ ຫຼື ບໍ່?")
    if(l == 'yes'):
        a.withdraw()
        os.system("D:\ASP_Project\ASP\\window1.py")

#button
canvas = Canvas(
    a,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "ASP/Image/bg_attan.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)

bt1 = PhotoImage(file="ASP/Image/bt_start.png")
button_1 = Button(
    image=bt1,
    borderwidth=0,
    highlightthickness=0,
    command=auto_att,
    relief="flat")
button_1.place(
    x=500.,
    y=180)

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
    y=650,
    width=246,
    height=90
)

a.mainloop()