from tkinter import *
class window:
    def __init__(self , win):
        self.lbl1=Label(win,text="First Number")
        self.lbl2=Label(win,text="Second Number")
        self.lbl3=Label(win,text="Result")
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1=Button(win,text="Add")
        self.btn2=Button(win,text="Sub")
        self.btn3=Button(win,text="Mul")
        self.lbl1.place(x=100,y=50)
        self.t1.place(x=200,y=50)
        self.lbl2.place(x=100,y=100)
        self.t2.place(x=200,y=100)
        self.b1=Button(win,text="Add",command=self.add)
        self.b2=Button(win,text="Sub")
        self.b2.bind("<Button-1>",self.sub)
        self.b3=Button(win,text='Mul')
        self.b3.bind("<Button-1>",self.mul)
        self.b1.place(x=100,y=150)
        self.b2.place(x=200,y=150)
        self.b3.place(x=300,y=150)
        self.lbl3.place(x=100,y=200)
        self.t3.place(x=200,y=200)
    def add(self):
        self.t3.delete(0,'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END,str(result))
    def sub(self,event):
        self.t3.delete(0,'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END,str(result))
    def mul(self,event):
        self.t3.delete(0,'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1*num2
        self.t3.insert(END,str(result))  
Window=Tk()
window(Window)
Window.title("Hello Python")
Window.geometry("400x400+1000+100")
Window.mainloop()


