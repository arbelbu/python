import tkinter as tk
import time


win = tk.Tk()
c= tk.Canvas(win,height=1000,width=1000)

btn= tk.StringVar()
E = tk.Entry(win)
def arbel():
   btn.set("Hello arbel")
   c.create_text(50,50,text=E.get())

B = tk.Button(win, textvariable =btn, command = arbel)
btn.set("Hello")


E.pack()
B.pack()
c.pack()
pass
tk.mainloop()

