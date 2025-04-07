import stddraw, random

import menus
import picture



class level:

    contents = []   # level contents loaded in from file
    level_type = 0  # The type of level
    nexttimer = 0   # Timer until next event
    level_counter  = 0
    background = 0
    

    def __init__(self):
        self.level_type = 0
        self.nexttimer = 0
        self.event_counter  = 0
        self.isempty = True
        self.waitempty = False
        self.bossfightactive = False
        self.level_path = ''
        self.level_counter = 1
        self.endlessmode = True

        self.background = picture.Picture("assets/backgrounds/normal_background.png")
        self.boss_background = picture.Picture("assets/backgrounds/boss_background.png")
        self.normal_background = picture.Picture("assets/backgrounds/normal_background.png")
        

    def update(self):
       
        
        match self.contents[self.event_counter][0]:
            case 3: self.bossfightactive == True; return [4,0,0,0]      #boss
            case 4: self.bossfightactive == True; return [4,0,0,0]      #boss_x
            case 5: self.background = self.boss_background              #boss_bg
            case 6: self.background = self.normal_background            #normal_bg
            case 7: return [7,0,0,0]                                    #endless mode
            case 8:                                                     #next_lvl
                self.loadnextlevel()
                self.event_counter = 0
                return [8,0,0,0]

            case 9:                                                     #wait_empty
                if self.isempty == False: self.waitempty = True
                else: self.waitempty = False

        if self.bossfightactive == False and self.endlessmode == False and not((self.waitempty == True and self.isempty == False)):
        
            if self.nexttimer <= 0:
                if self.event_counter < len(self.contents)-1:
                    returnarr = self.contents[self.event_counter][:4]
                    self.event_counter += 1
                    self.nexttimer = self.contents[self.event_counter][4]
                    return returnarr
                else:
                    self.nexttimer = 0
                    return [0,0,0,0]    # level empty
            else:
                self.nexttimer -= 1
                return [100,0,0,0]      # timer not ready
        else: return [100,0,0,0]


    def loadlevelfromfile(self,path): # called after initialization if level needs to be initialized
        self.level_path = path.split("_")
        self.level_path.pop()
        self.level_path = '_'.join(self.level_path)
        print(self.level_path)
        with open(path,'r') as infile:
            for line in infile.readlines():
                line = line.strip()
                args = line.split('|')
                for k in range(len(args)):
                    try:
                        args[k] = int(args[k])
                    except:
                        raise TypeError(f"Error in {path}.\nLine: {line}\nArgument: {args[k]}\nLevel arguments must be of type int")
                
                self.contents.append(args)
        
        self.nexttimer = self.contents[0][4]

    def loadnextlevel(self):
        self.contents = []
        self.level_counter += 1
        with open(f"{self.level_path}_{self.level_counter}",'r') as infile:
            for line in infile.readlines():
                line = line.strip()
                args = line.split('|')
                for k in range(len(args)):
                    try:
                        args[k] = int(args[k])
                    except:
                        raise TypeError(f"Error in {self.level_path}_{self.level_counter}\nLine: {line}\nArgument: {args[k]}\nLevel arguments must be of type int")
                
                self.contents.append(args)
        self.nexttimer = self.contents[0][4]
        

class boss:
    x = 0
    y = 0
    size = 0
    active = True
    speed = 0

    sprite = picture.Picture("assets/boss/boss.png")
    sprite_alternate = picture.Picture("assets/boss/boss_alternate.png")
    sprite_state = 1
    sprite_timer = 10

    def __init__(self,x,y,health):
        self.x = x
        self.y = y
        self.size = 256
        self.active = True
        self.health = health

        self.sprite = picture.Picture("assets/boss/boss.png")
        self.sprite_alternate = picture.Picture("assets/boss/boss_alternate.png")
        self.sprite_state = 1
        self.sprite_timer = 10

    def update(self):
        randomaction = random.randint(1,5)
        
        if self.health <=0:
            self.active = False
            randomaction = 0
        
        match randomaction:
            case 1: #move
                pass
            case 2: #attack
                pass
            case 3: #spawn minion
                pass
            case 4: #do nothing
                pass
            case 5: #do nothing
                pass
        
        if self.sprite_timer <= 0:
            match self.sprite_state:
                case 1: self.sprite_state = 2
                case 2: self.sprite_state = 1
            self.sprite_timer = 10
        else:
            self.sprite_timer -= 1
        
        match self.sprite_state:
            case 1:
                stddraw.picture(self.sprite,self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,self.size/stddraw._canvasWidth,self.size/stddraw._canvasHeight)
            case 2:
                stddraw.picture(self.sprite_alternate,self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,self.size/stddraw._canvasWidth,self.size/stddraw._canvasHeight)


class enemy:
    x = 0
    y = 0
    size = 0
    active = True
    speed = 0

    sprite = picture.Picture("assets/enemy/Enemy.png")
    sprite_alternate = picture.Picture("assets/enemy/Enemy_alternate1.png")
    sprite_state = 1
    sprite_timer = 10

    def __init__(self,x,y,health):
        self.x = x
        self.y = y
        self.size = 16
        self.active = True
        self.speed = 40
        self.health = health

        self.sprite = picture.Picture("assets/enemy/Enemy.png")
        self.sprite_alternate = picture.Picture("assets/enemy/Enemy_alternate1.png")
        self.sprite_state = 1
        self.sprite_timer = 10
    
    def update(self):
        rand1 = random.randint(1,5)
        if self.health <= 0:
            self.active = False
            rand1 = 0
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
        
        self.draw()

    def draw(self):
        
        
        match self.sprite_state:
            case 1: stddraw.picture(self.sprite,self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,self.size*2/stddraw._canvasWidth,self.size*2/stddraw._canvasWidth)
            case 2: stddraw.picture(self.sprite_alternate,self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,self.size*2/stddraw._canvasWidth,self.size*2/stddraw._canvasWidth)

        if self.sprite_timer <= 0:
            match self.sprite_state:
                case 1: self.sprite_state = 2
                case 2: self.sprite_state = 1
            self.sprite_timer = 10
        else:
            self.sprite_timer -= 1



class player:
    x = 0
    y = 0
    health = 10
    score = 0
    invincibility_timer = 0

    def __init__(self):
        self.health = 10
        self.score = 0
        self.x = 32
        self.y = 32
        self.healthgained = False

        self.sprite = picture.Picture("assets/player/player.png")
        self.sprite_alternate1 = picture.Picture("assets/player/player_alternate1.png")
        self.sprite_hurt = picture.Picture("assets/player/player_hurt.png")
        self.spritestate = 1
        self.spritetimer = 10

    
    def draw(self):
        match self.spritestate:
            case 1: stddraw.picture(self.sprite,self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,0.04,0.08) # normal
            case 2: stddraw.picture(self.sprite_alternate1,self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,0.04,0.08) # alternate1
            case 3: stddraw.picture(self.sprite_hurt,self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,0.04,0.08) # hurt
        
        if self.spritetimer <= 0: #every nth frame switch states
            match self.spritestate:
                case 1: self.spritestate = 2 # alternate1
                case 2: self.spritestate = 1 # alternate1
            self.spritetimer = 10
        else:
            self.spritetimer-= 1
        
    
    def update(self):
        if self.invincibility_timer > 0:
            self.invincibility_timer -= 1

        if self.invincibility_timer == 0 or self.invincibility_timer % 3 != 0:
            self.draw()
        else:
            temp = self.spritestate
            self.spritestate = 3
            self.draw()
            self.spritestate = temp
    
    def move(self,x,y):
        
        self.x += x 
        self.y += y
        if self.x <16:
            self.x = 16
        if self.x > 784:
            self.x = 784
        if self.y <20:
            self.y = 20
        if self.y > 768:
            self.y = 768

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

        self.sprite = picture.Picture("assets/player/bullet_player.png")
        self.sprite_alternate1 = picture.Picture("assets/player/bullet_player_alternate1.png")
        self.sprite_state = 1
        self.sprite_timer = 5

    def update(self):
        if (self.x >= stddraw._canvasWidth or self.x <= 0) or (self.y >= stddraw._canvasHeight or self.y <= 0):
            self.active = False
        self.x += self.vel[0]
        self.y += self.vel[1]
        self.draw()
    
    def draw(self):
        match self.sprite_state:
            case 1: stddraw.picture(self.sprite,self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,0.04,0.04)
            case 2: stddraw.picture(self.sprite_alternate1,self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,0.04,0.04)

        if self.sprite_timer <= 0:
            match self.sprite_state:
                case 1: self.sprite_state = 2
                case 2: self.sprite_state = 1
            self.sprite_timer = 1
        else:
            self.sprite_timer -= 1

def mainloop():

    plr = player()
    bullets = []
    counter = 0
    enemies = []
    boss_arr = []
    gameactive = True
    endlessmode = False
    endless_enemycooldown = 10

    lvl = level()
    lvl.loadlevelfromfile("levels/default/level_1")

    stddraw.setPenColor(stddraw.LIGHT_GRAY)

    bawss = boss(400,400,10)
    

    while gameactive == True:
        

        
        stddraw.clear(stddraw.GRAY)
        
        stddraw.picture(lvl.background,0.5,0.5,1,1)

        
        bawss.update()

        if plr.health <= 0:
            gameactive = False
            break
        if stddraw.hasNextKeyTyped():
            match stddraw.nextKeyTyped():
                case 'a': plr.move(-32,0)
                case 'd': plr.move(32,0)
                case 'w': plr.move(0,32)
                case 's': plr.move(0,-32)
                case ' ': bullets.append(bullet(plr.x,plr.y,0,64))
                case '\x1b': menus.pause_menu()
                case 'p': enemies.append(enemy(random.randrange(16,784,16),784,2))
                

        plr.update()
        counter = 0
        counter2 = 0
        while counter < len(bullets):
            
            counter2 = 0
            while counter2 < len(enemies): #Checks every enemy for collision.
                if (bullets[counter].x >= enemies[counter2].x-enemies[counter2].size*2 and bullets[counter].x <= enemies[counter2].x+enemies[counter2].size*2) and (bullets[counter].y >= enemies[counter2].y-enemies[counter2].size*2 and bullets[counter].y <= enemies[counter2].y+enemies[counter2].size*2) and bullets[counter].active == True:
                    enemies[counter2].health -= 1
                    bullets[counter].active == False #effectively deletes current bullet
                    if enemies[counter2].health <= 0:
                        plr.score+=1
                        plr.healthgained = False
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
        
        lvlarray = lvl.update()

        match lvlarray[0]: #actions for the level's state/events
            case 0: pass    # level is empty    #TODO-> add end screen if it happens
            case 1:         # spawn enemy
                enemies.append(enemy(lvlarray[1]/stddraw._canvasWidth,lvlarray[2]/stddraw._canvasHeight,lvlarray[3]))
            case 2:         # spawn enemy with random X
                enemies.append(enemy(random.randrange(16,784,32)/stddraw._canvasWidth,lvlarray[2]/stddraw._canvasHeight,lvlarray[3]))
            case 3:         # spawn boss
                pass
            case 4:         # spawn boss with random X
                pass
            case 5: pass    # set background to the boss's background
            case 6: pass    # set background to normal
            case 7:         # set game to endless mode
                if endlessmode == False:
                    endlessmode = True
            case 8: pass    # load next level
            case 9: pass    # wait until screen is empty (all enemies are killed)
            case 100: pass  # indicates that level is waiting until screen is empty/ counter == 0

        if endlessmode == True:     #endless mode logic

            if endless_enemycooldown <= 0:
                enemies.append(enemy(random.randrange(16,784,16),768,1))
                endless_enemycooldown = random.randrange(1,100)
            else:
                endless_enemycooldown -= 1
            
            if plr.score % 10 == 0 and plr.score > 0 and plr.healthgained == False:
                plr.health+=1
                plr.healthgained = True


        stddraw.text(0.9,0.97,f"SCORE: {plr.score} ")
        stddraw.text(0.9,0.95,f"HEALTH: {plr.health}")
        stddraw.show(50)

