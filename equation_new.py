import re
import tkinter as tk
import math
#import turtle

def split(mish):
    part=mish.partition("=")
    a=re.sub(r"((?:\d+))((x)|\()", r"\1*\2", str(part[0]))
    b=re.sub(r"((?:\d+))((x)|\()", r"\1*\2", str(part[2]))
    #print (b)
    return (a.strip(),b.strip())

def negate(input):
    a=input.strip()
    a="-("+a+")"
    return a

def one_side (in_):
    part = split(in_)
    minos=negate(part[1])
    in_=part[0]+minos
    in_=in_.lstrip()
    return in_


def mekadmim(trgil):
    x=0.0
    c=eval(trgil)
    trgil+="-("+str(c)+")"
    x=1.0
    n=eval(trgil)
    x=2.0
    m=eval(trgil)
    a=eval('(m-2*n)/2')
    b=eval('n-a')
    return (a,b,c) 
#להוסיף בפונקציה אפשרות למשוואה ריבועית (a) ככתוב בדףשמאחורי המסך< 

assert (mekadmim("3*x**2+4*x+5")==(3,4,5))
#assert (mekadmim("2x**2+2x+4")==28)
pass

def liftor_ribooiot (a,b,c):
    if a==0:
        try:
            return [-c/b]
        except ZeroDivisionError :
            return []
    try:
        x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        return [x1,x2]
    except ValueError:
        return []
assert(liftor_ribooiot(0,0,2) == [])
def liftor(mish):
    l,r=split(mish)
    r=negate(r)
    meaohd=l+r
    a,b,c = mekadmim(meaohd)
    return liftor_ribooiot(a,b,c)


assert(liftor("3*x+3=-3-3*x") == [-1.0])
assert(liftor("22*x=44")==[2])
assert(liftor("-22*x=44")==[-2])
assert(liftor("-22*x=-44")==[2])
assert(liftor('x=6')==[6])
assert(liftor('-6=-x')==[6])
assert(liftor('0.5=x')==[0.5])



#t = "3*x+12=3-2*x"
#x = liftor(t)
#s = t.partition("=")
#print("left :", eval(s[0]))
#print("right :", eval(s[2]))

t = "3+12=3-2+324-2*(6+3)"
#
win = tk.Tk()

c= tk.Canvas(win,height=200,width=200)


c.create_text(100, 10,anchor="center",text="Give the equation")
#'''




E = tk.Entry(win)
#E.pack(side=tk.TOP)
id = 5000
E.place(x=40, y=20, in_=win)
 

def graft(e = None):    
    mish=E.get()
    c.delete("tag1")
    c.delete("tag2")
    try:
        r = liftor(mish)
    except :
        c.create_text(100,100,text=('המשוואה שגויה'),tag="tag1")
        return None
    if len(r) == 0: 
        c.create_text(100,100,text=('אין פתרון'),tag="tag1")
    elif len(r) == 1:
        str1=str(r[0])
        c.create_text(100,100,text=('x=',str1),tag="tag1")
    elif len(r) == 2:
        str1=str(r[0])
        str2=str(r[1])
        c.create_text(100,100,text=('x1=',str1),tag="tag1")
        c.create_text(100,120,text=('x2=',str2),tag="tag2")

win.bind("<Return>", graft)
print ("dd")

c.pack()

tk.mainloop()
