from tkinter import *
import cv2
import pymysql
from time import sleep
from pyfirmata import Arduino, SERVO

# port = "COM7"
# pin = 9
# # led = 13
# board = Arduino(port)

# board.digital[pin].mode = SERVO

faceDetect = cv2.CascadeClassifier("ASP/Detect/haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(1)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("ASP/Data/trainingImage.yml")
# path='DataSet'
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2
fontColor = (255, 0, 0)


# def servo(pin, angle):
#     board.digital[pin].write(angle)
#     sleep(0.015)


# def led(led, state):
#     board.digital[led].write(state)
#     sleep(1)


def getProfile(Id):
    connection = pymysql.connect(
        host="localhost", user="root", password="", database="asp_base"
    )
    conn = connection.cursor()
    sql = "SELECT * FROM tb_face where f_Id='" + str(Id) + "';"
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
        if conf < 50:
            print(conf)
            global profile
            profile = getProfile(Id)
            if profile != None:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(
                    img,
                    str(profile[0]),
                    (x, y + h + 30),
                    fontface,
                    fontScale,
                    fontColor,
                )
                cv2.putText(
                    img,
                    str(profile[1]),
                    (x, y + h + 80),
                    fontface,
                    fontScale,
                    fontColor,
                )
        else:
            print("Unknown " + str(conf))
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Unknown", (x, y + h + 30), fontface, fontScale, fontColor)
    cv2.imshow("Face", img)
    key = cv2.waitKey(1) & 0xFF == ord("q")
    if key:
        break
cam.release()
cv2.destroyAllWindows()

# if str(profile[1]) == "souliya":
#     index = 1
#     x = 1
#     print(profile)
#     while True:
#         if x == index:
#             for i in range(0):
#                 servo(pin, i)
#             for i in range(0, 90, 1):
#                 servo(pin, i)
#             sleep(5)
#             for i in range(90, 0, -1):
#                 servo(pin, i)
#         break
# else:
#     print("Unknown")
#     while True:
#         led(13, 1)
#         sleep(1)
#         led(13, 0)
#         sleep(1)
