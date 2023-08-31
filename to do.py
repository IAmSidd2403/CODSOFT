from tkinter import *

def add():
    val1 = e1.get()
    li.insert(END, val1)
    e1.delete(0, END)

def remove():
    de = li.curselection()
    li.delete(de)

def clear():
    li.delete(0, END)



root = Tk()
root.title("TO DO LIST")
root.geometry("500x700")



fr4 = Frame(root, bg="#333333")
fr4.pack(expand=TRUE, fill=BOTH)

e1 = Entry(fr4,font="Segoe 13 ", width=40)
e1.grid(row=1,column=2)

b12 = Button(fr4, text="ADD", font="Segoe  ", relief=GROOVE, bd=0,command=add, fg="white", bg="#333333", width=7, height=2)
b12.grid(row=2, column=2)

b1 = Button(fr4, text="DELETE", font="Segoe  ", relief=GROOVE, bd=0,command=remove, fg="white", bg="#333333", width=7, height=2)
b1.grid(row=3, column=2)

b11 = Button(fr4, text="CLEAR ALL", font="Segoe  ", relief=GROOVE, bd=0,command=clear, fg="white", bg="#333333", width=12, height=3)
b11.grid(row=4, column=2)
li = Listbox(fr4,selectmode=SINGLE, width=40, height=10)
li.grid(row=5, column=2)

l1=Label(fr4,text="Topic :  ",font="Segoe",fg='white',bg="#333333")
l1.grid(row=1,column=1)

l2=Label(fr4,text="TO DO LIST :  ",font="Segoe",fg='white',bg="#333333")
l2.grid(row=5,column=1)

root.mainloop()

