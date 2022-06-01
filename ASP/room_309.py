from tkinter import *
import tkinter
from tkinter import ttk
import pymysql
from tkinter import messagebox
import os
from datetime import *
import pytz
from tkinter import font as tkFont


a = tkinter.Tk()
a.geometry("1500x900")
a.attributes("-fullscreen", True)


def check_in():
    import cv2
    import pymysql

    faceDetect = cv2.CascadeClassifier("ASP/Detect/haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read("ASP\\Data\\trainingImage.yml")
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    fontColor = (255, 0, 0)
    try:

        def auto():
            def getProfile(Id):
                connection = pymysql.connect(
                    host="localhost", user="root", password="", database="asp_base"
                )
                conn = connection.cursor()
                sql = (
                    "select st.st_Id, st.st_Name, st.st_Surname, d.d_Name, s.s_Name, \
                    r.r_Name, cl.cl_Name, sc.sc_Period, sc.sc_Year, f.Name, f.Surname, sc.start_Class, \
                    sc.end_Class \
                    from tb_face f inner join tb_student st on f.st_Id = st.st_Id\
                    inner join tb_class cl on st.cl_Id = cl.cl_Id\
                    inner join tb_schedule sc on sc.cl_Id=cl.cl_Id\
                    inner join tb_day d on d.d_Id=sc.d_Id\
                    inner join tb_subject s on s.s_Id=sc.s_Id\
                    inner join tb_room r on r.r_Id=sc.r_Id\
                    where f_Id = '"
                    + str(Id)
                    + "';"
                )
                conn.execute(sql)
                profile = None
                for row in conn:
                    profile = row
                conn.close()
                return profile

            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = faceDetect.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    Id, conf = rec.predict(gray[y : y + h, x : x + w])
                    if conf < 38:
                        print(conf)
                        global profile
                        profile = getProfile(Id)
                        if profile != None:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            cv2.putText(
                                img,
                                str(profile[9]),
                                (x, y + h + 30),
                                fontface,
                                fontScale,
                                fontColor,
                            )
                            cv2.putText(
                                img,
                                str(profile[10]),
                                (x, y + h + 80),
                                fontface,
                                fontScale,
                                fontColor,
                            )
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(
                            img,
                            "Unknown",
                            (x, y + h + 30),
                            fontface,
                            fontScale,
                            fontColor,
                        )
                cv2.imshow("Face", img)
                key = cv2.waitKey(1) & 0xFF == ord("q")
                if key or conf <= 38:
                    break
            try:
                connection = pymysql.connect(
                    host="localhost", user="root", password="", database="asp_base"
                )
                conn = connection.cursor()
                if str(profile[5]) == "309" and str(profile[6]) == "CS6B":
                    local_time = pytz.timezone("Asia/Bangkok")
                    a = 0
                    b = 1
                    date_Today = datetime.now(tz=local_time).strftime("%Y-%m-%d")
                    time_now = datetime.now(tz=local_time).strftime("%H:%M:%S")
                    start_Class = str(
                        time(hour=8, minute=45, second=0, tzinfo=local_time)
                    )
                    st_Id = str(profile[0])
                    r_Name = str(profile[5])
                    cl_Name = str(profile[6])
                    if time_now < start_Class:
                        update_data = (
                            " UPDATE tb_attandance set time_In = '"
                            + time_now
                            + "', first_Absence = '"
                            + str(a)
                            + "' where st_Id = '"
                            + st_Id
                            + "' and r_Name = '"
                            + r_Name
                            + "' and cl_Name = '"
                            + cl_Name
                            + "' and date = '"
                            + date_Today
                            + "';"
                        )
                        conn.execute(update_data)
                        connection.commit()
                    else:
                        update_data = (
                            " UPDATE tb_attandance set time_In = '"
                            + time_now
                            + "', first_Absence = '"
                            + str(b)
                            + "' where st_Id = '"
                            + st_Id
                            + "' and r_Name = '"
                            + r_Name
                            + "' and cl_Name = '"
                            + cl_Name
                            + "' and date = '"
                            + date_Today
                            + "';"
                        )
                        conn.execute(update_data)
                        connection.commit()
                else:
                    print("Hello")
            except Exception as e:
                print(e.args)

            cam.release()
            cv2.destroyAllWindows()

        auto()
    except Exception as e:
        print(e)


def Exit_Room():
    import cv2
    import pymysql

    faceDetect = cv2.CascadeClassifier("ASP/Detect/haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(0)
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read("ASP\\Data\\trainingImage.yml")
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    fontColor = (255, 0, 0)
    try:

        def auto():
            def getProfile(Id):
                connection = pymysql.connect(
                    host="localhost", user="root", password="", database="asp_base"
                )
                conn = connection.cursor()
                sql = (
                    "select st.st_Id, st.st_Name, st.st_Surname, d.d_Name, s.s_Name, \
                    r.r_Name, cl.cl_Name, sc.sc_Period, sc.sc_Year, f.Name, f.Surname, sc.start_Class, \
                    sc.end_Class\
                    from tb_face f inner join tb_student st on f.st_Id = st.st_Id\
                    inner join tb_class cl on st.cl_Id = cl.cl_Id\
                    inner join tb_schedule sc on sc.cl_Id=cl.cl_Id\
                    inner join tb_day d on d.d_Id=sc.d_Id\
                    inner join tb_subject s on s.s_Id=sc.s_Id\
                    inner join tb_room r on r.r_Id=sc.r_Id\
                    where f_Id = '"
                    + str(Id)
                    + "';"
                )
                conn.execute(sql)
                profile = None
                for row in conn:
                    profile = row
                conn.close()
                return profile

            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = faceDetect.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    Id, conf = rec.predict(gray[y : y + h, x : x + w])
                    if conf < 38:
                        print(conf)
                        global profile
                        profile = getProfile(Id)
                        if profile != None:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            cv2.putText(
                                img,
                                str(profile[9]),
                                (x, y + h + 30),
                                fontface,
                                fontScale,
                                fontColor,
                            )
                            cv2.putText(
                                img,
                                str(profile[10]),
                                (x, y + h + 80),
                                fontface,
                                fontScale,
                                fontColor,
                            )
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(
                            img,
                            "Unknown",
                            (x, y + h + 30),
                            fontface,
                            fontScale,
                            fontColor,
                        )
                cv2.imshow("Face", img)
                key = cv2.waitKey(1) & 0xFF == ord("q")
                if key or conf <= 38:
                    break
            try:
                connection = pymysql.connect(
                    host="localhost", user="root", password="", database="asp_base"
                )
                conn = connection.cursor()
                local_time = pytz.timezone("Asia/Bangkok")
                time_now = datetime.now(tz=local_time).strftime("%H:%M:%S")
                date_Today = datetime.now().strftime("%Y-%m-%d")
                a = 0
                b = 1
                start_Class = str(time(hour=8, minute=45, second=0, tzinfo=local_time))
                end_Class = str(time(hour=12, minute=0, second=0, tzinfo=local_time))
                st_Id = str(profile[0])
                r_Name = str(profile[5])
                cl_Name = str(profile[6])
                if time_now <= start_Class and time_now >= end_Class:
                    update_data = (
                        " UPDATE tb_attandance set time_Out = '"
                        + time_now
                        + "', second_Absence = '"
                        + str(a)
                        + "' where st_Id = '"
                        + st_Id
                        + "' and r_Name = '"
                        + r_Name
                        + "' and cl_Name = '"
                        + cl_Name
                        + "' and date = '"
                        + date_Today
                        + "';"
                    )
                    conn.execute(update_data)
                    connection.commit()
                else:
                    update_data = (
                        " UPDATE tb_attandance set time_Out = '"
                        + time_now
                        + "', second_Absence = '"
                        + str(b)
                        + "' where st_Id = '"
                        + st_Id
                        + "' and r_Name = '"
                        + r_Name
                        + "' and cl_Name = '"
                        + cl_Name
                        + "' and date = '"
                        + date_Today
                        + "';"
                    )
                    conn.execute(update_data)
                    connection.commit()
            except Exception as e:
                print(e)

            cam.release()
            cv2.destroyAllWindows()

        auto()
    except Exception as e:
        print(e)


def back():
    l = messagebox.askquestion("BACK", "ທ່ານຕ້ອງການຈະກັບໄປໜ້າການມາຮຽນ ຫຼື ບໍ່?")
    if l == "yes":
        a.withdraw()
        os.system("D:\ASP_Project\ASP\\attandance.py")


# button
canvas = Canvas(
    a, bg="#FFFFFF", height=1080, width=1920, bd=0, highlightthickness=0, relief="ridge"
)

canvas.place(x=0, y=0)

background_img = PhotoImage(file="ASP/Image/bg_309.png")
background = canvas.create_image(950.0, 540.0, image=background_img)

bt1 = PhotoImage(file="ASP/Image/bt_checkIn.png")
button_1 = Button(
    image=bt1,
    borderwidth=0,
    highlightthickness=0,
    command=check_in,
    relief="flat",
)
button_1.place(x=250, y=380)

bt2 = PhotoImage(file="ASP/Image/bt_checkOut.png")
button_2 = Button(
    image=bt2,
    borderwidth=0,
    highlightthickness=0,
    command=Exit_Room,
    relief="flat",
)
button_2.place(x=950, y=380)

bt3 = PhotoImage(file="ASP/Image/bt_break.png")
button_3 = Button(
    image=bt3,
    borderwidth=0,
    highlightthickness=0,
    # command=auto_att,
    relief="flat",
)
button_3.place(x=950, y=700)

bt4 = PhotoImage(file="ASP/Image/back.png")
button_4 = Button(
    image=bt4,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat",
)
button_4.place(x=300, y=700)

bt5 = PhotoImage(file="ASP/Image/bt_start_class.png")
button_5 = Button(
    image=bt5,
    borderwidth=0,
    highlightthickness=0,
    # command=back,
    relief="flat",
)
button_5.place(x=900, y=150)

connection = pymysql.connect(
    host="localhost", user="root", password="", database="asp_base"
)
conn = connection.cursor()

cbFont = tkFont.Font(family="Saysettha OT", size=18)

conn.execute("select cl_Name from tb_class;")
results = conn.fetchall()
combo_cl_name = [result[0] for result in results]


class_lb = Label(a, text="ກະລຸນາເລືອກຊັ້ນຮຽນ : ", font=cbFont, bg="#ECF8DC")
class_lb.place(x=200, y=180)

cb_class = ttk.Combobox(a, width=25, values=combo_cl_name)
cb_class.place(x=500, y=180)
cb_class.config(font=(cbFont), state="readonly")
cb_class.configure(font=("Saysettha OT", 16))
cb_class.option_add("*font", cbFont)
cb_class.current(0)

a.mainloop()
