from tkinter import *
import webbrowser
from PIL import Image,ImageTk

root = Tk()
root.geometry("993x545")
root.title("Shortcut search")
root.config(bg="#b78119")
root.resizable(False,False)

# Function for searching in the instagram
# Note :- The username should be exactly same as in the instagram otherwise it will not display "!!!object" you are searching for
def search_instagram():
    got_it0 = ent.get().replace("@","")
    url0 = f"https://www.instagram.com/{got_it0}/"
    webbrowser.open(url0)

# Function for searching in the instagram
def search_google():
    got_it = ent.get()
    url = f"https://www.google.com/search?q={got_it}&rlz=1C1CHBD_enNP1069NP1069&oq=code+with+harry&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIHCAEQABiABDIMCAIQABgUGIcCGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAE0gEJNzY3M2owajE1qAIIsAIB&sourceid=chrome&ie=UTF-8"
    webbrowser.open(url)
        

# Function for searching in the instagram
def search_youtube():
    got_it2 = ent.get()
    url1 = f"https://www.youtube.com/results?search_query={got_it2}"
    webbrowser.open(url1)

# Label for showing the text
Label(root,text="Shortcut Search",font="Robote 30  bold",fg="#e3fc08",bg="#b78119").place(x = 330, y = 6)

# Entry widget for taking user's input
ent = Entry(root,font="arial 21 bold",relief=SUNKEN,bd=3,width=27)
ent.place(x = 261, y = 72)

# f1 for instagram
f1 = Frame(root,bg="#b78119",bd=6,relief=RAISED,border=5,height=300,width=270)
f1.place(x = 5, y = 240)
# Logo of instagram
img = Image.open("instagram.jpeg") #instagram logo
img = ImageTk.PhotoImage(img)
# Label to display the logo
Label(f1,image=img,height=180,width=180,bg="#b78119").place(x = 39, y = 9)
# Label to show text
Label(f1,text="Instagram",font="arial 21 bold",bg="#b78119",fg="red").place(x = 66, y = 195)
# Button to search on the instagram
Button(f1,text="Search",font="lucida 18 bold",bg="#b78119",fg="#fcde07",width=12,relief=RAISED,command=search_instagram).place(x = 30, y = 236)



# f2 for google
f2 = Frame(root,bg="#b78119",bd=6,relief=RAISED,border=5,height=300,width=270)
f2.place(x = 360, y = 240)
# Logo of google
img1 = Image.open("google.jpeg") #google logo
img1 = ImageTk.PhotoImage(img1)
# Label to display logo
Label(f2,image=img1,height=180,width=180,bg="#b78119").place(x = 39, y = 9)
# Label to display the text
Label(f2,text="Google",font="arial 21 bold",bg="#b78119",fg="red").place(x = 81, y = 195)
# Button to search on the google
Button(f2,text="Search",font="lucida 18 bold",bg="#b78119",fg="#fcde07",width=12,relief=RAISED,command=search_google).place(x = 30, y = 236)


# f3 for youtube
f3 = Frame(root,bg="#b78119",bd=6,relief=RAISED,border=5,height=300,width=270)
f3.place(x = 715, y = 240)
img3 = Image.open("youtube.jpeg") #youtube logo
img3 = ImageTk.PhotoImage(img3)
# Label to display logo
Label(f3,image=img3,height=180,width=180,bg="#b78119").place(x = 39, y = 9)
# Label to display text
Label(f3,text="youtube",font="arial 21 bold",bg="#b78119",fg="red").place(x = 81, y = 195)
# Button to search on the youtube
Button(f3,text="Search",font="lucida 18 bold",bg="#b78119",fg="#fcde07",width=12,relief=RAISED,command=search_youtube).place(x = 30, y = 236)

root.mainloop()