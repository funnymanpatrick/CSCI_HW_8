import Tkinter as tk
from Ball import *
if __name__ == "__main__":
    #check for graphics
    graphics = raw_input("Use graphics? ==>").lower() == "y"
    #check for random
    random = raw_input("Use random balls? ==>").lower() == "y"
    #get data file
    data_file = open(raw_input("Input file location ==>"))
    #counter to find first line in file
    i = 0
    balls = [] 
    ##  We will create a root object, which will contain all 
    ##  our user interface elements
    ##
    root = tk.Tk()
    root.title("HW 8 Mike and Patrick")
    
    #print data_file.read()
    for line in data_file:
        if len(line) > 2:
            l = line.strip().split()
            #parse first line of doc
            if i == 0:
                N = int(l[0])
                maxit = int(l[1])
                xbound = int(l[2])
                ybound = int(l[3])
                ##  Create a canvas, like an image, that we can draw objects on.
                ##  This canvas is called chart_1.  By passing root in the call
                ##  before, chart_1 is attached to the root canvas.
                ##
                maxx = xbound # canvas width, in pixels
                maxy = ybound # canvas height, in pixels
                chart_1 = tk.Canvas(root, width=maxx, height=maxy, background="white")
                chart_1.grid(row=0, column=0)
            #every other line
            else:
                #if random parse 2nd line and generate N balls
                if random:
                    maxspeed = int(l[0])
                    minr = int(l[1])
                    maxr = int(l[2])
                    for i in range(N):
                        balls.append(randomball(maxspeed,minr,maxr,xbound,ybound,i))
                #generate the ball from the doc
                else:
                    balls.append(Ball(int(l[0]),int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5],i-1))
            i += 1
    print 'Initial ball configuration'
    for ball in balls:
        print ball
    ##  Loop until the ball runs off the screen.
    i = 0
    bNum = len(balls)
    while len(balls) > 1 and i < maxit:
        i += 1
        wait_time = 20
        chart_1.after(wait_time)
        chart_1.delete(tk.ALL)
        for b in balls:
            b.move()
            b.wallcheck(xbound, ybound)
            for ball in balls:
                if ball != b:
                    if b.intersect(ball):
                        print 'Iteration %i collision between ball %i and %i to form ball %i' %(i, b.num, ball.num, bNum)
                        print b
                        print ball
                        balls.append(b.combine(ball,bNum))
                        balls.remove(b)
                        balls.remove(ball)
                        print 'New', str(balls[-1])
                        print 'Num remaining: %i' %len(balls)
                        bNum += 1
                        break
            if graphics:
                bounding_box = (b.x-b.r, b.y-b.r,b.x+b.r, b.y+b.r)
                chart_1.create_oval(bounding_box, fill=b.c)
                chart_1.update()
    if len(balls) == 1:
        print 'Ends at iteration %i with only ball %i remaining' %(i, balls[0].num)
    else:
        print 'Ends at iteration %i with %i balls remaining:' %(i, len(balls))
        for ball in balls:
            print ball
    ## This is an infinite loop that allows the window to listen to
    ## "events", which are user inputs.  The only user event here is
    ## closing the window, which ends the program. 
    root.mainloop()
