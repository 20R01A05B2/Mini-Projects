#Declaring global values
a=0
b=0
i=0
result=""
textentered=""
#Declaring assign function
def assign(v):
        global a
        global b
        global i
        global result
        global textentered
        if(i==0):
                a=str(a)
                v=str(v)
                a=a+v
                a=int(a)
        else:
            b=str(b)
            v=str(v)
            b=b+v
            b=int(b)
#Declaring numbers function
def one():
        global textentered
        textentered=textentered+"1"
        display()
        assign(1)
def two():
        global textentered
        textentered=textentered+"2"
        display()
        assign(2)
def three():
        global textentered
        textentered=textentered+"3"
        display()
        assign(3)
def four():
        global textentered
        textentered=textentered+"4"
        display()
        assign(4)
def five():
        global textentered
        textentered=textentered+"5"
        display()
        assign(5)
def six():
        global textentered
        textentered=textentered+"6"
        display()
        assign(6)
def seven():
        global textentered
        textentered=textentered+"7"
        display()
        assign(7)
def eight():
        global textentered
        textentered=textentered+"8"
        display()
        assign(8)
def nine():
        global textentered
        textentered=textentered+"9"
        display()
        assign(9)
def zero():
        global textentered
        textentered=textentered+"0"
        display()
        assign(0)
#Declaring plus function:
def plus():
        global textentered
        global i
        global a
        global b
        textentered=textentered+"+"
        display()
        if(i>0):
                a=operations()
                b=0
                pass
        i=1
def minus():
        global textentered
        global i
        global a
        global b
        textentered=textentered+"-"
        display()
        if(i>0):
                a=operations()
                b=0
                pass
        i=2
def multiply():
        global textentered
        global i
        global a
        global b
        textentered=textentered+"x"
        display()
        if(i>0):
                a=operations()
                b=0
                pass
        i=3
def divide():
        global textentered
        global i
        global a
        global b
        textentered=textentered+"/"
        display()
        if(i>0):
                a=operations()
                b=0
                pass
        i=4
def power():
        global textentered
        global i
        global a
        global b
        textentered=textentered+"^"
        display()
        if(i>0):
                a=operations()
                b=0
                pass
        i=5
def percentage():
        global textentered
        global i
        global a
        global b
        textentered=textentered+"%"
        display()
        if(i>0):
                a=operations()
                b=0
                pass
        i=6
def factorial():
        global textentered
        global i
        global a
        global b
        global result
        textentered=textentered+"!"
        display()
        if(i>0):
                result="ERROR OCCURED"
                show()
        i=7
def fact(a):
        fact=1
        while(a>0):
                fact=fact*a
                a=a-1
        return fact
def GCD():
        global textentered
        global i
        global a
        global b
        textentered=textentered+"GCDOF"
        display()
        if(i>0):
                a=operations()
                b=0
                pass
        i=8
def gcd(a,b):
        for i in range(1,a+1 and b+1):
                if(a%i==0 and b%i==0):
                        gcd=i
        return gcd
def erase():
        global textentered
        global result
        global a
        global b
        global i
        textentered=""
        result=""
        display()
        show()
        a=0
        b=0
        i=0
def delete():
        global textentered
        global i
        global a
        global b
        #textentered=list(textentered)
        deletedvalue=textentered[-1]
        #textentered.pop()
        #textentered=str(textentered)
        textentered=textentered[:len(textentered)-1]
        if(i==0):
                a=str(a)
                a=a[:len(a)-1]
                a=int(a)
        else:
                b=str(b)
                b=b[:len(b)-1]
                b=int(b)
        s='+ - * / % ** ! GCDOF'
        for l in s:
                if l in deletedvalue:
                        i=0
        display()
def operations():
        global result
        if(i==1):
                result=a+b
        elif(i==2):
                result=a-b
        elif(i==3):
                result=a*b
        elif(i==4):
                result=a/b
        elif(i==5):
                result=a**b
        elif(i==6):
                result=a/100
        elif(i==7):
                result=fact(a)
        elif(i==8):
                result=gcd(a,b)
        else:
                if(a==0):
                        result="ERROR OCCURED"
                else:
                        result=a
        return result
def equal():
        global result
        result=operations()
        show()
def show():
        global result
        l1=Label(cal,text=result,bd=10,font="Times 15 bold",height=6,width=90,bg="white").place(x=0,y=160)
def display():
        l=Label(cal,text=textentered,bd=10,font="Times 15 bold",height=6,width=90,bg="grey").place(x=0,y=0)
from tkinter import*
cal=Tk()
cal.geometry("1000x1000")
cal.title("CALCULATOR")
cal.configure(bg="grey")
erasebutton=Button(cal,text="AC",bd=15,font="Times 15 bold",height=6,width=20,bg="white",activebackground="yellow",activeforeground="blue",command=erase).place(x=0,y=320)
deletebutton=Button(cal,text="DEL",bd=15,font="Times 15 bold",height=6,width=20,bg="white",activebackground="yellow",activeforeground="blue",command=delete).place(x=275,y=320)
gcdbutton=Button(cal,text="GCD",bd=15,font="Times 15 bold",height=6,width=20,bg="white",activebackground="yellow",activeforeground="blue",command=GCD).place(x=550,y=320)
factbutton=Button(cal,text="FACT(!)",bd=15,font="Times 15 bold",height=6,width=20,bg="white",activebackground="yellow",activeforeground="blue",command=factorial).place(x=825,y=320)
onebutton=Button(cal,text="1",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=one).place(x=0,y=663)
twobutton=Button(cal,text="2",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=two).place(x=0,y=492)
threebutton=Button(cal,text="3",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=three).place(x=220,y=663)
fourbutton=Button(cal,text="4",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=four).place(x=220,y=492)
fivebutton=Button(cal,text="5",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=five).place(x=440,y=663)
sixbutton=Button(cal,text="6",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=six).place(x=440,y=492)
sevenbutton=Button(cal,text="7",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=seven).place(x=660,y=663)
eightbutton=Button(cal,text="8",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=eight).place(x=660,y=492)
ninebutton=Button(cal,text="9",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=nine).place(x=880,y=663)
zerobutton=Button(cal,text="0",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=zero).place(x=880,y=492)
equalbutton=Button(cal,text="=",bd=10,font="Times 15 bold",height=6,width=34,bg="white",activebackground="yellow",activeforeground="blue",command=equal).place(x=1100,y=663)
plusbutton=Button(cal,text="+",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=plus).place(x=1100,y=492)
minusbutton=Button(cal,text="-",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=minus).place(x=1320,y=492)
multiplybutton=Button(cal,text="x",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=multiply).place(x=1100,y=320)
dividebutton=Button(cal,text="/",bd=10,font="Times 15 bold",height=6,width=16,bg="white",activebackground="yellow",activeforeground="blue",command=divide).place(x=1320,y=320)
powerbutton=Button(cal,text="POWER(^)",bd=10,font="Times 15 bold",height=6,width=34,bg="white",activebackground="yellow",activeforeground="blue",command=power).place(x=1100,y=0)
percentagebutton=Button(cal,text="PERCENTAGE(%)",bd=10,font="Times 15 bold",height=6,width=34,bg="white",activebackground="yellow",activeforeground="blue",command=percentage).place(x=1100,y=160)
show()
display()
cal.mainloop()