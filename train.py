from ntpath import join
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class Train:  
    def __init__(self, root):
         self.root=root
         self.root.geometry("1530x798+8+8")
         self.root.title("Face Recogniton System")

         title_lbl=Label(self.root, text="TRAIN DATA SET", font=("times new roman",35,"bold"),bg="blue",fg="white")
         title_lbl.place(x=0, y=0,width=1530, height=45)


         img_top=Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\main background.jpg")
         img_top=img_top.resize((1530,798),Image.ANTIALIAS)
         self.photoimg_top=ImageTk.PhotoImage(img_top)

         f_lbl=Label(self.root,image=self.photoimg_top)
         f_lbl.place(x=0,y=55,width=1530 ,height=798)

        #button
         b1_1=Button(self.root, text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="blue",fg="white")
         b1_1.place(x=450, y=380,width=600,height=60)

         img_bottom=Image.open(r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\images\training.jpg")
         img_bottom=img_bottom.resize((350,360),Image.ANTIALIAS)
         self.photoimage_bottom=ImageTk.PhotoImage(img_bottom)

         f_lbl=Label(self.root,image=self.photoimage_bottom)
         f_lbl.place(x=620,y=85,width=250 ,height=250)

    def train_classifier(self):
        
        data_dir = (r"C:\Users\Akansha Jain\Desktop\Desktop\project\project\data")
        path=[os.path.join(data_dir,file) for  file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  # grAY SCALE image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train the classifier and save 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        speak_va("Training datasets completed successfully!")
        messagebox.showinfo("Result","Training datasets completed successfully!",parent=self.root)
        self.root.destroy()



    
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()