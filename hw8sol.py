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
        #every other line
        else:
            #if random parse 2nd line and generate N balls
            if random:
                maxspeed = int(l[0])
                minr = int(l[1])
                maxr = int(l[2])
                for i in range(N):
                    balls.append(randomball(maxspeed,minr,maxr,xbound,ybound))
            #generate the ball from the doc
            else:
                balls.append(Ball(int(l[0]),int(l[1]),int(l[2]),int(l[3]),int(l[4]),l[5]))
        i += 1
    
    
raw_input()
