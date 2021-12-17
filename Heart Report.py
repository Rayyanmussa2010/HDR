# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 15:12:36 2021

@author: DELL
"""

from tkinter import*
from tkinter import filedialog
import os

root=Tk()
root.title("Heart Report")
root.geometry("600x600")
question1radio=StringVar(value="0")

question1=Label(root, text="Do you experience shortness of breath during routine activities?")
question1.pack()
question1r1=Radiobutton(root, text="Yes", variable=question1radio, value="Yes")
question1r1.pack()
question1r2=Radiobutton(root, text="No", variable=question1radio, value="No")
question1r2.pack()


question2radio=StringVar(value="0")

question2=Label(root, text="Do you have swelling in the Feet/ Ankle/ Legs (Shoes feel tight) / Abdomen?")
question2.pack()
question2r1=Radiobutton(root, text="Yes", variable=question2radio, value="Yes")
question2r1.pack()
question2r2=Radiobutton(root, text="No", variable=question2radio, value="No")
question2r2.pack()


question3radio=StringVar(value="0")

question3=Label(root, text="Do you feel any of these symptoms - confusion / disorientation / loss of memory?")
question3.pack()
question3r1=Radiobutton(root, text="Yes", variable=question3radio, value="Yes")
question3r1.pack()
question3r2=Radiobutton(root, text="No", variable=question3radio, value="No")
question3r2.pack()


question4radio=StringVar(value="0")

question4=Label(root, text="Do you experience shortness of breath during rest / lying down?")
question4.pack()
question4r1=Radiobutton(root, text="Yes", variable=question4radio, value="Yes")
question4r1.pack()
question4r2=Radiobutton(root, text="No", variable=question4radio, value="No")
question4r2.pack()


question5radio=StringVar(value="0")

question5=Label(root, text="Do you experience persistent wheezinng / coughing that produces white or pink blood tinged mucus?")
question5.pack()
question5r1=Radiobutton(root, text="Yes", variable=question5radio, value="Yes")
question5r1.pack()
question5r2=Radiobutton(root, text="No", variable=question5radio, value="No")
question5r2.pack()


def fever_score():
    score=0
    if question1radio.get()=="Yes":
        score=score+20
        print(score)
    if question2radio.get()=="Yes":
        score=score+20
        print(score)
    if question3radio.get()=="Yes":
        score=score+20
        print(score)
    if question4radio.get()=="Yes":
        score=score+20
        print(score)
    if question5radio.get()=="Yes":
        score=score+20
        print(score)
    
    if score<=20:
        messagebox.showinfo("report", "You don't need to visit a doctor")
    
    elif score>20 and score<=40:
        messagebox.showinfo("report", "You might perhaps visit a doctor")
    
    else:
        messagebox.showinfo("report", "I strongly advice you to visit a doctor")


button_report=Button(root, text="Generate Report", command=fever_score)
button_report.pack()









root.mainloop()