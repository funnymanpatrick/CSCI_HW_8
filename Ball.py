from math import sqrt,pi
from random import random,choice,randint
class Ball(object):
    #initialization
    def __init__(self,x,y,r,dx,dy,c,num):
        self.x = float(x)
        self.y = float(y)
        self.r = float(r)
        self.dx = float(dx)
        self.dy = float(dy)
        self.c = c
        self.num = num
    #called when print ball is executed
    def __str__(self):
        return 'Ball %i: position (%.1f,%.1f), radius %.1f, motion (%.1f,%.1f), color %s' %(self.num, self.x, self.y, self.r, self.dx, self.dy, self.c)
    #basic move function
    def move(self):
        self.x += self.dx
        self.y += self.dy
    #check if it should bounce against a wall
    def wallcheck(self,xbound,ybound):
        if self. x + self.r > xbound:
            self.dx *= -1
            print self.num
            #x = xbound - self.r
        elif self.x - self.r < 0:
            self.dx *= -1
            print self.num
            #x = self.r
        elif self.y + self.r > ybound:
            self.dy *= -1
            print self.num
            #y = ybound - self.r
        elif self.y - self.r < 0:
            self.dy *= -1
            print self.num
            #y = self.r
    #check if two balls are intersecting, return boolean
    def intersect(self,other):
        dist = sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        if dist <= self.r + other.r:
            return True
        else:
            return False
    #combines two balls and returns new ball
    def combine(self,other,num):
        ars = pi * ( self.r ** 2 )
        aro = pi * ( other.r ** 2 )
        x = (ars * self.x) + (aro * other.x)
        x /= (ars+aro)
        y = (ars * self.y) + (aro * other.y)
        y /= (ars+aro)   
        dx = (ars * self.dx) + (aro * other.dx)
        dx /= (ars+aro) 
        dy = (ars * self.dy) + (aro * other.dy)
        dy /= (ars+aro)
        r = sqrt((ars+aro) / pi )
        if ars >= aro:
            c = self.c
        else:
            c = other.c
        return Ball(x,y,r,dx,dy,c,num)
#generates a random ball with the given arguments
def randomball(maxspeed,minr,maxr,xbound,ybound,num):
    dx = randint(maxspeed*-1,maxspeed)
    dy = randint(maxspeed*-1,maxspeed)
    r = randint(minr,maxr)
    x = randint(minr,(xbound-maxr))
    y = randint(minr,(ybound-maxr))
    color = choice( ["black", "blue", "red", "green", "magenta", "orange", "pink", "purple", "yellow"] )
    return Ball(x,y,r,dx,dy,color,num)
    
        
