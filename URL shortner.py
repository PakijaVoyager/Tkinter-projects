from tkinter import *
import pyshorteners

root = Tk()
root.title("Form")
root.geometry("595x456")
root.config(bg="light grey")

def apply():
    initiate = pyshorteners.Shortener()
    short_url = initiate.tinyurl.short(url_got.get())
    usr_ent.delete(0,END)
    usr_ent.insert(0,short_url)
    print(short_url)

Label(root,text="Enter URL",font="Robote 21 bold",bg="light grey").pack(pady = 18)
url_got = StringVar()
usr_ent = Entry(root,width=30,borderwidth=5,font="arial 15 bold",relief="sunken",textvariable=url_got)
usr_ent.pack()

Button(root,text="Convert",borderwidth=6,width=9,font="lucida 15 bold",command=apply).pack(pady = 21)
root.mainloop()