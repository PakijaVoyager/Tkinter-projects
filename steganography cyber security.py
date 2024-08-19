from tkinter import *
from tkinter import filedialog
import os
from stegano import lsb
from PIL import Image,ImageTk

def open_img():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image",filetypes=(("PNG file","*.png"),("JPG file","*.jpg"),("All files","*.txt")))
    img1 = Image.open(filename)
    img1 = ImageTk.PhotoImage(img1)
    lbl.configure(image=img1,width=320,height=290)
    lbl.image = img1

def save_img():
    secret1.save("hidden.png")

def hide_data():
    global secret1
    msg = txt_1.get(1.0,END)
    secret1= lsb.hide(str(filename),msg)
    txt_1.delete(1.0,END)
    

def show_data():
    txt_1.delete(1.0,END)
    dt = lsb.reveal(filename)
    txt_1.insert(1.0,dt)
    

root = Tk()
root.title("Secret Image hide")
root.geometry("690x612")
root.resizable(False,False)
root.config(bg="#151e3b")
# icon
img = Image.open("stegano.jpeg")
img = ImageTk.PhotoImage(img)
root.iconphoto(False,img) 

# Logo
Label(root,image=img).place(x = 6, y = 3)
Label(root,text="Cyber Science",font="arial 21 bold underline",bg="#151e3b",fg="white").place(x = 360, y = 6)

# Frame1
f1 = Frame(root,height=300,width=330,bg="black",bd=3,relief=GROOVE)
f1.place(x = 1, y = 200)
lbl = Label(f1,width=320,height=290,bg="black")
lbl.place(x = 0, y = 0)

# Frame2
f2 = Frame(root,height=300,width=330,bg="white",bd=3,relief=GROOVE)
f2.place(x = 330, y = 200)
# Text widget
txt_1 = Text(f2,font="arial 15 bold",bg="white",fg="black")
txt_1.place(width=310,height=300,x = 0, y = 0)
# scrollbar widget
scbar = Scrollbar(f2)
scbar.place(x=310, y = 0,height=300)

txt_1.configure(yscrollcommand=scbar.set)
scbar.configure(command=txt_1.yview)

# Frame3
f3 = Frame(root,height=90,width=390,border=3,relief=GROOVE,bg="#151e3b")
f3.place(x = 0, y = 510)
Label(f3,text="Picture, file, video",font="arial 12",fg="yellow",bg="#151e3b").place(x = 0 , y = 3)
Button(f3,text="Open Image",font="arial 18 bold",command=open_img).place(x = 3, y = 30)
Button(f3,text="Save Image",font="arial 18 bold",command=save_img).place(x = 175, y = 30)

# Frame4
f4 = Frame(root,height=90,width=330,border=3,relief=GROOVE,bg="#151e3b")
Label(f4,text="Picture, file, video",font="arial 12",fg="yellow",bg="#151e3b").place(x = 0 , y = 3)
Button(f4,text="Hide Data",font="arial 18 bold",command=hide_data).place(x = 9, y = 30)
Button(f4,text="Show Data",font="arial 18 bold",command=show_data).place(x = 175, y = 30)
f4.place(x = 330, y = 510)

root.mainloop()