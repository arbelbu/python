from tkinter import *
import time
import tkinter
tk = Tk()
c= Canvas(tk,height=100,width=100)

start =(50,50)

def arbel():
   c.create_text(50,50,text="Hello arbel")

B = Button(tk, text ="Hello", command = arbel)
B.pack()
c.pack()
pass
tk.mainloop()
pass  
