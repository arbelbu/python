import tkinter as tk
win = tk.Tk()
win.geometry("150x150")

f1 = tk.Frame(win, background="blue")
f2 = tk.Frame(win, background="pink")

f1.pack(side="left", fill="both", expand=True)
f2.pack(side="right", fill="both", expand=True)

button = tk.Button(win, text="click me!")
button.place(x=10, y=10, in_=win)

win.mainloop()
