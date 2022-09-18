"""
Important Notes
-> First Install ( pip install pillow )
-> install open cv 2 (pip install opencv-python)
-> install (pip install opencv-contrib-python)
-> install numpy ( pip install numpy)
-> Database create (  host="localhost",user="root",passwd="123456",database="criminaldetection)
-> Database table Name ( detectiontabel)
"""


import os
from tkinter import *
from tkinter import ttk

import cv2
import numpy as np
import PIL
from PIL import Image

from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

from face_identifcation import Face_Recognition
from dataset import dataset
from changepassword import Change_Password




class main:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x680+0+0')

        self.root.title('CRIMINAL RECOGNITION SYSTEM ')
        self.root.wm_iconbitmap("face.ico")

        #Title______CRIMINAL MANAGEMENT SYSTEM______
        lbl_title=Label(self.root,text='CRIMINAL FACE RECOGNITION SYSTEM ',font=('times new romain',40,'bold') ,bg='black', fg='white')
        lbl_title.place(x=0,y=0,width=1530,height=70)

        #logo
        img_logo=Image.open("images\logo2.png")
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=90,y=5,width=60,height=60)


        #---------------------------------------------------------------------

        # main_frame

        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='LightBlue')
        Main_frame.place(x=1, y=70, width=1350, height=630)

        #------------------------------------------------=============================================
        #data set (CFR) image and btn
        #take image and resize the image
        student_btn=Image.open(r"images\dev.jpg")
        student_btn=student_btn.resize((190,200),Image.ANTIALIAS)
        self.photo_btn1=ImageTk.PhotoImage(student_btn)

        #the image we take make btn
        btn_simple_data_img=Button(Main_frame,image=self.photo_btn1,cursor="hand2",command=self.criminal_details)
        # btn_simple_data_img.grid(row=0, column=0, padx=50, pady=30)
        btn_simple_data_img.place(x=400,y=170)

        #data set (CFR)(text btn)
        btn_simple= Button(Main_frame, text="CFR", cursor="hand2", font=('Arial', 13, 'bold'), bg='black', fg='white',activeforeground='white',activebackground='green',borderwidth=0,command=self.criminal_details)
        btn_simple.place(x=402,y=340,width=190,height=35)

        #===================================================================================================


        #==================================================================================================

        # criminal_face_recognition photo button

        criminal_recognition_btn = Image.open(r"images\f_det.jpg")
        criminal_recognition_btn = criminal_recognition_btn.resize((190, 200), Image.ANTIALIAS)
        self.photo_btn4 = ImageTk.PhotoImage(criminal_recognition_btn)

        btn_criminal_recognition_photo = Button(Main_frame, image=self.photo_btn4, cursor="hand2", command=self.face_data)
        # btn_criminal_recognition_photo.grid(row=1, column=0, padx=50, pady=30)
        btn_criminal_recognition_photo.place(x=700,y=170)

        # criminal recognition (Text)
        btn_criminal_recognition = Button(Main_frame, text="Criminal Recognition", cursor="hand2", font=('Arial', 13, 'bold'), bg='black', fg='white',
                                activeforeground='white',
                                activebackground='green', borderwidth=0, command=self.face_data)
        btn_criminal_recognition.place(x=703, y=340, width=190, height=35)

        #================================================================================================
        #change password

        # change Password photo button

        change_password = Image.open(r"images\password change.jpg")
        change_password = change_password.resize((190, 200), Image.ANTIALIAS)
        self.photo_btn5 = ImageTk.PhotoImage(change_password)

        change_password_photo = Button(Main_frame, image=self.photo_btn5, cursor="hand2",command=self.change_pass)
        # btn_criminal_recognition_photo.grid(row=1, column=0, padx=50, pady=30)
        change_password_photo.place(x=950,y=170)



        change_password_btn = Button(Main_frame, text="Change Password", cursor="hand2", font=('Arial', 13, 'bold'), bg='black', fg='white',
                                          activeforeground='white',
                                          activebackground='green', borderwidth=0,command=self.change_pass)
        change_password_btn.place(x=950, y=340, width=195, height=35)


     # #+++++++++++++++++++++=functions+++++++++++

    #criminal button connect to new new window
    def criminal_details(self):
        self.new_window=Toplevel(self.root)
        self.app=dataset(self.new_window)

    #--------------------------------------------------------

    #photo opens
    def open_img(self):
        pass
        #os.startfile(r"photo")

    #---------------------------------------------------------


    #-----------------------------------------------

    #Face_recognition to new window

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

     #-----------------change password function----------------


    def change_pass(self):
        self.new_window = Toplevel(self.root)
        self.app = Change_Password(self.new_window)


#Main
if __name__=="__main__":
    root=Tk()
    obj=main(root)
    root.mainloop()

