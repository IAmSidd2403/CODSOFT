from tkinter import *
from tkinter import ttk
import random


def pas():
    
 
    length = le.get()
 
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*"
    password = ""
 
    if ch.get() == 'Low Strength':
        for i in range(0, length):
            password = password + random.choice(lower)
            e2.delete(0,END)
        e2.insert(0,password)
 

    elif ch.get() == 'Medium Strength':
        for i in range(0, length+1):
            password +=  random.choice(upper)
            e2.delete(0,END)
        e2.insert(0,password)
 
    elif ch.get() == 'High Strength':
        for i in range(0, length+1):
            password = password + random.choice(digits)
            e2.delete(0,END)
        e2.insert(0,password)
    else:
        e2.insert(0,"Please choose an option")


root=Tk()
root.title("PASSWORD GENERATOR")
root.geometry("700x400+300+400")


fr1 = Frame(root, bg="#333333")
fr1.pack(expand=TRUE, fill=BOTH)

l1 = Label(fr1, text="Password Length:",font="Segoe 15",fg="white", bg="#333333")
l1.grid(row=1,column=1,pady=10)

le=IntVar()
e1=Entry(fr1,textvariable=le,font="Segoe 15",fg='white',bg="#999999",width=20)
e1.grid(row=1,column=2)

l2 = Label(fr1, text="Password Strength:",font="Segoe 15",fg="white", bg="#333333")
l2.grid(row=3,column=1,pady=10)

l3 = Label(fr1, text="Password :",font="Segoe 15",fg="white", bg="#333333")
l3.grid(row=4,column=1,pady=10)

ch=ttk.Combobox(fr1,font=('Arial',14),width=15)
ch['values']=('Low Strength','Medium Strength','High Strength')
ch.current(1)
ch.grid(row=3,column=2)

b = Button(fr1, text="Genrate", font="Segoe  ", relief=GROOVE, bd=0,command=pas,fg="white", bg="#999999" )
b.place(x=300,y=200)

e2 = Entry(fr1, font="Segoe 23 ", fg="white", bg="#333333", bd=0, insertbackground="#999999")
e2.grid(row=4,column=2)


root.mainloop()