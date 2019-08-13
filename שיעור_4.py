from turtle import *
speed(10000)
left(90)
def fw ():
    forward(10)
def bw ():
    backward(10)
def ri ():
    right(90) 
    forward(10)
    left(90)   
def le ():
    left(90)
    forward(10)
    right(90) 
def l7 ():
    left(45)
    forward(11)
    right(45)
def r9 ():
    right(45)
    forward(11)
    left(45)
def l1 ():
    left(135)
    forward(11)
    right(135)
def r3 ():
    right(135)
    forward(11)
    left(135)
x=0
def pu ():
    global x
    if x==0:
        penup()
        x="2"
    else:
        pendown()
        x=0
#def pd ():
#    pendown()
def cl ():
    clear()
def gr ():
    color("green","green")
def rd ():
    color("red","red")
def bl ():
    color("black","black")
def wh ():
    color("white","black")
def prt ():
    color("purple","purple")
def bu ():
    color("blue","blue")
def ye ():
    color("yellow","yellow")
def pi ():
    color("pink","pink")
def bg ():
    begin_fill()
def en ():
    end_fill()
a=1
pensize(width=a)
def ps ():
    global a
    a+=1
    pensize(width=a)
b=1
pensize(width=b)
def po ():
    global b
    b-=1
    pensize(width=b)
begin_fill()
onkey(pu,"5")
#onkey(pd,"0")
onkey(fw, "8")
onkey(bw,"2")
onkey(ri, '6')
onkey(le,'4')
onkey(l7,"7")
onkey(r9,"9")
onkey(l1, "1")
onkey(r3,"3")
onkey(cl,"c")
onkey(gr, "g")
onkey(rd,"r")
onkey(bl,"b")
onkey(wh,"w")
onkey(prt, "z")
onkey(bu,"x")
onkey(ye,"s")
onkey(pi,"d")
onkey(bg, "q")
onkey(en,"a")
onkey(ps,"p")
onkey(po,"o")
end_fill()
listen()
mainloop()