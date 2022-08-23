from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")
        
        title_lbl=Label(self.root, text="DEVELOPER", font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0, y=0,width=1530, height=45)


        img_top=Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\main background.jpg")
        img_top=img_top.resize((1530,798),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1530 ,height=798)
        
        #frame1
        main_frame=Frame(f_lbl,bd=2,bg="white",)
        main_frame.place(x=450,y=100,width=700,height=290)

        img_top1=Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\akansha.png")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl2=Label(main_frame,image=self.photoimg_top1)
        f_lbl2.place(x=470,y=50,width=200,height=200)

        #developer1 info
        dev_label=Label(main_frame,text="Akansha Jain",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=80)
        dev_label=Label(main_frame,text="MCA Sec-A",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=140)
        dev_label=Label(main_frame,text="00614004421",font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=60,y=200)   

        
        

if __name__ ==  "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()