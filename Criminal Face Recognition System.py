from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import os
import mysql.connector

from face_identifcation import Face_Recognition
from dataset import dataset

class login_system:
    def __init__(self, root):
        self.root = root
        root.title("Criminal Face Recognition Login System")
        root.geometry('1360x710+1+0')
        # ***************************** Image ****************************************888
        # self.images = ImageTk.PhotoImage(file="C:/Users/AZMAT ULLAH KHAN/PycharmProjects/Azmat/image1.jpg")
        # self.lbl_image = Label(self.root, image=self.images).place(x=0, y=0)
        # ######################### Variable ###########################
        self.employee_id = StringVar()
        self.password = StringVar()

        self.user_name_entry=StringVar()
        self.password_entry=StringVar()
        self.new_password_entry = StringVar()

        #backgroung image of login window
        self.bg=ImageTk.PhotoImage(file=r"images\bg4.png")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ********************************** Login_Frame ********************************
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=500, y=98, width=350, height=460)

        title = Label(login_frame, text="Login System", font=("Elephent", 30, "bold"), bg="white").place(x=0, y=30,
                                                                                                         relwidth=1)
        # ******************************** Username And Entry ************************
        lbl_user = Label(login_frame, text="Email ", font=("times new roman", 14, "bold"), fg='Black').place(x=50,
                                                                                                                y=100)
        txt_username = Entry(login_frame, textvariable=self.user_name_entry, font=("times new roman", 14,"bold"),
                             bg="#ECECEC").place(
            x=50, y=140)

        # ******************************** Password And Entry ************************
        lbl_pass = Label(login_frame, text="Password", font=("times new roman", 14, "bold"),
                         fg="black").place(x=50, y=200)
        txt_pass = Entry(login_frame, font=("time new roman", 15), textvariable=self.password_entry, show="*",
                         bg="#ECECEC").place(x=50, y=240)

        # ******************* Button ***************************************
        btn_login = Button(login_frame, text="Log In", command=self.login, font=("Arial Rounded MT Bold", 15),
                           bg="#00B0F0",
                           activebackground="#00B0F0", fg="white", activeforeground="white", cursor="hand2").place(x=50,
                                                                                                                   y=300,
                                                                                                                   width=250,
                                                                                                                   height=35)

        # ***************************** All Function ***********************************

    def login(self):

        try:
            if self.user_name_entry.get() == "" or self.password_entry.get() == "":
                messagebox.showerror("Error", "All field required")
                #playsound(r"mp3\2.mp3")

            else:
                conn = mysql.connector.connect(host="localhost", user="root", passwd="123456",
                                               database="criminaldetection_2")
                mycursor = conn.cursor()
                mycursor.execute("select * from login where Email=%s and Password=%s",
                                  (self.user_name_entry.get(), self.password_entry.get()))
                user = mycursor.fetchone()
                if user == None:

                    messagebox.showerror("Error", "Invalid USERNAME/PASSWORD")




                else:
                    self.root.destroy()


                    os.system("python All_Menu.py")









        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")


if __name__ == '__main__':
    root = Tk()
    obj = login_system(root)
    root.mainloop()
