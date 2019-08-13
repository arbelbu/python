from turtle import *

color ("green","pink")
#pensize=(50)
begin_fill()

#x=0
#while x!=5:
def a():
    for a in range(4):
       forward(100)
       right (90)

a()
end_fill()
penup()
left (90)
forward(100)
pendown()
color ("blue","yellow")
begin_fill()
a()
end_fill()
#    x+=1
mainloop()
