# split the equation to two parts
# e.g. split("3x+4=5") is ("3x+4","5")
def split(mish):
    part=mish.partition("=")
    return (part[0].strip(),part[2].strip())

# test of split
assert(split("a=3") == ("a","3"))
assert(split("3x+4=5") == ("3x+4","5"))
assert(split("5=3x+4") == ("5","3x+4"))
assert(split("5 = 3x+4") == ("5","3x+4"))
assert(split(" 5 = 3x+4 ") == ("5","3x+4"))

# negate a algebric phrase
# e.g. negate("-7x+6") is "7x-6"
def negate(input):
    a=input.strip()
    a = "+" + a
    a = a.replace("+-", "-")
    a = a.replace("-", "&")
    a = a.replace("+", "-")
    a = a.replace("&", "+")
    return a

assert(negate("x") == "-x")
assert(negate("-x") == "+x")
assert(negate(" x ") == "-x")
assert(negate("3") == "-3")
assert(negate("-3") == "+3")
assert(negate("2x+6") == "-2x-6")
assert(negate("-7x+6") == "+7x-6")
assert(negate("5+7-3x+3x") == "-5-7+3x-3x")

# one_side
# Take an equation and put all elements in one side
# e.g. : one_side("12x+4=43+5x")="12x+4-43-5x"
def one_side (in_):
    part = split(in_)
    minos=negate(part[1])
    in_=part[0]+minos
    in_=in_.lstrip()
    return in_

assert(one_side("5x--5=10")=="5x--5-10")
assert(one_side("12x+4x=-43+5x")=="12x+4x+43-5x")

def do_x (q):
    imp = []
    q=q.replace("+","@+")
    q=q.replace("-","@-")
    trck=q.split("@")
    if '' in trck:
        trck=trck.remove ('')
    imp+=trck
    return imp

assert(do_x("12x+4x-43+5x")==['12x','+4x','-43','+5x'])
assert(do_x('+3+3x')==['+3','+3'])
pass
def mehber (imp):
    rx = []
    r = []
    for dd in imp:
        if "x" in dd:
            rx+=[dd]
        else:
             r+=[dd]
    return (rx,r)

assert(mehber(['12x','+4x','-43','+5x','+2'])==(['12x','+4x','+5x'],['-43','+2']))
assert(mehber(['12x','+x6','-43','+5x','+2'])==(['12x','+x6','+5x'],['-43','+2']))

def schoom (nosaf):
    i=0
    for s in nosaf :
        s = s.replace('x', '')
        i+=int(s)
    return i

assert(schoom(['12','+6','-4','+5','+2'])==21)
assert(schoom(['12x','+x6','-4','+4x','+2'])==20)



def liftor(mish):
   
    return r
 
mish = "3x+3=-3-3x"
l,r=split(mish)
r=negate(r)
l=do_x(l)
r=do_x(r)
meaohd=l+r
x,nox=mehber(meaohd)
x=schoom (x)
nox=schoom (nox)
pass
#mesh =input("Give the equation")
#print("x=",liftor(mish))