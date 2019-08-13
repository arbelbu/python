import tkinter as tk
import random
import time

win = tk.Tk()
c= tk.Canvas(win,height=200,width=200)

rps=['אבן','נייר','מספריים']
com=0
pla=0

def a (plac):
    global com, pla 
    c.delete("tag_")
    c.delete("tag__")
    comc=random.choice(rps)
    c.create_text(100,150,text=("המחשב בחר  "+comc),tag="tag__")
    if (plac=="אבן" and comc=="מספריים") or (plac=="מספריים" and comc=="נייר") or (plac=="נייר" and comc=="אבן"):
        pla+=1
    elif plac!=comc:
        com+=1
    c.create_text(100,50,text="התוצאה : {} למחשב ו{} לי".format(com,pla),tag="tag_")
    if pla==3:
        c.create_text(100,10,text="!!! ניצחת")
        time.sleep(6) 
        exit   
    if com==3:
        c.create_text(100,10,text="המחשב ניצח")
        time.sleep(6) 
        exit 
        
c.create_text(100,100,text="בחר: אבן, נייר או מספריים")
#E = tk.Entry(win)

def gr():    
    a("אבן")
    

def gp():    
    a("נייר")

def gs():    
    a("מספריים")
    
  #  c.delete("tag_")
 #   c.create_text(100,100,text=('x=',stri),tag="tag_")

Br= tk.Button(win,text='אבן', command = gr)
Bp= tk.Button(win,text='נייר', command = gp)
Bs= tk.Button(win,text='מספריים', command = gs)

#E.pack()
c.pack()
Br.pack()
Bp.pack()
Bs.pack()

tk.mainloop()



