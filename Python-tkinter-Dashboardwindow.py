from tkinter import*
from tkinter import messagebox

def mainwindow() :
    root = Tk()
    root.title("Dashbroad by Patiphan Arphorn")
    root.geometry("900x550")
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=3)
    root.rowconfigure(2,weight=2)
    root.columnconfigure(0,weight=10)
    root.columnconfigure(1,weight=2)
    return(root)

def layout(root) :
    top = Frame(root,bg="#AEE2FF")
    top.grid(row=0,columnspan=2,sticky="news")
    top.rowconfigure(0,weight=1)
    top.columnconfigure(0,weight=1)

    left = Frame(root,bg="white")
    left.grid(row=1,column=0,sticky="news")
    left.rowconfigure(0,weight=4)
    left.rowconfigure(1,weight=1)
    left.columnconfigure(0,weight=1)
    left.columnconfigure(1,weight=1)
    left.columnconfigure(2,weight=1)
    left.columnconfigure(3,weight=1)

    right = Frame(root,bg="white")
    right.grid(row=1,column=1)
    right.rowconfigure(0,weight=1)
    right.rowconfigure(1,weight=2)


    down = Frame(root,bg="#2B4865")
    down.grid(row=2,columnspan=2,sticky="news")
    down.rowconfigure(0,weight=1)
    down.columnconfigure(0,weight=1)
    down.columnconfigure(1,weight=1)
    down.columnconfigure(2,weight=1)
    down.columnconfigure(3,weight=1)

    return(top,left,right,down)

def topwidget(top) :
    title = Label(top,text="Dashbroad by Patiphan Arphorn",font=("Open Sans",(20)),fg="#02273f",bg="#AEE2FF")
    title.grid(row=0,column=0)

def leftwidget(left) :
    male = Label(left,image=img1,bg="white")
    male.place(x=40,y=15)
    text1 = Label(left,text = "Mister Patiphan Arphorn",font=("Open Sans",(18)),fg="#495579",bg="white")
    text1.place(x=290,y=60)
    text2 = Label(left,text = "Instructor",fg="#495579",bg="white")
    text2.place(x=290,y=115)
    text3 = Label(left,text = "information Technology and Innovation",fg="#495579",bg="white")
    text3.place(x=290,y=160)
    age = Label(left,text = "19\nAge",bg="#68B984")
    age.grid(row=1,column=0,sticky="news")
    weight = Label(left,text = "58\nWeight",bg="#FED049")
    weight.grid(row=1,column=1,sticky="news")
    height = Label(left,text = "175\nHeight",bg="#5DA7DB")
    height.grid(row=1,column=2,sticky="news")
    skill = Label(left,text = "5\nSkill",bg="#E0144C")
    skill.grid(row=1,column=3,sticky="news")

def rightwidget(right) :
    text = Label(right,text= "My English Skill",font=("Open Sans",(16)),fg="#02273f",bg="white")
    text.grid(row=0,column=0,sticky=SW)
    skill = Label(right,image=img2,bg="white")
    skill.grid(row=1,column=0)

def bottomwidget(down) :
    select1 = Button(down,text="Click me 1",bg="#62B6B7",command=click1)
    select1.grid(row=0,column=0,ipadx=35,ipady=15)
    select2 = Button(down,text="Click me 2",bg="#62B6B7",command=click2)
    select2.grid(row=0,column=1,ipadx=35,ipady=15)
    select3 = Button(down,text="Click me 3",bg="#62B6B7",command=click3)
    select3.grid(row=0,column=2,ipadx=35,ipady=15)
    select4 = Button(down,text="Exit Program",bg="#62B6B7")
    select4.grid(row=0,column=3,ipadx=35,ipady=15)

def click1() :
    messagebox.showinfo("Patiphan said :","Click me 1 clicked")

def click2() :
    messagebox.showinfo("Patiphan said :","Click me 2 clicked")

def click3() :
    messagebox.showinfo("Patiphan said :","Click me 3 clicked")


root = mainwindow()
img1 = PhotoImage(file="hw3-images\male.png").subsample(3,3)
img2 = PhotoImage(file="hw3-images\skill.png").subsample(2,2)
top,left,right,down = layout(root)
topwidget(top)
leftwidget(left)
rightwidget(right)
bottomwidget(down)
root.mainloop()