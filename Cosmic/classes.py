import stddraw, random, math, picture

class level:

    contents = []   # level contents loaded in from file
    level_type = 0  # The type of level
    nexttimer = 0   # Timer until next event
    level_counter  = 0
    background = 0
    high_score = -1
    

    def __init__(self):
        self.level_type = 0
        self.nexttimer = 0
        self.event_counter  = 0
        self.isempty = True
        self.waitempty = False
        self.bossfightactive = False
        self.level_path = ''
        self.level_counter = 1
        self.endlessmode = False

        self.background = picture.Picture("assets/backgrounds/normal_background.png")
        self.boss_background = picture.Picture("assets/backgrounds/boss_background.png")
        self.normal_background = picture.Picture("assets/backgrounds/normal_background.png")
        

    def update(self):
       
        match self.contents[self.event_counter][0]:
            case 3:                                                     #boss
                if self.bossfightactive == False:                    
                    self.bossfightactive = True
                    returnarr = self.contents[self.event_counter][:4] 
                    if self.contents[self.event_counter+1][0] == 3 or self.contents[self.event_counter+1][0] == 4:
                        self.event_counter += 1
                        self.bossfightactive = False

                    return returnarr
            case 4:                                                     #boss_x
                if self.bossfightactive == False:   
                    self.bossfightactive = True
                    if self.contents[self.event_counter+1][0] == 3 or self.contents[self.event_counter+1][0] == 4:
                        self.event_counter += 1
                        self.bossfightactive = False
                    return [4,0,0,0]
            case 5: self.background = self.boss_background              #boss_bg
            case 6: self.background = self.normal_background            #normal_bg
            case 7: 
                self.endlessmode = True
                return [7,0,0,0]                                    #endless mode
            case 8:                                                     #next_lvl
                self.loadnextlevel()
                self.event_counter = 0
                return [8,0,0,0]

            case 9:                                                     #wait_empty
                if self.isempty == False: self.waitempty = True
                else: self.waitempty = False
            case 42:
                returnarr = self.contents[self.event_counter][:4]
                self.high_score = returnarr[1]
                self.event_counter += 1
                return returnarr
                

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
        self.level_name = self.level_path.split("/")[-1] + f" {self.level_counter}"
        
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
        self.level_name = "".join(self.level_name.split(" ")[:-1]) + f" {self.level_counter}"
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
    state_timer = 10
    state = 0
    movedirection = 0
    phase = 1

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
        self.maxhealth = health

        self.sprite = picture.Picture("assets/boss/boss.png")
        self.sprite_alternate = picture.Picture("assets/boss/boss_alternate.png")
        self.sprite_state = 1
        self.sprite_timer = 10

    def update(self,bullets = [],playercoords = [0,0]):
        bulletarr = bullets
        randomaction = random.randint(0,2)

        if self.health <=0:
            self.active = False
            randomaction = 0
        
        if self.health <= self.maxhealth*0.5:
            self.phase = 2
        
        if self.state_timer <= 0:
            self.state = randomaction
            match randomaction:
                case 0: #idle
                    if self.phase == 1:
                        self.state_timer = 5
                    else: #in phase 2, the boss will attack instead of idling
                        try:
                            m = (self.y - playercoords[1])/(self.x - playercoords[0])
                        except:
                            m = (self.y - playercoords[1])/0.0000001
                        velx = math.sqrt(256/(1+m**2))
                        if playercoords[0]-self.x<0: velx = -velx
                        vely = velx*m
                        bulletarr.append(boss_bullet(self.x,self.y,[velx,vely]))
                        self.state_timer = 0
                case 1: #move
                    self.movedirection = random.randint(1,4)
                    if self.phase == 1:
                        self.state_timer = 10
                    else:
                        self.state_timer = 5
                case 2: #attack
                    if self.phase == 1:
                        bulletarr.append(boss_bullet(self.x,self.y,[-16,-16]))
                        bulletarr.append(boss_bullet(self.x,self.y,[16,16]))
                        bulletarr.append(boss_bullet(self.x,self.y,[-16,16]))
                        bulletarr.append(boss_bullet(self.x,self.y,[16,-16]))
                        bulletarr.append(boss_bullet(self.x,self.y,[-16,0]))
                        bulletarr.append(boss_bullet(self.x,self.y,[16,0]))
                        bulletarr.append(boss_bullet(self.x,self.y,[0,16]))
                        bulletarr.append(boss_bullet(self.x,self.y,[0,-16]))
                        self.state_timer = 1
                    else:
                        try:
                            m = (self.y - playercoords[1])/(self.x - playercoords[0])
                        except:
                            m = (self.y - playercoords[1])/0.0000001
                        velx = math.sqrt(256/(1+m**2))
                        if playercoords[0]-self.x<0: velx = -velx
                        vely = velx*m
                        bulletarr.append(boss_bullet(self.x,self.y,[velx,vely]))
                        self.state_timer = 0
        else:
            self.state_timer -= 1
            if self.state == 1: #moving
                if self.phase == 1:
                    match self.movedirection:
                        case 1: #right
                            self.x += 10
                        case 2: #left
                            self.x -= 10
                        case 3: #up
                            self.y += 10
                        case 4:
                            self.y -= 10
                else:
                    match self.movedirection:
                        case 1: #right
                            self.x += 20
                        case 2: #left
                            self.x -= 20
                        case 3: #up
                            self.y += 20
                        case 4:
                            self.y -= 20
        
        if self.x <= self.size/2:
            self.x = self.size/2
        if self.x >= stddraw._canvasWidth-self.size/2:
            self.x = stddraw._canvasWidth-self.size/2
        if self.y <= self.size/2:
            self.y = self.size/2
        if self.y >= stddraw._canvasHeight-self.size/2:
            self.y = stddraw._canvasHeight-self.size/2
            
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

        return bulletarr

class boss_bullet: 

    active = True
    
    sprite = picture.Picture("assets/boss/boss_bullet.png")

    def __init__(self,x,y,velocity):
        self.x = x
        self.y = y
        self.velx = velocity[0]
        self.vely = velocity[1]
    

    def update(self):
        
        self.x += self.velx
        self.y += self.vely

        if self.x >= stddraw._canvasWidth or self.x <= 0 or self.y >= stddraw._canvasHeight:
            self.active = False
        
        stddraw.picture(self.sprite,self.x/stddraw._canvasWidth,self.y/stddraw._canvasHeight,0.04,0.04)
        
        



        

class enemy: #TODO check whether random movement is ok [change lvl 1]
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
    
    def update(self,enemy_state = 0):

        match enemy_state:
            case 0: # idle
                pass
            case 1: # down
                self.y -= self.speed
            case 2: # left
                if self.x > self.speed:
                    self.x -= self.speed
            case 3: # right
                if self.x < stddraw._canvasWidth-self.speed:
                    self.x += self.speed
        if self.y <= 0:
            self.active = False
            return -1
        
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
    crosshair_lookup = {} #lookup table for the crosshair position

    def __init__(self):
        self.health = 10
        self.score = 0
        self.x = 32
        self.y = 32
        self.healthgained = False
        self.angle = 90
        self.move_state = 0
        self.angle_move_state = 0

        self.sprite = picture.Picture("assets/player/player.png")
        self.sprite_alternate1 = picture.Picture("assets/player/player_alternate1.png")
        self.sprite_hurt = picture.Picture("assets/player/player_hurt.png")
        self.crosshair_sprite = picture.Picture("assets/player/crosshair.png")
        self.spritestate = 1
        self.spritetimer = 10

        for k in range(0,190,5):
            self.crosshair_lookup[k] = [64*math.cos(math.radians(k)),64*math.sin(math.radians(k))]

    
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
        crosshair_offset = self.crosshair_lookup[self.angle]
        stddraw.picture(self.crosshair_sprite, (self.x+crosshair_offset[0])/stddraw._canvasWidth,(self.y+crosshair_offset[1])/stddraw._canvasHeight,0.04,0.04)
        
    
    def update(self):
        self.move()
        if self.invincibility_timer > 0:
            self.invincibility_timer -= 1

        if self.invincibility_timer == 0 or self.invincibility_timer % 3 != 0:
            self.draw()
        else:
            temp = self.spritestate
            self.spritestate = 3
            self.draw()
            self.spritestate = temp
    
    def move(self):
        
        match self.move_state:
            case 1:
                self.x += 8
            case 2:
                self.x -= 8
            case 3:
                self.x += 16
            case 4:
                self.x -= 16
        
        match self.angle_move_state:
            case 1:
                self.angle += 5
            case 2:
                self.angle -= 5
        
        if self.x <16:
            self.x = 16
            self.move_state = 1 # bounce back
        if self.x > 784:
            self.x = 784
            self.move_state = 2 # bounce back
        if self.angle < 0:
            self.angle = 0
            self.angle_move_state = 1
        if self.angle > 180:
            self.angle = 180
            self.angle_move_state = 2
        # if self.y <20:
        #     self.y = 20
        # if self.y > 768:
        #     self.y = 768

class bullet:
    x = 0
    y = 0
    vel = [0,0]
    active = True

    def __init__(self,x,y,velocity):
        self.x = x
        self.y = y
        self.vel = velocity
        self.active = True

        self.sprite = picture.Picture("assets/player/bullet_player.png")
        self.sprite_alternate1 = picture.Picture("assets/player/bullet_player_alternate1.png")
        self.sprite_state = 1
        self.sprite_timer = 3

        self.particles = []

    def update(self):
        if (self.x >= stddraw._canvasWidth or self.x <= 0) or (self.y >= stddraw._canvasHeight or self.y <= 0):
            self.active = False
        self.x += self.vel[0]
        self.y += self.vel[1]
        self.draw()
        self.particles.append(particle(self.x,self.y,1,[0,0]))
    
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

        tempcounter = len(self.particles)
        k = 0
        while k < tempcounter:
            self.particles[k].draw()
            if self.particles[k].counter <= 0:
                del self.particles[k]
                tempcounter-=1
            else:
                k+= 1

class particle:

    def __init__(self,x,y,type,vel):
        
        self.type = type
        self.counter = 3
        self.x = x
        self.y = y

    def draw(self):
        temp = stddraw._penColor
        tempradius = stddraw._penRadius
        self.counter -= 1
        match self.type:
            case 1: # bullet particle
                stddraw.setPenColor(stddraw.BLUE)
                stddraw.setPenRadius(0.004)
                stddraw.point((self.x+random.randrange(-16,16,1))/stddraw._canvasWidth,(self.y+random.randrange(-16,16,1))/stddraw._canvasHeight)
                stddraw.point((self.x+random.randrange(-16,16,1))/stddraw._canvasWidth,(self.y+random.randrange(-16,16,1))/stddraw._canvasHeight)
                stddraw.point((self.x+random.randrange(-16,16,1))/stddraw._canvasWidth,(self.y+random.randrange(-16,16,1))/stddraw._canvasHeight)
                stddraw.point((self.x+random.randrange(-16,16,1))/stddraw._canvasWidth,(self.y+random.randrange(-16,16,1))/stddraw._canvasHeight)
                stddraw.setPenColor(temp)
                stddraw.setPenRadius(tempradius)
