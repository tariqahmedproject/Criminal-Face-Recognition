

import os
from tkinter import *
from tkinter import ttk

import cv2
import numpy as np
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from playsound import playsound

import cv2
from simple_facerec import SimpleFacerec

class Face_Recognition :
    def __init__(self,root):
        self.root=root
        self.root.geometry('550x370+300+170')
        self.root.maxsize(width=550, height=370)
        self.root.minsize(width=550, height=370)

        self.root.title('Face Recognition')
        self.var_criminal = StringVar()


        # #Title______Face Recognition ______
        # lbl_title=Label(self.root,text='Face Recognition',font=('times new romain',40,'bold') ,bg='black',fg='gold')
        # lbl_title.place(x=0,y=0,width=1530,height=70)

        #BACKGROUND IMAGE
        self.bg = ImageTk.PhotoImage(file=r"images\f_bg.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, width=550, height=370)

        # ----------------------------------------------------

        # face_Recognition button camera 1
        #label for camera 1
        cam1=Label(root,text='Camera 1',font=('Arial', 15, 'bold'), bg='white', fg='black')
        cam1.place(x=20,y=20)

        #PHOTO CAM 1
        criminal_recognition_btn = Image.open(r"images\f_det.jpg")
        criminal_recognition_btn = criminal_recognition_btn.resize((190, 200), Image.ANTIALIAS)
        self.photo_btn4 = ImageTk.PhotoImage(criminal_recognition_btn)

        btn_criminal_recognition_photo = Button(self.root, image=self.photo_btn4, cursor="hand2", activeforeground='white',activebackground='green',command=self.face_cam1)
        btn_criminal_recognition_photo.grid(row=0, column=0, padx=10, pady=60)

        #SAMPLE BUTTON CAM 1
        btn_criminal_recognition = Button(self.root, text="Criminal Recognition C1", cursor="hand2", font=('Arial', 13, 'bold'), bg='black', fg='white',
                                          activeforeground='white',
                                          activebackground='green', borderwidth=0, command=self.face_cam1)
        btn_criminal_recognition.place(x=10, y=228, width=190, height=35)

        #------------------------------- camera 2--------------------------------
        #label for camera 2
        cam1=Label(root,text='Camera 2(external)',font=('Arial', 15, 'bold'), bg='white', fg='black')
        cam1.place(x=250,y=20)

        cam2 = Image.open(r"images\f_det.jpg")
        btn_cam2 = cam2.resize((190, 200), Image.ANTIALIAS)
        self.btn_cam2 = ImageTk.PhotoImage(btn_cam2)

        cam2_btn = Button(self.root, image=self.btn_cam2, cursor="hand2", activeforeground='white',activebackground='green',command=self.face_cam2)
        cam2_btn.grid(row=0, column=1, padx=20, pady=60)

        # criminal photo open (tect btn)
        camera2_btn = Button(self.root, text="Criminal Recognition C2", cursor="hand2", font=('Arial', 13, 'bold'), bg='black', fg='white',
                                          activeforeground='white',
                                          activebackground='green', borderwidth=0, command=self.face_cam2)
        camera2_btn.place(x=240, y=228, width=190, height=35)


        pressenter=Label(self.root,text='Note :: Press (Enter) to exit camera ',font=('Arial', 12, 'bold'), bg='white', fg='red')
        pressenter.place(x=100,y=300)

        wait=Label(self.root,text='Note :: when click on face recognition then please wait for some time  ',font=('Arial', 12, 'bold'), bg='white', fg='red')
        wait.place(x=10,y=330)

        back=Button(self.root,text='Back',font=('Arial', 12, 'bold'),cursor="hand2",command=self.backbtn)
        back.place(x=490,y=20)
    def backbtn(self):
        self.root.destroy()


    def face_cam1(self):
        #playsound(r"mp3\5.mp3")


        # Encode faces from a folder
        sfr = SimpleFacerec()

        sfr.load_encoding_images("photo/")


        # Load Camera
        cap = cv2.VideoCapture(0) #change camera to extrnal write 2 otherwsie 0


        while True:
            ret, frame = cap.read()

            # Detect Faces
            face_locations, face_names = sfr.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                cv2.putText(frame, name,(40, y1 - 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
                #playsound(r'mp3/0.mp3')


            cv2.imshow("Press Enter To Exit", frame)

            key = cv2.waitKey(1)
            if key == 27 or key == 13:
                break

        cap.release()
        cv2.destroyAllWindows()
    #-------------------------------- cam 2----------------------

    def face_cam2(self):

        # Encode faces from a folder
        sfr = SimpleFacerec()

        sfr.load_encoding_images("photo/")


        # Load Camera
        cap = cv2.VideoCapture(2) #change camera to extrnal write 2 otherwsie 0


        while True:
            ret, frame = cap.read()

            # Detect Faces
            face_locations, face_names = sfr.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                cv2.putText(frame, name,(40, y1 - 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

            cv2.imshow("Press Enter To Exit", frame)

            key = cv2.waitKey(1)
            if key == 27 or key == 13:
                break

        cap.release()
        cv2.destroyAllWindows()


#Main
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()