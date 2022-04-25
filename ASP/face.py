from tkinter import *
from tkinter import  messagebox
import  os
import pymysql
import numpy as np
import cv2


def trainImg():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    global detector
    detector = cv2.CascadeClassifier("D:\ASP_Project\ASP\Detect\haarcascade_frontalface_default.xml")
    try:
        global faces,Id
        faces, Id = getImagesAndLabels("ASP/Data")
    except Exception as e:
        l='please make "DataSet" folder & put Images'
        Notification.configure(text=l, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)

    recognizer.train(faces, np.array(Id))
    try:
        recognizer.save("ASP/Data/trainingData.yml")
    except Exception as e:
        q='Please make "Recognizer" folder'
        Notification.configure(text=q, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)

    res = "Model Trained" 
    Notification.configure(text=res, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
    Notification.place(x=250, y=400)



def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    Ids = []

    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')

        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(imageNp)
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            Ids.append(Id)
    return faceSamples, Ids

def insert():
    window.withdraw()
    os.system("D:\ASP_Project\ASP\InsertOrUpdateFace.py")

def back():
    l = messagebox.askquestion("BACK","ທ່ານຕ້ອງການຈະກັບໄປໜ້າຫຼັກ ຫຼື ບໍ່?")
    if(l == 'yes'):
        window.withdraw()
        os.system("D:\ASP_Project\ASP\window1.py")

window = Tk()
window.attributes('-fullscreen', True)
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "ASP/Image/bg_face.png")
background = canvas.create_image(
    950.0, 540.0,
    image=background_img)

bt1 = PhotoImage(file="ASP/Image/scan.png")
button_1 = Button(
    image=bt1,
    borderwidth=0,
    highlightthickness=0,
    command=insert,
    relief="flat")
button_1.place(
    x=280.,
    y=300,
    width=259,
    height=246)

bt2 = PhotoImage(file="ASP/Image/train.png")
button_2 = Button(
    image=bt2,
    borderwidth=0,
    highlightthickness=0,
    command=trainImg,
    relief="flat"
)
button_2.place(
    x=1000,
    y=300,
    width=259,
    height=246
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
    x=650,y=720,
    width=246,
    height=90
)

Notification = Label(window, text="All things are good", bg="Green", fg="white", width=15,
                height=3, font=('times', 17, 'bold'))


window.resizable(False, False)
window.mainloop()
