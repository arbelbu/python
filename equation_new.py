import re
import tkinter as tk

def split(mish):
    part=mish.partition("=")
    a=re.sub(r"((?:\d+))((x)|\()", r"\1*\2", str(part[0]))
    b=re.sub(r"((?:\d+))((x)|\()", r"\1*\2", str(part[2]))
    print (b)
    return (a.strip(),b.strip())
assert(split("a=3") == ("a","3"))
assert(split("3x+4=5") == ("3*x+4","5"))
assert(split("5=3x+4") == ("5","3*x+4"))
assert(split("5 = 3x+4") == ("5","3*x+4"))
assert(split(" 5 = 3x+4 ") == ("5","3*x+4"))
pass
def negate(input):
    a=input.strip()
    a="-("+a+")"
    
    return a
#assert(negate("x") == "-x")
assert(negate("-x") == "-(-x)")
assert(negate(" x ") == "-(x)")
assert(negate("3") == "-(3)")
assert(negate("-3") == "-(-3)")
#assert(negate("2x+6") == "-2x-6")
#assert(negate("-7x+6") == "+7x-6")
#assert(negate("5+7-3x+3x") == "-5-7+3x-3x")
def one_side (in_):
    part = split(in_)
    minos=negate(part[1])
    in_=part[0]+minos
    in_=in_.lstrip()
    return in_


def mekadem_hofshi(trgil):
    x=0
    p=eval(trgil)
    return p
def mekadmim(trgil):
    m=mekadem_hofshi(trgil)
    trgil+="-("+str(m)+")"
    x=1
    m_x=eval(trgil)
    return (m, m_x) 

assert (mekadem_hofshi("40+5-5*7")==10)
assert (mekadem_hofshi("40+5-5*7*x")==45)
#print(mekadmim("40+5-5*7*x"))



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

t = "3*x+12=3-2*x"
x = liftor(t)
s = t.partition("=")
#print("left :", eval(s[0]))
#print("right :", eval(s[2]))

t = "3+12=3-2+324-2*(6+3)"

print (re.sub(r"((?:\d+))((x)|\()", r"\1*\2", t))
pass


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
