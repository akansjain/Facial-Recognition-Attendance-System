from tkinter import *
from tkinter import ttk as ttk 
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from developer import Developer
from help import Help 
from attendance import Attendance
import tkinter
from time import strftime
from datetime import datetime
from face_recognition import Face_Recognition

class Face_Recognition_System:
     def __init__(self,root):
         self.root = root
         self.root.geometry("1400x850+0+0")
         self.root.title("Face Recognition System")
        # side image
         img1 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\bgwhite.png")
         img1 = img1.resize((420,150), Image.ANTIALIAS)
         self.photoimg3 = ImageTk.PhotoImage(img1)
         b_lbl = Label(self.root, image=self.photoimg3)
         b_lbl.place(x=0, y=80, width=650, height=150)
        # second image
         img2 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\jims logo.jpg")
         img2 = img2.resize((420,150), Image.ANTIALIAS)
         self.photoimg2 = ImageTk.PhotoImage(img2)
         f_lbl = Label(self.root, image=self.photoimg2)
         f_lbl.place(x=450, y=0, width=420, height=150)
        # background image
         img4 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\main background.jpg")
         img4 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\main background.jpg")
         img4 = img4.resize((1350, 580), Image.ANTIALIAS)
         img4 = img4.resize((1550, 780), Image.ANTIALIAS)
         self.photoimg4 = ImageTk.PhotoImage(img4)

         bg_img = Label(self.root, image=self.photoimg4)
         bg_img.place(x=0, y=120, width=1350, height=580)
         bg_img.place(x=0, y=150, width=1550, height=780)

         title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                           font=("Times New Roman", 35, "bold"), bg="#57d7ac", fg="black")
         title_lbl.place(x=0, y=00, width=1400, height=45)  # using .place u can place things at any part of the window
         #========time=========#

         def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

         lbl=Label(b_lbl, font=('times new roman',14, 'bold'), foreground= 'blue')
         lbl.place(x=10,y=30,width=110,height=50)
         time()     
         
        #  Grid.rowconfigure(root,0,weight=1)
        #  Grid.columnconfigure(root,0,weight=1)

         #========student-details===============#
         img5 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\student2.png")
         img5 = img5.resize((195, 195), Image.ANTIALIAS)
         self.photoimg5 = ImageTk.PhotoImage(img5)
         btn1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
         btn1.place(x=100, y=80, width=195, height=195)
        #  btn1.grid(row=0,column=0,sticky="nsew")


         btn1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
         btn1_1.place(x=100, y=245, width=195, height=40)
        #  btn1_1.grid(row=0,column=0,sticky="nsew")

       
         img6 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\face detector.jpg")
         img6 = img6.resize((195, 195), Image.ANTIALIAS)
         self.photoimg6 = ImageTk.PhotoImage(img6)

         btn2 = Button(bg_img, image=self.photoimg6,command=self.face_details, cursor="hand2")
         btn2.place(x=400, y=80, width=195, height=195)

         btn2_2 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
         btn2_2.place(x=400, y=245, width=195, height=40)

         # attendance button
         img7 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\attendence.png")
         img7 = img7.resize((195, 195), Image.ANTIALIAS)
         self.photoimg7 = ImageTk.PhotoImage(img7)

         btn3 = Button(bg_img, image=self.photoimg7,command=self.Attendance, cursor="hand2")
         btn3.place(x=700, y=80, width=195, height=195)

         btn3_3 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
         btn3_3.place(x=700, y=245, width=195, height=40)

         # Help Desk button
         img8 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\helpdesk.jpg")
         img8 = img8.resize((195, 195), Image.ANTIALIAS)
         self.photoimg8 = ImageTk.PhotoImage(img8)

         btn4 = Button(bg_img, image=self.photoimg8,command=self.help_data, cursor="hand2")
         btn4.place(x=1000, y=80, width=195, height=195)

         btn4_4 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
         btn4_4.place(x=1000, y=245, width=195, height=40)

         # train data button
         img9 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\training.jpg")
         img9 = img9.resize((350,360), Image.ANTIALIAS)
         self.photoimg9 = ImageTk.PhotoImage(img9)

         btn5 = Button(bg_img, image=self.photoimg9,command=self.Train_details, cursor="hand2")
         btn5.place(x=100, y=350, width=195, height=195)

         btn5_5 = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
         btn5_5.place(x=100, y=525, width=195, height=40)

#         # Photos button
         img10 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\photos.png")
         img10 = img10.resize((210,195), Image.ANTIALIAS)
         self.photoimg10 = ImageTk.PhotoImage(img10)

         btn6 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.open_img)
         btn6.place(x=400, y=350, width=195, height=195)

         btn6_6 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
         btn6_6.place(x=400, y=525, width=195, height=40)

         # Developer button
         img11 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\developer.png")
         img11 = img11.resize((265,265), Image.ANTIALIAS)
         self.photoimg11 = ImageTk.PhotoImage(img11)
         btn7 = Button(bg_img, image=self.photoimg11,command=self.developer_data, cursor="hand2")
         btn7.place(x=700, y=350, width=195, height=195)

         btn7_7 = Button(bg_img, text="Developer", cursor="hand2",font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
         btn7_7.place(x=700, y=525, width=195, height=40)

         # Exit button
         img12 = Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\exit.png")
         img12 = img12.resize((195,195), Image.ANTIALIAS)
         self.photoimg12 = ImageTk.PhotoImage(img12)

         btn8 = Button(bg_img, image=self.photoimg12,command=self.iExit, cursor="hand2")
         btn8.place(x=1000, y=350, width=195, height=195)

         btn8_8 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
         btn8_8.place(x=1000, y=525, width=195, height=40)


     def open_img(self):
         os.startfile("data")    
     def student_details(self):
         self.new_window = Toplevel(self.root)
         self.app = Student(self.new_window)
     def Train_details(self):
         self.new_window = Toplevel(self.root)
         self.app = Train(self.new_window)    
     def developer_data(self):
         self.new_window=Toplevel(self.root) 
         self.app=Developer(self.new_window)
     def face_details(self):
         self.new_window=Toplevel(self.root) 
         self.app=Face_Recognition(self.new_window)    

     def help_data(self):
         self.new_window=Toplevel(self.root) 
         self.app=Help(self.new_window)
    
     def iExit(self):

         self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project",parent=self.root)

         if  self.iExit >0:
             self.root.destroy()

         else:
             return     
     def Attendance(self):
             self.new_window=Toplevel(self.root) 
             self.app=Attendance(self.new_window)
        
         
# # defining object
if __name__ == "__main__":
     root = Tk()
     obj = Face_Recognition_System(root)
     root.mainloop()
