import tkinter as tk
import time


win = tk.Tk()
c= tk.Canvas(win,height=100,width=100)

btn= tk.StringVar()

def arbel():
   btn.set("Hello arbel")
   
   #B = tk.Button(win, text ="Hello arbel", command = arbel)
   #B.pack()
   #c.create_text(50,50,text="Hello arbel")

B = tk.Button(win, textvariable =btn, command = arbel)
btn.set("Hello")
B.pack()
c.pack()
pass
tk.mainloop()
pass  
