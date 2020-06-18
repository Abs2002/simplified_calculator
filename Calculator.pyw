from tkinter import *
from math import *

try:
    rt=Tk()
    rt.geometry("710x700")
    rt.maxsize("710", "700")
    rt.title("Calculator 2.1.12")
    rt.configure(background="black")

    def num(x):
        global op
        op=op+str(x)
        scv.set(op)
    def clear():
        global op
        op=""
        scv.set(op)
    def eq():
        global op
        op=str(eval(op))
        scv.set(op)
    op=""

    scv=StringVar()
    en=Entry(rt, font=("bold", 45), justify="right", textvariable=scv)
    en.place(x=20, y=30)

    b1=Button(rt, text="1", padx=20, pady=20, command=lambda:num(1), font=(35), bg="red")
    b2=Button(rt, text="2", padx=20, pady=20, command=lambda:num(2), font=(35), bg="red")
    b3=Button(rt, text="3", padx=20, pady=20, command=lambda:num(3), font=(35), bg="red")
    b4=Button(rt, text="4", padx=20, pady=20, command=lambda:num(4), font=(35), bg="red")
    b5=Button(rt, text="5", padx=20, pady=20, command=lambda:num(5), font=(35), bg="red")
    b6=Button(rt, text="6", padx=20, pady=20, command=lambda:num(6), font=(35), bg="red")
    b7=Button(rt, text="7", padx=20, pady=20, command=lambda:num(7), font=(35), bg="red")
    b8=Button(rt, text="8", padx=20, pady=20, command=lambda:num(8), font=(35), bg="red")
    b9=Button(rt, text="9", padx=20, pady=20, command=lambda:num(9), font=(35), bg="red")
    b0=Button(rt, text="0", padx=20, pady=20, command=lambda:num(0), font=(35), bg="red")
    bp=Button(rt, text="+", padx=20, pady=20, command=lambda:num("+"), font=(35), bg="green")
    bs=Button(rt, text="- ", padx=20, pady=20, command=lambda:num("-"), font=(35), bg="green")
    bm=Button(rt, text="* ", padx=20, pady=20, command=lambda:num("*"), font=(35), bg="green")
    bd=Button(rt, text="/ ", padx=20, pady=20, command=lambda:num("/"), font=(35), bg="green")

    b7.place(x=20, y=150)
    b8.place(x=100, y=150)
    b9.place(x=180, y=150)
    b4.place(x=20, y=240)
    b5.place(x=100, y=240)
    b6.place(x=180, y=240)
    b1.place(x=20, y=330)
    b2.place(x=100, y=330)
    b3.place(x=180, y=330)
    b0.place(x=100, y=420)
    bp.place(x=300, y=150)
    bs.place(x=300, y=240)
    bm.place(x=300, y=330)
    bd.place(x=300, y=420)

    be=Button(rt, text="log", font=(35), padx=39, pady=20, command=lambda:num("log("), bg="violet")
    be.place(x=400, y=150)

    bc=Button(rt, text="C", font=(35), padx=20, pady=20, command=clear, bg="yellow")
    bc.place(x=180, y=420)

    bdo=Button(rt, text=". ", font=(35), padx=20, pady=20,command=lambda:num("."), bg="green")
    bdo.place(x=20, y=420)

    bsi=Button(rt, text="sin", font=(35), padx=39, pady=20, command=lambda:num("sin("), bg="violet")
    bco=Button(rt, text="cos", font=(35), padx=35, pady=20, command=lambda:num("cos("), bg="violet")
    btn=Button(rt, text="tan", font=(35), padx=37, pady=20, command=lambda:num("tan("), bg="violet")

    bsi.place(x=400, y=240)
    bco.place(x=400, y=330)
    btn.place(x=400, y=420)

    bcr1=Button(rt, text="( ", font=(35), padx=20, pady=20, command=lambda:num("("), bg="green")
    bcr2=Button(rt, text=") ", font=(35), padx=20, pady=20, command=lambda:num(")"), bg="green")

    bcr1.place(x=20, y=510)
    bcr2.place(x=100, y=510)

    bl=Button(rt, text="=", font=(35), padx=80, pady=20, command=eq, bg="orange")
    bl.place(x=180, y=510)

    blg=Button(rt, text="log10", font=(35), padx=30, pady=20, command=lambda:num("log10("), bg="violet")
    blg.place(x=400, y=510)

    bfc=Button(rt, text="factorial", font=(35), padx=23, pady=20, command=lambda:num("factorial("), bg="blue")
    bfc.place(x=550, y=150)

    bsq=Button(rt, text="square", font=(35), padx=23, pady=20, command=lambda:num("**2"), bg="blue")
    bcu=Button(rt, text="cube", font=(35), padx=30, pady=20, command=lambda:num("**3"), bg="blue")
    bsqr=Button(rt, text="sq root", font=(35), padx=23, pady=20, command=lambda:num("**1/2"), bg="blue")
    bcur=Button(rt, text="cu root", font=(35), padx=23, pady=20, command=lambda:num("**1/3"), bg="blue")

    bsq.place(x=550, y=240)
    bsqr.place(x=550, y=330)
    bcu.place(x=550, y=420)
    bcur.place(x=550, y=510)



    rt.mainloop()

except:
    print("error")
