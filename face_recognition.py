from tkinter import*
from tkinter import ttk
from turtle import title, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from train import Train
from ntpath import join



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # 1st image
        # img_top=Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\face detector.jpg")
        # img_top=img_top.resize((650,700),Image.ANTIALIAS)
        # self.photoimg_top=ImageTk.PhotoImage(img_top)

        # f_lbl=Label(self.root,image=self.photoimg_top)
        # f_lbl.place(x=0,y=55,width=650,height=700)

        
        # 2nd image
        img_bottom=Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\facerecog.png")
        img_bottom=img_bottom.resize((1250,750),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=55,width=1500,height=700)

        # button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",30,"bold"),bg="dark green",fg="white") 
        b1_1.place(x=500,y=620,width=500,height=40) 
    #====================attendance====================      
    def mark_attendance(self,i,r,n,d):
        with open("C:/Users/Akansha Jain/Desktop/Desktop/project/project/project.csv","r+",newline="\n") as f:
            myDastaList=f.readlines()
            name_list=[]
            for line in myDastaList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    #============face recognition ===================

    def face_recog(self):
        def draw_boundary(img,Classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=Classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) 
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))  

                conn=mysql.connector.connect(host="localhost",username="root",password="mrinal@",database="student")
                my_cursor=conn.cursor()


                my_cursor.execute("select Name from student1 where id="+str(id))
                n=my_cursor.fetchone()
                n = str(n).join(n)
                #n="+".join(n)
               

                my_cursor.execute("select Roll from student1 where id="+str(id))
                r=my_cursor.fetchone()
                r = str(r).join(r)
                #r="+".join(r)

                my_cursor.execute("select Dep from student1 where id="+str(id))
                d=my_cursor.fetchone()
                d = str(d).join(d)
                #d="+".join(d)

                my_cursor.execute("select id from student1 where id="+str(id))
                i=my_cursor.fetchone()
                i = str(i).join(i)
                #i="+".join(i)

                cv2.putText(img,f"Accuracy:{confidence}%",(x, y-100), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)


                if confidence>77:
                    cv2.putText(img,f"id:{r}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
             
                coord=[x,y,w,y]

            return coord
    
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")  

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img= recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img) 
    
            if cv2.waitKey(1)==13:
                
                break
        video_cap.release()
        cv2.destroyAllWindows() 
            
    
if __name__ == "__main__":
        root=Tk()
        obj=Face_Recognition(root)
        root.mainloop()