from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Restaurant")
root.geometry("1056x852")
root.config(bg="green")

order_dishes = []
total_amount = 0


def order(event):
    global order_dishes, total_amount
    menu = {"TEA": 20, "COFFEE": 30, "SALAD": 50, "PARATHA": 65, "IDLI": 50, "SAMOSA": 20, 'CHOWMEINS': 50,
            "PAKODI": 25, "CHOWMEIN": 60, "ALOO BONDA": 15, "POHA": 30, "GREEN VEG": 150, "CHICKEN": 350,
            "PANEER TIKKA": 200, "VEG ROL": 80, "KADI CHAWAL": 90}
    dish = dishes.get().upper()

    if dish in menu:
        total_amount += menu[dish]
        order_dishes.append(dish)
        Label(root, text=f"{dish} has been ordered", font="Robote 15 bold", fg="blue", width=33).place(x=360, y=570)
        ent.delete(0, END)

    elif dish == "CONFIRM":
        if order_dishes:
            orders_1 = "\n".join(order_dishes)
            dish_order.config(
                text=f"Your order \n{orders_1} \nhas been placed\n\nTotal amount to pay Rs. {total_amount}|-")
        else:
            dish_order.config(text=f"No order has been placed")


    else:
        messagebox.showerror("Not available", f"{dish} is not available, you can order something else")
        ent.delete(0, END)


dishes = StringVar()

break_fast = ['Tea - 20', 'Coffee - 30', 'Salad - 50', 'Paratha - 65']
lunch = ['Idli - 50', "Kadi chawal - 90", 'Chowmeins - 50', 'Pakodi - 25']
snaks = ['Chowmein - 60', 'Aloo bonda - 15', 'Samosa - 20', 'Poha - 30']
dinner = ['Green veg - 150', 'Chicken - 350', 'Paneer tikka - 200', 'Veg rol - 80']

a1 = 30
b1 = 12
Label(root, text="Breakfast", font="lucida 21 bold", bg="red").place(x=a1, y=b1)
for i in range(len(break_fast)):
    b1 += 42
    Label(root, text=f"{break_fast[i]}  Per", font="lucida 12 bold").place(x=a1, y=b1)

b1 = 12
Label(root, text="Lunch", font="lucida 21 bold", bg="red").place(x=300, y=b1)
for i in range(len(lunch)):
    b1 += 42
    Label(root, text=f"{lunch[i]}  Per", font="lucida 12 bold").place(x=300, y=b1)

b1 = 12
Label(root, text="Snaks", font="lucida 21 bold", bg="red").place(x=570, y=b1)
for i in range(len(snaks)):
    b1 += 42
    Label(root, text=f"{snaks[i]}  Per", font="lucida 12 bold").place(x=570, y=b1)

b1 = 12
Label(root, text="Dinner", font="lucida 21 bold", bg="red").place(x=840, y=b1)
for i in range(len(dinner)):
    b1 += 42
    Label(root, text=f"{dinner[i]}  Per Plate", font="lucida 12 bold").place(x=840, y=b1)

btn = Button(root, text="Order", font="lucida 15 bold", borderwidth=6, relief=GROOVE, width=15, fg="orange", bg="grey")
btn.bind("<Button-1>", order)
btn.place(x=470, y=420)

ent = Entry(root, textvariable=dishes, font="lucida 18 bold", borderwidth=9, relief=RAISED, width=30)
ent.place(x=360, y=300)

dish_order = Label(root, text="", bg="green", fg="blue", font="lucida 12 bold")
dish_order.place(x=500, y=660)

root.mainloop()