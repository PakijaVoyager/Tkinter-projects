from tkinter import *
from time import strftime

root = Tk()
root.geometry("256x152")
root.config(bg="black")
root.title("Digital Clock")
def time_clock():
    text = strftime(' %H:%M:%S %p ')
    lbl.configure(text=text)
    lbl.after(1000,time_clock)


lbl = Label(root,font="digital 27 bold",fg="red",bg="black")
lbl.pack(pady = 60)
time_clock()
root.mainloop()