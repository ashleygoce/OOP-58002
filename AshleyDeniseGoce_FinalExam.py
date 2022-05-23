from tkinter import *
window = Tk()
window.geometry("400x300+20+10")
window.title('Final Exam')

lbl1 = Label(window, text="Find the least among three numbers", fg="blue", bg="yellow")
lbl1.place(relx=0.50, y=50, anchor="center")

lbl2 = Label(window, text="Enter the first number:")
lbl2.place(x=50, y=80)
txtfld2 = Entry(window, bd=3)
txtfld2.place(x=200, y=80)

lbl3 = Label(window,text="Enter the second number:")
lbl3.place(x=50,y=120)
txtfld3=Entry(window,bd=3)
txtfld3.place(x=200,y=120)

lbl4 = Label(window, text="Enter the third number:")
lbl4.place(x=50, y=160)
txtfld4=Entry(window,bd=3)
txtfld4.place(x=200,y=160)


def Average():
    minnum.delete(0,"end")
    num1=int(txtfld2.get())
    num2=int(txtfld3.get())
    num3=int(txtfld4.get())
    answer = min(num1, num2, num3)
    minnum.insert(END,str(answer))


btn1=Button(window,text="Find",width=10,command=Average)
btn1.place(x=200, y=208, anchor="center")
lbl5 = Label(window,text = "Lowest Value", fg="red")
lbl5.place(x=150, y=260)
minnum = Entry(window)
minnum.place(x=138, y=240)


window.mainloop()
