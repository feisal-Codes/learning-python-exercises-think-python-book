
import copy
import math
class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """


class Rect:
    """Represents a rectangle.

    attributes: width ,height ,corner
    """
    
def distance_between_points(p1,p):
    distance=math.sqrt(math.pow((p1.x - p.x),2) + math.pow((p1.y- p.y),2))
    return distance
    

def print_point(p):
    print(('%g, %g')%(p.x,p.y))

def find_center(rect):
    p=Point()
    p.x=rect.corner.x + rect.width/2
    p.y=rect.corner.y + rect.height/2
    return p

def move_rectangle(rect,dx,dy):
    rect.corner.x+=dx
    rect.corner.y+=dy

#object creation
#blank=Point()
box=Rect()
#initializing and object
#blank.x=3
#blank.y=4
#initiatilizing box object
box.width=200.0
box.height=100.0
#embeded object
box.corner=Point()
box.corner.x=0.0
box.corner.y=0.0
box2=copy.deepcopy(box)
box2.corner.x=3
box2.corner.y=4
move_rectangle(box2,3,4)
move_rectangle(box,1,2)

#center=find_center(box)
#print_point(center)


print(box2.corner.x,box2.corner.y)
print(box.corner.x,box.corner.y)












