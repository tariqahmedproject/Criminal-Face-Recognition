from tkinter import *
from tkinter import ttk

import cv2
from PIL import Image

from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Change_Password:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x680+0+0')

        self.root.title('Change Password')
        self.var_username = StringVar()
        self.var_password=StringVar()
        self.var_newpassword=StringVar()


        back=Button(self.root,text='Back',font=('Arial', 12, 'bold'),cursor="hand2",command=self.backbtn)
        back.place(x=1,y=2)

        label= Label(self.root, text='Change Password ', font=('Arial', 15, 'bold'), bg='white', fg='red')
        label.place(x=500, y=150, width=200, height=40)

        username= Label(self.root, text='Email', font=('Arial', 15, 'bold'), bg='white', fg='black')
        username.place(x=430, y=200, width=140, height=40)

        usernameentry = ttk.Entry(self.root, width=22, font=('Arial', 11, 'bold'),textvariable=self.var_username)
        usernameentry.place(x=600, y=200, width=200, height=40)

        #-----------------------------------------

        password= Label(self.root, text='Old Password', font=('Arial', 15, 'bold'), bg='white', fg='black')
        password.place(x=430, y=250, width=140, height=40)

        passwordentry = ttk.Entry(self.root, width=22, font=('Arial', 11, 'bold'),textvariable=self.var_password)
        passwordentry.place(x=600, y=250, width=200, height=40)


        newpassword= Label(self.root, text='New Password', font=('Arial', 15, 'bold'), bg='white', fg='black')
        newpassword.place(x=430, y=300, width=140, height=40)

        newpasswordentry = ttk.Entry(self.root, width=22, font=('Arial', 11, 'bold'),textvariable=self.var_newpassword)
        newpasswordentry.place(x=600, y=300, width=200, height=40)

        # -----------
        #button

        btn_simple= Button(self.root, text="Change Password", cursor="hand2", font=('Arial', 13, 'bold'), bg='black', fg='white',activeforeground='white',activebackground='green',borderwidth=0,command=self.changepassword)
        btn_simple.place(x=500,y=370,width=190,height=35)

    def changepassword(self):
        username=self.var_username.get()
        oldpassword=self.var_password.get()
        newpassword=self.var_newpassword.get()
        print(oldpassword)

        # sql connection
        conn = mysql.connector.connect(host="localhost", user="root", passwd="123456",
                                       database="criminaldetection_2")
        my_cursor = conn.cursor()
        my_cursor.execute('select * from login')
        data = my_cursor.fetchone()
        print(data)

        name=data[0]
        pwd=data[1]
        print(name,pwd)

        if username !=''and oldpassword !='' and newpassword !='':
            if name==username and pwd==oldpassword:
                my_cursor.execute('update login set Password=%s where Email=%s and Password=%s ',(newpassword,username,oldpassword))
                conn.commit()
                messagebox.showinfo("Sucess","Password Changed",parent=self.root)
            else:
                messagebox.showerror("Error","Invlaid User name and password",parent=self.root)
        else:
            messagebox.showerror("Error","Fill All Field",parent=self.root)




        conn.commit()
        conn.close()






    def backbtn(self):
        self.root.destroy()






if __name__=="__main__":
    root=Tk()
    obj=Change_Password(root)
    root.mainloop()