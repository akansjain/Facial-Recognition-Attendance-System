from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from student import Student
from train import Train
from face_recognition import Face_Recognition
import os
from attendance import Attendance
import re
import tkinter
import pyttsx3 
from main import Face_Recognition_System

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice


def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()


def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")

        self.bg = ImageTk.PhotoImage(file = r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\main background.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1550,height=800)

        frame = Frame(self.root, bg="dark blue")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\jims logo.jpg")

        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), bg="Dark blue", fg="white")
        get_str.place(x=100, y=100)

        # labels
        username_lbl = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), bg="Dark blue", fg="white")
        username_lbl.place(x=65, y=152)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password_lbl = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="Dark blue", fg="white")
        password_lbl.place(x=65, y=225)

        self.txtpass = ttk.Entry(frame, show="*",font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        img2 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\jims logo.jpg")

        img2 = img2.resize((20, 20), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\student2.png")

        img3 = img3.resize((20, 20), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=397, width=25, height=25)

        # loginBuutton
        loginbtn = Button(frame, command=self.login, text="Login", font=(
            "times new roman", 15, "bold"), bd=3, relief=RIDGE, bg="red", fg="white")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # registrationButton
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=(
            "times new roman", 10, "bold"), borderwidth=0, bg="Dark blue", fg="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # forgetpasswordButton
        forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window,font=("times new roman", 10, "bold"), borderwidth=0, bg="Dark blue", fg="white", activebackground="black")
        forgetbtn.place(x=10, y=375, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all field required")
        elif self.txtuser.get() == "khom37" or "Khom" and self.txtpass.get() == "khom@123":
            speak_va("Welcome to Face Recognition World")
            messagebox.showinfo("success", "welcome to Face Recognition World")
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition_System(self.new_window)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="mrinal@", database="student")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()

                     ))
            row=my_cursor.fetchone()
            if row==None:
                speak_va("Invalid username and password!")
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Acess only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            # self.root.destroy()
        

            #************************************Reset password button ko lagi*******************
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
                messagebox.showerror("Error","select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
                messagebox.showerror("Error","select your answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
                messagebox.showerror("Error","please enter your new password",parent=self.root2) 
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="mrinal@", database="student")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s ")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)

            row=my_cursor.fetchone()
            if row==None:
                speak_va("Wrong Security Answer")
                messagebox.showerror("Error","Invalid security answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpassword.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                speak_va("Your password has been reset successfully.")
                messagebox.showinfo("Info","your password has been reset , please login new password",parent=self.root2)
            conn.commit()
            conn.close()
            self.root2.destroy()
               


                
                
 #   ************************forget password ko lagi****************
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="mrinal@", database="student")
            my_cursor = conn.cursor()
            query=("select *from register where email=%s")   ##### <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< see thissssssss
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2= Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman", 15, "bold"),bg="white", fg="red")
                l.place(x=0,y=0,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth place", "your dad name", "your mother name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpassword = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpassword.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15, "bold"), bg="orange",fg="green")
                btn.place(x=100,y=300)





#>>>>>>>>>>>>>>>>>>>>>>>>Register ko class lyakoo>>>

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration Form')
        self.root.geometry("1600x800+0+0")

        # ***************variabletr
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\main background.jpg")
        lbl_lbl = Label(self.root, image=self.bg)
        lbl_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # #left image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\jims logo.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=30, y=100, width=500, height=550)
        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        
        Register_frame=LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="REGISTER HERE",font=("times new roman",20,"bold"), fg="blue")
        Register_frame.place(x=5,y=5,width=670,height=400)

        fname=Label(Register_frame,text="First and Middle Name",font=("times new roman",15,"bold"),bg="white")
        fname.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        fname_entry=ttk.Entry(Register_frame,textvariable=self.var_fname,width=25,font=("times new roman",13,"bold"))
        fname_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        validate_fname=self.root.register(self.checkname)
        fname_entry.config(validate='key',validatecommand=(validate_fname,'%P'))

        lname=Label(Register_frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        lname_entry=ttk.Entry(Register_frame,textvariable=self.var_lname,width=25,font=("times new roman",13,"bold"))
        lname_entry.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        validate_lname=self.root.register(self.checklname)
        fname_entry.config(validate='key',validatecommand=(validate_lname,'%P'))


        contact=Label(Register_frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white")
        contact.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        contact_entry=ttk.Entry(Register_frame,textvariable=self.var_contact,width=25,font=("times new roman",13,"bold"))
        contact_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        validate_phone=self.root.register(self.checkphone)
        contact_entry.config(validate='key',validatecommand=(validate_phone,'%P'))

        email=Label(Register_frame,text="Email or Username",font=("times new roman",15,"bold"),bg="white")
        email.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(Register_frame,textvariable=self.var_email,width=25,font=("times new roman",13,"bold"))
        email_entry.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        email=Label(Register_frame,text="*Please enter valid email: ex123@gmail.com",font=("times new roman",8,"bold"),fg="red",bg="white")
        email.place(x=250, y=139)




        security_Q=Label(Register_frame,text="Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.grid(row=6,column=1,padx=5,pady=5,sticky=W)

        Security_combo=ttk.Combobox(Register_frame,textvariable=self.var_securityQ,font=("times new roman",13,"bold"),state="readonly",width=23)
        Security_combo["values"]=("Select Security Question","Your Dad's Name","Your Mom's name")
        Security_combo.current(0)
        Security_combo.grid(row=7,column=1,padx=5,pady=10,sticky=W)


        security_A=Label(Register_frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.grid(row=6,column=2,padx=10,pady=5,sticky=W)

        security_entry=ttk.Entry(Register_frame,textvariable=self.var_securityA,width=25,font=("times new roman",13,"bold"))
        security_entry.grid(row=7,column=2,padx=10,pady=5,sticky=W)


        pswd=Label(Register_frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.grid(row=8,column=1,padx=10,pady=5,sticky=W)

        pswd_entry=ttk.Entry(Register_frame,textvariable=self.var_pass,width=25,font=("times new roman",13,"bold"))
        pswd_entry.grid(row=9,column=1,padx=10,pady=5,sticky=W)


        pswd=Label(Register_frame,text="*Please enter strong password",font=("times new roman",10,"bold"),fg="red",bg="white")
        pswd.place(x=35, y=305)



    


        confirm_pswd=Label(Register_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.grid(row=8,column=2,padx=10,pady=5,sticky=W)

        confirm_pswd_entry=ttk.Entry(Register_frame,textvariable=self.var_confpass,width=25,font=("times new roman",13,"bold"))
        confirm_pswd_entry.grid(row=9,column=2,padx=10,pady=5,sticky=W)

        # ......check button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I am Agree with terms and conditions", font=(
            "times new roman", 12, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=370)

        # button
        img = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\register.png")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data,
                    image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\exit2.png")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,command=self.return_login,borderwidth=0, cursor="hand2")
        b1.place(x=330, y=420, width=200)


    def checkname(self,name):
        for char in name:
            if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
        return True

    def checklname(self,name):
        for char in name:
            if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
        return True

    def checkphone(self,phone):
        if len(phone) <=10:
          if phone.isdigit():
            return True
          if len(str(phone))==0:
            return True
          else:
            messagebox.showerror('Invalid','Invalid entry. Please enter phone (example:9846200045)', parent=self.root)
            return False
            
        else:
            messagebox.showwarning('Alert','invalid phone. Please enter phone (example:9846200045)',parent=self.root)
            return False



        
       
       



# ................fuction

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "password and confirm password must be same",parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please agree our terms and conditions",parent=self.root)

        elif not ("@" or ".com") in self.var_email.get():
            messagebox.showerror("Error",'Invalid email Enter valid email like mrinalnarang51@gmail.com ',parent=self.root)

        
        elif not ("@" or "!" or "$" or "-" or "." or "#" ) in self.var_pass.get():
            messagebox.showerror("Error",'Invalid password Please Enter Strong password like mrinal@123 ',parent=self.root)

    
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="mrinal@",database="student")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")   
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "user already exists ,try another email", parent=self.root )
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                messagebox.showinfo("Success", "Register Successfully", parent=self.root )
            conn.commit()
            conn.close()
            self.root.destroy()
    def return_login(self):
        self.root.destroy()




                                                                                                 
if __name__ == "__main__":
    main()
    root= Tk()
    app=login_window(root)
    root.mainloop()
