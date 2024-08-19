from tkinter import *
import os
from tkinter import filedialog
from textblob import TextBlob # pip install textblob . This library in python helps to check the correctness of the text and also analyze the sentiments
import emoji  #pip install emoji

# Link for python emoji (https://carpedm20.github.io/emoji/). Here you can get various emoji's name.

root = Tk()
root.config(bg="#24e7ff")
root.geometry("496x525")
root.title("Text corrector and emotion detector")

def txt_detector():
    txt_1 = ent.get()
    checking = TextBlob(txt_1)
    analyzing = checking.correct()
    print(analyzing)
    ent2.insert(0,analyzing)
    
def emotion_detector():
    ent2.delete(0,END)
    txt_1 = ent.get()
    checking = TextBlob(txt_1)
    emotions = checking.sentiment.polarity
    if emotions < 0:
        ent2.insert(0,"The text has negative emotion")
        Label(root,text=f"{emoji.emojize(":disappointed_face:")}",font="arial 32",bg="#24e7ff").place(x = 447, y = 265) #Here using sad emoji for the sad sentiments.
    
    elif emotions > 0:
        ent2.insert(0,"The text has positive emotions")
        Label(root,text=f"{emoji.emojize(":grinning_face_with_big_eyes:")}",font="arial 32",bg="#24e7ff").place(x = 447, y = 265) #Here using grinning or smile emoji for happy sentiments.
    
    else:
        ent2.insert(0,"The text has neutral emotion")
    
Label(root,text="Enter text to detect correctness and its emotion",font="arial 15 bold",fg="#f23c12",bg="#24e7ff").pack(pady = 12,padx = 21)

# Entry 1 to get user's input
ent = Entry(root,font="Robote 18 bold",bd=3,relief=RAISED)
ent.pack(pady = 18)

f1 = Frame(root,height=60,width=420,bg="#24e7ff",bd=6,relief=GROOVE)
f1.pack()

# First button to check correctness of the text
Button(f1,text="Detect Correctness",font="Robote 15 bold",command=txt_detector).place(x = 1,y = 3)

# Second button to detect the emotion level of the text
Button(f1,text="Detect Emotion",font="Robote 15 bold",width=15,command=emotion_detector).place(x = 214, y = 3)

Label(root,text="Corrected text / Emotion level",font="arial 15 bold",fg="#f23c12",bg="#24e7ff").pack(pady = 30)
# Entry 2 to provide corrected text and text's emotion
ent2 = Entry(root,font="Robote 18 bold",bd=3,relief=RAISED,width=30)
ent2.pack()

root.mainloop()