import tkinter
from tkinter import *
c = 0
tk = Tk()
tk.title("Calculator by Machinexa")

Input = Entry(tk, width=100)
Input.grid(row=0, column=0, columnspan=3, padx=50, pady=50)

def onClick(n):
    global c
    if c == 0:
        Input.delete(0, END)
        c += 1
    data = Input.get()
    Input.delete(0, END)
    data = str(data) + str(n)
    Input.insert(0, data)

def onClear():
    Input.delete(0, END)

def onEq():
    data = Input.get()
    evaluate = eval(data)
    Input.delete(0, END)
    Input.insert(0, evaluate)

Button1 = Button(tk, text=1, padx=100, pady=40, command=lambda: onClick(1))
Button2 = Button(tk, text=2, padx=100, pady=40, command=lambda: onClick(2))
Button3 = Button(tk, text=3, padx=100, pady=40, command=lambda: onClick(3))
Button4 = Button(tk, text=4, padx=100, pady=40, command=lambda: onClick(4))
Button5 = Button(tk, text=5, padx=100, pady=40, command=lambda: onClick(5))
Button6 = Button(tk, text=6, padx=100, pady=40, command=lambda: onClick(6))
Button7 = Button(tk, text=7, padx=100, pady=40, command=lambda: onClick(7))
Button8 = Button(tk, text=8, padx=100, pady=40, command=lambda: onClick(8))
Button9 = Button(tk, text=9, padx=100, pady=40, command=lambda: onClick(9))
Button0 = Button(tk, text=0, padx=100, pady=40, command=lambda: onClick(0), width=36)
ButtonAdd = Button(tk, text="+", padx=50, pady=30, command=lambda: onClick("+"), width=1)
ButtonSub = Button(tk, text="-", padx=50, pady=30, command=lambda: onClick("-"), width=1)
ButtonMul = Button(tk, text="*", padx=50, pady=30, command=lambda: onClick("*"), width=1)
ButtonDiv = Button(tk, text="/", padx=50, pady=30, command=lambda: onClick("/"), width=1)
ButtonCls = Button(tk, text="C", padx=50, pady=10, command=onClear, width=1)
ButtonEq = Button(tk, text="=", padx=100, pady=40, command=lambda: onEq())


Button1.grid(row=3, column=0, )
Button2.grid(row=3, column=1, )
Button3.grid(row=3, column=2, )
Button4.grid(row=4, column=0, )
Button5.grid(row=4, column=1, )
Button6.grid(row=4, column=2, )
Button7.grid(row=5, column=0, )
Button8.grid(row=5, column=1, )
Button9.grid(row=5, column=2, )
Button0.grid(row=6, column=0, columnspan=2 )
ButtonEq.grid(row=6, column=2, )


ButtonCls.grid(row=0, column=4, )
ButtonAdd.grid(row=3, column=4, )
ButtonSub.grid(row=4, column=4, )
ButtonMul.grid(row=5, column=4, )
ButtonDiv.grid(row=6, column=4, )
tk.mainloop()
