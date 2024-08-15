from tkinter import *
import pyshorteners

root = Tk()
root.title("Form")
root.geometry("595x456")
root.config(bg="light grey")

def shorten_1():
    initiate = pyshorteners.Shortener()
    short_url = initiate.tinyurl.short(url_got.get())
    usr_ent.delete(0,END)
    usr_ent.insert(0,short_url)
    print("Shorten URL : ",short_url)

def expand_1():
    initiate = pyshorteners.Shortener()
    expand_url = initiate.tinyurl.expand(url_got.get())
    usr_ent.delete(0,END)
    usr_ent.insert(0,expand_url)
    print("Expand URL : ",expand_url)

Label(root,text="Enter URL",font="Robote 21 bold",bg="light grey").pack(pady = 18)
url_got = StringVar()
usr_ent = Entry(root,width=30,borderwidth=5,font="arial 15 bold",relief="sunken",textvariable=url_got)
usr_ent.pack()

Button(root,text="Shorten",borderwidth=6,width=9,font="lucida 15 bold",command=shorten_1).pack(side = LEFT,padx = 115)
Button(root,text="Expand",borderwidth=6,width=9,font="lucida 15 bold",command=expand_1).pack(side = LEFT)
root.mainloop()
