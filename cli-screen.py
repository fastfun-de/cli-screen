#!/usr/bin/env python3
# -.-coding=UTF8 -.-
""" generates a Screen object where strings can be displayed

            cli-screen

small script, created Jan. 6th, 2022

A tool to define a virtual text screen on the command line

 uses xterm commands...
"""



class Screen:


    def __init__(self, x, y,fill ="#"):
        assert  0 < x <200
        assert  0 < y <50
        self.x = x
        self.y = y
        
        
        self.array = [[fill for _ in range(self.x)] for _ in range(self.y)] 
        # don't use this !!
        #self.array=[fill]*self.x
        #self.array=[self.array]*self.y
    
    def display(self):
        """show Screen object"""
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
        """moves Cursor below the Screen object"""
        escape =""
        for ydir in range(self.y+1):
            escape +="\033[B"
        print(escape )
        

    def printonecharat(self,qx,qy,fill="."):
        """ just put one char at a specific location """
        #print (self.array)
        self.array[qy][qx]=fill
        #print (self.array)0
        
    def printstringat(self,qx,qy,printstring ,width=8, fill=" "):
        """ fills a width - long 1 line place """
        fills = fill * width
        printstring = printstring +fills

        for singlecharpos in range(width):
            if (qx+singlecharpos)<self.x:
                self.printonecharat(qx+singlecharpos,qy,printstring[singlecharpos])
       



if __name__ == '__main__':
    display = Screen(60,5,"*")
    display.display()
    display.printonecharat(9,0,"a")
    display.display()
    display.printstringat(58,2,"12345")
    display.display()
    display.end()




