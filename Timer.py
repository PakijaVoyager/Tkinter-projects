from tkinter import *
import time
from playsound import playsound
import threading

def start_timer():
    time_usr = usr_val.get()
    if time_usr <= 0:
        return
    clock_timer(time_usr)
    
def clock_timer(time_counter):
    if time_counter >= 0:
        hours = int(time_counter/3600)
        minss = int(time_counter/60)%60
        sec = time_counter % 60   
        text = f"{hours:02}:{minss:02}:{sec:02}"
        lbl.configure(text=text)
        root.after(1000,clock_timer,time_counter-1)
        if time_counter==0:
            threading.Thread(target=playsound,args=("timer.wav",)).start()
            
        
root = Tk()
root.title("Timer")
root.geometry("656x456")
root.config(bg="black")

# icon setting
img = PhotoImage(file="timer.png")
root.iconphoto(False,img)

# 
lbl = Label(root,text="Enter time in seconds : ",font="digital 24 bold",bg="black",fg="red")
lbl.place(x = 72, y = 24)

# Label for showing the timer
lbl = Label(root,font="digital 24 bold",bg="black",fg="red")
lbl.place(x = 180, y = 180)

# Entry widget for asking user time in seconds
usr_val = IntVar()
ent = Entry(root,font="arial 21 bold",bd=3,relief=RAISED,width=6,textvariable=usr_val)
ent.place(x = 450, y = 24)

Button(root,text="Set",font="Robote 18 bold",bd=6,relief=RAISED,bg="black",fg="blue",width=9,command=start_timer).place(x = 240, y = 81)

root.mainloop()