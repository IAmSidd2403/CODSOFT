from functools import partial
from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry("400x700")  

def bc1():
    p=len(e1.get())
    e1.insert(p,"1")

def bc2():
    p=len(e1.get())
    e1.insert(p,"2")

def bc3():
    p=len(e1.get())
    e1.insert(p,"3")

def bc4():
    p=len(e1.get())
    e1.insert(p,"4")

def bc5():
    p=len(e1.get())
    e1.insert(p,"5")

def bc6():
    p=len(e1.get())
    e1.insert(p,"6")

def bc7():
    p=len(e1.get())
    e1.insert(p,"7")
def bc8():
    p=len(e1.get())
    e1.insert(p,"8")

def bc9():
    p=len(e1.get())
    e1.insert(p,"9")

def bc0():
    p=len(e1.get())
    e1.insert(p,"0")

def bcd():
    p=len(e1.get())
    e1.insert(p,"/")

def bcm():
    p=len(e1.get())
    e1.insert(p,"*")

def bcs():
    p=len(e1.get())
    e1.insert(p,"-")

def bca():
    p=len(e1.get())
    e1.insert(p,"+")



def bca():
    p=len(e1.get())
    e1.insert(p,"+")

def bcdeli():
    p=len(e1.get())
    e1.insert(p,".")


def bcr():
    p=len(e1.get())
    e1.insert(p,"()")


def bcl():
    p=len(e1.get())
    e1.insert(p,")")


def bcX():
    pos = len(e1.get())
    display = str(e1.get())
    e1.delete(0, END)
    e1.insert(0, display[0:pos-1])


def bcC():
    val = len(e1.get())
    display = str(e1.get())
    e1.delete(0, END)
   








def bce():

    value = e1.get()
    value = eval(value)
    e1.delete(0, END)
    e1.insert(0, value)














e1 = Entry(root, font="Segoe 23 ", fg="black", bg="#abbab1", bd=0, justify=RIGHT, insertbackground="#abbab1", cursor="arrow")
e1.pack(expand=TRUE, fill=BOTH)

fr5 = Frame(root, bg="#333333")
fr5.pack(expand=TRUE, fill=BOTH)

b14 = Button(fr5, text="⌫", font="Segoe  ", relief=GROOVE, bd=0,command=bcX, fg="white", bg="#333333", width=10, height=5)
b14.grid(row=1, column=2, sticky="nsew")

b15 = Button(fr5, text="AC", font="Segoe  ", relief=GROOVE, bd=0,command=bcC, fg="white", bg="#333333", width=10, height=5)
b15.grid(row=1, column=1, sticky="nsew")

b16 = Button(fr5, text="÷", font="Segoe  ", relief=GROOVE, bd=0,command=bcd, fg="white", bg="#333333", width=10, height=5)
b16.grid(row=1, column=3, sticky="nsew")

b17 = Button(fr5, text="X", font="Segoe  ", relief=GROOVE, bd=0,command=bcm, fg="white", bg="#333333", width=10, height=5)
b17.grid(row=1, column=4, sticky="nsew")

fr4 = Frame(root, bg="#333333")
fr4.pack(expand=TRUE, fill=BOTH)

b9 = Button(fr4, text="7", font="Segoe  ", relief=GROOVE, bd=0,command=bc7, fg="white", bg="#333333", width=10, height=5)
b9.grid(row=2, column=1, sticky="nsew")

b10 = Button(fr4, text="8", font="Segoe  ", relief=GROOVE, bd=0,command=bc8, fg="white", bg="#333333", width=10, height=5)
b10.grid(row=2, column=2, sticky="nsew")

b11 = Button(fr4, text="9", font="Segoe  ", relief=GROOVE, bd=0,command=bc9, fg="white", bg="#333333", width=10, height=5)
b11.grid(row=2, column=3, sticky="nsew")

b12 = Button(fr4, text="-", font="Segoe  ", relief=GROOVE, bd=0,command=bcs, fg="white", bg="#333333", width=10, height=5)
b12.grid(row=2, column=4, sticky="nsew")

fr3 = Frame(root, bg="#333333")
fr3.pack(expand=TRUE, fill=BOTH)

b5 = Button(fr3, text="4", font="Segoe  ", relief=GROOVE, bd=0,command=bc4, fg="white", bg="#333333", width=10, height=5)
b5.grid(row=3, column=1, sticky="nsew")

b6 = Button(fr3, text="5", font="Segoe  ", relief=GROOVE, bd=0,command=bc5, fg="white", bg="#333333", width=10, height=5)
b6.grid(row=3, column=2, sticky="nsew")

b7 = Button(fr3, text="6", font="Segoe  ", relief=GROOVE, bd=0,command=bc6, fg="white", bg="#333333", width=10, height=5)
b7.grid(row=3, column=3, sticky="nsew")

b8 = Button(fr3, text="+", font="Segoe  ", relief=GROOVE, bd=0,command=bca, fg="white", bg="#333333", width=10, height=5)
b8.grid(row=3, column=4, sticky="nsew")

fr2 = Frame(root, bg="#333333")
fr2.pack(expand=TRUE, fill=BOTH)

b1 = Button(fr2, text="1", font="Segoe  ", relief=GROOVE, bd=0,command=bc1,fg="white", bg="#333333", width=10, height=5)
b1.grid(row=4, column=1, sticky="nsew")

b2 = Button(fr2, text="2", font="Segoe  ", relief=GROOVE, bd=0,command=bc2, fg="white", bg="#333333", width=10, height=5)
b2.grid(row=4, column=2, sticky="nsew")

b3 = Button(fr2, text="3", font="Segoe  ", relief=GROOVE, bd=0,command=bc3, fg="white", bg="#333333", width=10, height=5)
b3.grid(row=4, column=3, sticky="nsew")

b4 = Button(fr2, text=".", font="Segoe  ", relief=GROOVE, bd=0,command=bcdeli, fg="white", bg="#333333", width=10, height=5)
b4.grid(row=4, column=4, sticky="nsew")

fr6 = Frame(root, bg="#333333")
fr6.pack(expand=TRUE, fill=BOTH)

b = Button(fr6, text=" ( ", font="Segoe  ", relief=GROOVE, bd=0,command=bcr, fg="white", bg="#333333", width=10, height=5)
b.grid(row=5, column=1, sticky="nsew")

b19 = Button(fr6, text=" 0 ", font="Segoe  ", relief=GROOVE, bd=0,command=bc0, fg="white", bg="#333333", width=10, height=5)
b19.grid(row=5, column=2, sticky="nsew")

b20 = Button(fr6, text=")", font="Segoe  ", relief=GROOVE, bd=0,command=bcl, fg="white", bg="#333333", width=10, height=5)
b20.grid(row=5, column=3, sticky="nsew")

b21 = Button(fr6, text="=", font="Segoe  ", relief=GROOVE, bd=0,command=bce, fg="white", bg="#333333", width=10, height=5)
b21.grid(row=5, column=4, sticky="nsew")


root.mainloop()


