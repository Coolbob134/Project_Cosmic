import stddraw, random

import menus
import picture




class enemy:
    x = 0
    y = 0
    size = 0
    active = True

    def __init__(self,x,y,size,speed):
        self.x = x
        self.y = y
        self.size = size
        self.active = True
        self.speed = speed
    
    def update(self):
        stddraw.square(self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,self.size/stddraw._canvasWidth)
        rand1 = random.randint(1,5)
        if rand1 == 1:
            rand1 = random.randint(1,3)
            if rand1 == 1 and self.x < stddraw._canvasWidth-self.speed:
                self.x += self.speed
            else:
                if rand1 == 2 and self.x > self.speed:
                    self.x -= self.speed
            rand1 = random.randint(1,3)
            if rand1 == 1:
                self.y -= self.speed
        if self.y <= 0:
            self.active = False

class player:
    x = 0
    y = 0
    health = 10
    score = 0
    invincibility_timer = 0

    def __init__(self):
        self.health = 10
        self.score = 0
        self.x = 20
        self.y = 20
    
    def drawplr(self):
        stddraw.circle(self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,0.01)
    
    def update(self):
        if self.invincibility_timer > 0:
            self.invincibility_timer -= 1

        if self.invincibility_timer == 0 or self.invincibility_timer % 3 != 0:
            self.drawplr()
        else:
            stddraw.setPenColor(stddraw.WHITE)
            self.drawplr()
            stddraw.setPenColor(stddraw.BLACK)
    
    def move(self,x,y):
        
        self.x += x 
        self.y += y
        if self.x <0:
            self.x = 0
        if self.x > 800:
            self.x = 800
        if self.y <0:
            self.y = 0
        if self.y > 800:
            self.y = 800

class bullet:
    x = 0
    y = 0
    vel = [0,0]
    active = True

    def __init__(self,x,y,velx,vely):
        self.x = x
        self.y = y
        self.vel[0] = velx
        self.vel[1] = vely
        self.active = True

    def update(self):
        if (self.x >= stddraw._canvasWidth or self.x <= 0) or (self.y >= stddraw._canvasHeight or self.y <= 0):
            self.active = False
        self.x += self.vel[0]
        self.y += self.vel[1]
        stddraw.filledCircle(self.x/stddraw._canvasWidth,self.y/stddraw._canvasWidth,0.01)

def mainloop():

    plr = player()
    bullets = []
    counter = 0
    enemies = []
    gameactive = True

    while gameactive == True:
        
        
        stddraw.clear(stddraw.GRAY)
        if plr.health <= 0:
            gameactive = False
            break
        if stddraw.hasNextKeyTyped():
            match stddraw.nextKeyTyped():
                case 'a': plr.move(-40,0)
                case 'd': plr.move(40,0)
                case 'w': plr.move(0,40)
                case 's': plr.move(0,-40)
                case ' ': bullets.append(bullet(plr.x,plr.y,0,50))
                case '\x1b': menus.pause_menu()
                case 'p': enemies.append(enemy(random.randrange(20,780,40),780,20,40))
                

        plr.update()
        counter = 0
        counter2 = 0
        while counter < len(bullets):
            
            counter2 = 0
            while counter2 < len(enemies): #Checks every enemy for collision.
                if (bullets[counter].x >= enemies[counter2].x-enemies[counter2].size*2 and bullets[counter].x <= enemies[counter2].x+enemies[counter2].size*2) and (bullets[counter].y >= enemies[counter2].y-enemies[counter2].size*2 and bullets[counter].y <= enemies[counter2].y+enemies[counter2].size*2):
                    del enemies[counter2]   # deletes enemy that was hit
                    bullets[counter].active == False #effectively deletes current bullet
                    plr.score+=1
                    break
                else:
                    counter2 += 1
            bullets[counter].update()
            if bullets[counter].active == False:
                del bullets[counter] #deletes off screen bullets or bullets that have hit an enemy
            else:
                counter+= 1

        counter = 0
        while counter < len(enemies):
            
            
            if (enemies[counter].x >= plr.x - enemies[counter].size and enemies[counter].x <= plr.x + enemies[counter].size) and (enemies[counter].y >= plr.y - enemies[counter].size and enemies[counter].y <= plr.y + enemies[counter].size) and enemies[counter].active and player.invincibility_timer == 0:
                plr.invincibility_timer = 50
                plr.health -= 1
                enemies[counter].active = False
                
            enemies[counter].update()
            if enemies[counter].active == False:
                del enemies[counter] #deletes enemies that are dead, or enemies that have somehow gotten off screen
            else:
                counter+= 1
        

        stddraw.text(0.9,0.97,f"SCORE: {plr.score} ")
        stddraw.text(0.9,0.95,f"HEALTH: {plr.health}")
        stddraw.show(50)


def endlessloop(): # endless gamemode
    plr = player()
    bullets = []
    counter = 0
    enemies = []
    gameactive = True
    enemycooldown = 10
    healthgained = True
    difficulty_factor = 1

    while gameactive == True:
        
        
        stddraw.clear(stddraw.GRAY)
        if plr.health <= 0:
            gameactive = False
            break
        if stddraw.hasNextKeyTyped():
            match stddraw.nextKeyTyped():
                case 'a': plr.move(-40,0)
                case 'd': plr.move(40,0)
                case 'w': plr.move(0,40)
                case 's': plr.move(0,-40)
                case ' ': bullets.append(bullet(plr.x,plr.y,0,50))
                case '\x1b': menus.pause_menu()
                case 'p': enemies.append(enemy(random.randrange(20,780,40),780,20,40))


        if enemycooldown <= 0 and random.randint(1,int(10*difficulty_factor)) == 1:
            enemycooldown = 20*difficulty_factor
            enemies.append(enemy(random.randrange(0,800,20),780,20,40))
            if plr.score >= 50:
                enemies.append(enemy(random.randrange(0,800,20),780,20,40))
                if plr.score >= 100:
                    enemies.append(enemy(random.randrange(0,800,20),780,20,40))
                    enemies.append(enemy(random.randrange(0,800,20),780,20,40))
        else:
            enemycooldown -= 1

        if plr.score % 10 == 0 and plr.score > 0 and healthgained == False:
            plr.health+=1
            healthgained = True

        if plr.score >= 50:
            difficulty_factor = 0.5
            if plr.score >= 100:
                difficulty_factor = 0.25

        plr.update()
        counter = 0
        counter2 = 0
        while counter < len(bullets):
            
            counter2 = 0
            while counter2 < len(enemies): #Checks every enemy for collision.
                if (bullets[counter].x >= enemies[counter2].x-enemies[counter2].size*2 and bullets[counter].x <= enemies[counter2].x+enemies[counter2].size*2) and (bullets[counter].y >= enemies[counter2].y-enemies[counter2].size*2 and bullets[counter].y <= enemies[counter2].y+enemies[counter2].size*2):
                    del enemies[counter2]   # deletes enemy that was hit
                    bullets[counter].active == False #effectively deletes current bullet
                    plr.score+=1
                    healthgained = False
                    break
                else:
                    counter2 += 1
            bullets[counter].update()
            if bullets[counter].active == False:
                del bullets[counter] #deletes off screen bullets or bullets that have hit an enemy
            else:
                counter+= 1

        counter = 0
        while counter < len(enemies):
            
            
            if (enemies[counter].x >= plr.x - enemies[counter].size and enemies[counter].x <= plr.x + enemies[counter].size) and (enemies[counter].y >= plr.y - enemies[counter].size and enemies[counter].y <= plr.y + enemies[counter].size) and enemies[counter].active and player.invincibility_timer == 0:
                plr.invincibility_timer = 50
                plr.health -= 1
                enemies[counter].active = False
                
            enemies[counter].update()
            if enemies[counter].active == False:
                del enemies[counter] #deletes enemies that are dead, or enemies that have somehow gotten off screen
            else:
                counter+= 1
        

        stddraw.text(0.9,0.97,f"SCORE: {plr.score} ")
        stddraw.text(0.9,0.95,f"HEALTH: {plr.health}")
        stddraw.show(50)
