# Python file to draw buttons using stddraw

import stddraw

class btn:

    width = 0
    height = 0
    text = ""
    x = 0
    y = 0

    def __init__(self,x,y,height,width,text):
        self.width = width
        self.x = x
        self.y = y
        self.height = height
        self.text = text
    
    def draw(self):
        stddraw.setPenRadius(0.0025)
        x0 = self.x - self.width  #left x
        x1 = self.x + self.width  #right x
        y0 = self.y + self.height #top y
        y1 = self.y - self.height #bottom y
        stddraw.line(x0,y0,x1,y0) #top line
        stddraw.line(x0,y1,x1,y1) #bottom line
        stddraw.line(x1,y0,x1,y1) #left line
        stddraw.line(x0,y0,x0,y1) #right line
        stddraw.text(self.x,self.y,self.text)
        stddraw.setPenRadius()

