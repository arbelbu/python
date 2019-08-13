import re
import tkinter as tk
import math

def split(mish):
    part=mish.partition("=")
    a=re.sub(r"((?:\d+))((x)|\()", r"\1*\2", str(part[0]))
    b=re.sub(r"((?:\d+))((x)|\()", r"\1*\2", str(part[2]))
    print (b)
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


def mekadem_hofshi(trgil):
    x=0.0
    p=eval(trgil)
    return p
def mekadmim(trgl):
    c=mekadem_hofshi(trgl)
    trgl+="-("+str(c)+")"
    x=1
    n=eval(trgl)
    x=2
    m=eval(trgl)
    a=eval('(m-2*n)/2')
    b=eval('n-a')
    return (a,b,c) 
#להוסיף בפונקציה אפשרות למשוואה ריבועית (a) ככתוב בדףשמאחורי המסך< 
assert (mekadem_hofshi("40+5-5*7")==10)
assert (mekadem_hofshi("40+5-5*7*x")==45)
assert (mekadmim("3*x**2+4*x+5")==(3,4,5))
#assert (mekadmim("2x**2+2x+4")==28)
pass

def liftor(mish):
    l,r=split(mish)
    r=negate(r)
    meaohd=l+r
    nox, x = mekadmim(meaohd)
    return nox/-x


assert(liftor("3*x+3=-3-3*x") == -1.0)
assert(liftor("22*x=44")==2)
assert(liftor("-22*x=44")==-2)
assert(liftor("-22*x=-44")==2)
assert(liftor('x=6')==6)
assert(liftor('-6=-x')==6)
assert(liftor('0.5=x')==0.5)

#t = "3*x+12=3-2*x"
#x = liftor(t)
#s = t.partition("=")
#print("left :", eval(s[0]))
#print("right :", eval(s[2]))

t = "3+12=3-2+324-2*(6+3)"
#
win = tk.Tk()
c= tk.Canvas(win,height=200,width=200)
c.create_text(100,10,text="Give the equation")

E = tk.Entry(win)
id = 5000
def graft():    
    mish=E.get()
    stri=str(liftor(mish))
    
    c.delete("tag_")
    c.create_text(100,100,text=('x=',stri),tag="tag_")

B= tk.Button(win,text='solve', command = graft)

E.pack()
c.pack()
B.pack()

tk.mainloop()
