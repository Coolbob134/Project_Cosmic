import stddraw

import menus

class enemy:
    x = 0
    y = 0
    size = 0
    active = True

    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.active = True
    
    def update(self):
        stddraw.square(self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,self.size/stddraw._canvasWidth)
        self.x += 50;
        self.y -= 50;

class player:
    x = 0
    y = 0
    health = 10
    score = 0

    def __init__(self):
        self.health = 10
        self.score = 0
        self.x = 10
        self.y = 10
    
    def update(self):
        stddraw.circle(self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,0.1)
        self.score += 1
    
    def move(self,x,y):
        self.x += x
        self.y += y

class bullet:
    x = 0
    y = 0
    vel = 0
    active = True

    def __init__(self):
        self.x = 10
        self.y = 400
        self.active = True

    def update(self):
        if (self.x >= stddraw._canvasWidth or self.x <= 0) or (self.y >= stddraw._canvasHeight or self.y <= 0):
            self.active = False
        self.x += 50
        stddraw.filledCircle(self.x/stddraw._canvasWidth/2,self.y/stddraw._canvasWidth,0.01)

def mainloop():
    enemy1 = enemy(100,700,50)
    plr = player()
    bullets = []

    while 1:
        stddraw.clear(stddraw.GRAY)
        if stddraw.hasNextKeyTyped():
            match stddraw.nextKeyTyped():
                case 'a': plr.move(-50,0)
                case 'd': plr.move(50,0)
                case 'w': plr.move(0,50)
                case 's': plr.move(0,-50)
                case ' ': bullets.append(bullet())
                case '\x1b': menus.pause_menu()
                

        enemy1.update()
        plr.update()
        counter = 0
        while counter < len(bullets):
            bullets[counter].update()
            if bullets[counter].active == False:
                del bullets[counter]
            else:
                counter+= 1

        stddraw.text(0.9,0.97,f"SCORE: {plr.score} ")
        stddraw.text(0.9,0.95,f"HEALTH: {plr.health}")
        stddraw.show(100)


