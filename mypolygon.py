import turtle
import math
t=turtle.Turtle()


def polygon(t,length,n):
   for i in range(n):
    t.fd(length)
    t.lt(360/n)
def circle(t,r):
    c=2 * math.pi * r
    n= int(c/3)+3
    length= c/n
    polygon(t,length,n)

circle(t,70)


turtle.mainloop()