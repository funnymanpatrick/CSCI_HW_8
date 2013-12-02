from Ball import *
#check for graphics
graphics = raw_input("Use graphics? ==>").lower() == "y"
#check for random
random = raw_input("Use random balls? ==>").lower() == "y"
#get data file
data_file = open(raw_input("Input file location ==>"))
#counter to find first line in file
i = 0
balls = []
for line in data_file:
    l = line.strip().split(" ")
    #parse first line of doc
    if i == 0:
        N = l[0]
        maxit = l[1]
        xbound = l[2]
        ybound = l[3]
    #every other line
    else:
        #if random parse 2nd line and generate N balls
        if random:
            maxspeed = l[0]
            minr = l[1]
            maxr = l[2]
            for i in range(N):
                balls.append(randomball(maxspeed,minr,maxr,xbound,ybound))
        #generate the ball from the doc
        else:
            balls.append(Ball(l[0],l[1],l[2],l[3],l[4],l[5]))
    i += 1
    
    
raw_input()
