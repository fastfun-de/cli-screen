#!/usr/bin/env python3
# -.-coding=UTF8 -.-
#
#
#  cli-screen
#
# created Jan. 6th, 2022
#
#
# A tool to define a virtual text screen on the command line
#
# TODO: DOES NOT WORK in ANSI , use xterm commandS!!
#



class Screen:


    def __init__(self, x, y,fill ="µ"):
        assert  0 < x <200
        assert  0 < y <50
        self.x = x
        self.y = y
        
        
        self.array = [[fill for _ in range(self.x)] for _ in range(self.y)] 
        # don't use this !!
        #self.array=[fill]*self.x
        #self.array=[self.array]*self.y
    
    def display(self):
        escape=""
        up ="\033[A"
        for ydir in range(self.y):
            escape += up
            line=""
            for xdir in range(self.x):
                #line +=str(xdir)+","+str(ydir)+self.array[ydir][xdir]
                line +=self.array[ydir][xdir]
            print (str(ydir)+": "+line) 
        print(escape +up )
         
       
    
    def end(self):
        escape =""
        for ydir in range(self.y+1):
            escape +="\033[B"
        print(escape )
        

    def printonecharat(self,qx,qy,fill="."):
        #print (self.array)
        self.array[qy][qx]=fill
        #print (self.array)0
        
    def printstringat(self,qx,qy,printstring ,width=8, fill=" "):
        fills = fill * width
        printstring = printstring +fills

        for singlecharpos in range(width):
            if (qx+singlecharpos)<self.x:
                self.printonecharat(qx+singlecharpos,qy,printstring[singlecharpos])
       



if __name__ == '__main__':
    hallo = Screen(60,5,"*")
    hallo.display()
    hallo.printonecharat(9,0,"a")
    hallo.display()
    hallo.printstringat(58,2,"12345")
    hallo.display()
    hallo.end()




