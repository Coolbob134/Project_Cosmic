import stddraw, random, math
from classes import *
import menus
import audio


#--------------------------------------------
# written by Alexander, Cameron and Ann
#--------------------------------------------
def mainloop(mode,lvlpath = "levels/default/level_1"):

    plr = player()
    bullets = []
    bulletdelay = 10
    counter = 0
    enemies = []
    boss_arr = []
    boss_bullets = []

    gameactive = True
    endlessmode = False
    endless_enemycooldown = 10
    enemy_state = 0
    enemy_state_cooldown = 5

    bullet_lookuptbl = {} #lookup table for bullet x and y velocity based on player's rotation (in degrees)
    bullet_speed = 32 #const for bullets speed

    for k in range(0,190,5):
        bullet_lookuptbl[k] = [bullet_speed*math.cos(math.radians(k)),bullet_speed*math.sin(math.radians(k))]
        


    lvl = level()
    match mode:
        case 1:
            lvl.loadlevelfromfile("levels/default/level_1")
        case 2:
            lvl.loadlevelfromfile(lvlpath)


    stddraw.setPenColor(stddraw.LIGHT_GRAY)

    

    while gameactive == True:
        

        
        stddraw.clear(stddraw.GRAY)
        
        stddraw.picture(lvl.background,0.5,0.5,1,1)

        
        

        if plr.health <= 0:
            audio.gameover()
            gameactive = False
            if plr.score >= lvl.high_score:
                    if lvl.high_score != -1:
                        with open(f"{lvl.level_path}_1","r") as infile:
                            lines = infile.readlines()
                        lines[0] = f"42|{plr.score}|0|0|0\n"
                        with open(f"{lvl.level_path}_1","w") as outfile:
                            outfile.seek(0)
                            outfile.writelines(lines)
                        lvl.high_score = plr.score
                    return [1,plr.score,plr.score]
            else:
                return [1,plr.score,lvl.high_score] #dies and ends game, returning scores

        if stddraw.hasNextKeyTyped():
            match stddraw.nextKeyTyped():
                case 'a':   # move left
                    if plr.move_state == 2:
                        plr.move_state = 4 # move faster
                    else:
                        if plr.move_state == 3:
                            plr.move_state = 1  # move slower to the right
                        else:
                            plr.move_state = 2
                case 'd':   # move right
                    if plr.move_state == 1:
                        plr.move_state = 3 # move faster
                    else:
                        if plr.move_state == 4:
                            plr.move_state = 2  #move slower to the left
                        else:
                            plr.move_state = 1
        
                case 's': plr.move_state = 0 # stop moving
                case 'q': plr.angle_move_state = 1
                case 'e': plr.angle_move_state = 2
                case 'w': plr.angle_move_state = 0
                case ' ': 
                    if bulletdelay <= 0:
                        audio.shoot_sound()
                        bullets.append(bullet(plr.x,plr.y,bullet_lookuptbl[plr.angle]))
                        bulletdelay = 10
                case '\x1b': 
                    if menus.pause_menu() == -1:
                        return [-1,0,0]
                    
                
        bulletdelay -= 1
        plr.update()
        counter = 0
        counter2 = 0

        while counter < len(bullets): #collision for bullets
            
            counter2 = 0
            while counter2 < len(enemies): #Checks every enemy for collision.
                if (bullets[counter].x >= enemies[counter2].x-(enemies[counter2].size)-16 and bullets[counter].x <= enemies[counter2].x+(enemies[counter2].size)+16) and (bullets[counter].y >= enemies[counter2].y-enemies[counter2].size and bullets[counter].y <= enemies[counter2].y+enemies[counter2].size) and bullets[counter].active == True:
                    enemies[counter2].health -= 1
                    
                    bullets[counter].active = False #effectively deletes current bullet
                    if enemies[counter2].health <= 0:
                        plr.score+=1
                        plr.healthgained = False
                        enemies[counter2].active = False
                    break
                else:
                    counter2 += 1
            
            counter2 = 0

            while counter2 < len(boss_arr): # Check bosses for collision.
                if (bullets[counter].x >= boss_arr[counter2].x - boss_arr[counter2].size/2 and bullets[counter].x <= boss_arr[counter2].x + boss_arr[counter2].size/2) and (bullets[counter].y>= boss_arr[counter2].y - boss_arr[counter2].size/2 and bullets[counter].y <= boss_arr[counter2].y + boss_arr[counter2].size/2) and bullets[counter].active == True:
                    boss_arr[counter2].health -= 1
                    bullets[counter].active = False
                    if boss_arr[counter2].health <= 0:
                        plr.score += 50
                        plr.healthgained = False
                        plr.health += 5
                        boss_arr[counter2].active = False
                        
                    break
                else:
                    counter2 += 1
            
            
            if bullets[counter].active == True:
                bullets[counter].update()
            if bullets[counter].active == False:
                del bullets[counter] #deletes off screen bullets or bullets that have hit an enemy
            else:
                counter+= 1

        counter = 0

        if enemy_state_cooldown <= 0:
            enemy_state_cooldown = 5
            if random.randint(1,2) == 1: # 50% chance of moving
                enemy_state =  random.randint(1,3)
            else:   
                enemy_state =  0 #idle
        else:
            enemy_state_cooldown -=1
            enemy_state = 0     #idle

        while counter < len(enemies): #collision for player and enemies
            
            
            if (enemies[counter].x >= plr.x - enemies[counter].size and enemies[counter].x <= plr.x + enemies[counter].size) and (enemies[counter].y >= plr.y - enemies[counter].size and enemies[counter].y <= plr.y + enemies[counter].size) and enemies[counter].active and player.invincibility_timer == 0:
                plr.invincibility_timer = 50
                plr.health -= 1
                enemies[counter].active = False
                
            
            if enemies[counter].update(enemy_state) == -1: #enemy hit bottom of the screen
                audio.gameover()
                if plr.score > lvl.high_score:
                    if lvl.high_score != -1:
                        with open(f"{lvl.level_path}_1","r") as infile:
                            lines = infile.readlines()
                        lines[0] = f"42|{plr.score}|0|0|0\n"
                        with open(f"{lvl.level_path}_1","w") as outfile:
                            outfile.seek(0)
                            outfile.writelines(lines)
                        lvl.high_score = plr.score

                        return [1,plr.score,plr.score]
                else:
                    return [1,plr.score,lvl.high_score] #dies and ends game, returning scores
            if enemies[counter].active == False:
                del enemies[counter] #deletes enemies that are dead, or enemies that have somehow gotten off screen
            else:
                counter+= 1
        

        counter = 0
        while counter < len(boss_arr):

            boss_bullets = boss_arr[counter].update(boss_bullets,[plr.x,plr.y])

            if boss_arr[counter].active == False:
                del boss_arr[counter]
            else:
                counter += 1

        counter = 0
        while counter < len(boss_bullets): #bosses bullets update

            if (boss_bullets[counter].x >= plr.x - 32 and boss_bullets[counter].x <= plr.x + 32) and (boss_bullets[counter].y >= plr.y - 64 and boss_bullets[counter].y <= plr.y + 64) and plr.invincibility_timer <= 0:
                boss_bullets[counter].active = False
                plr.health -= 1
                plr.invincibility_timer = 50
            
            if boss_bullets[counter].active == True:
                boss_bullets[counter].update()
                counter += 1
            else:
                del boss_bullets[counter]



        if len(enemies) == 0: # no enemies remaining on screen
            lvl.isempty = True
        if len(boss_arr) == 0:
            if lvl.bossfightactive == True:
                lvl.event_counter += 1
                lvl.bossfightactive = False
        lvlarray = lvl.update()
        
        
        match lvlarray[0]:  #actions for the level's state/events
            case 0:         # level is empty[end of level]
                if plr.score >= lvl.high_score:
                    if lvl.high_score != -1:
                        with open(f"{lvl.level_path}_1","r") as infile:
                            lines = infile.readlines()
                        lines[0] = f"42|{plr.score}|0|0|0\n"
                        with open(f"{lvl.level_path}_1","w") as outfile:
                            outfile.seek(0)
                            outfile.writelines(lines)
                        lvl.high_score = plr.score
                    return [2,plr.score,plr.score]
                else:
                    return [2,plr.score,lvl.high_score]
            case 1:         # spawn enemy
                enemies.append(enemy(lvlarray[1],lvlarray[2],lvlarray[3]))
                lvl.isempty = False
            case 2:         # spawn enemy with random X
                enemies.append(enemy(random.randrange(16,784,32),lvlarray[2],lvlarray[3]))
                lvl.isempty = False
            case 3:         # spawn boss
                boss_arr.append(boss(lvlarray[1],lvlarray[2],lvlarray[3]))
            case 4:         # spawn boss with random X
                boss_arr.append(boss(random.randrange(0,800,64),lvlarray[2],lvlarray[3]))
                
            case 5:         # set background to the boss's background
                lvl.background = lvl.boss_background
            case 6:         # set background to normal
                lvl.background = lvl.normal_background
            case 7:         # set game to endless mode
                if endlessmode == False:
                    endlessmode = True
            case 8: pass    # load next level
            case 9: pass    # wait until screen is empty (all enemies are killed)
            case 42: pass   # high score event
            case 100: pass  # indicates that level is waiting until screen is empty/ counter != 0

        if endlessmode == True:     #endless mode logic

            if endless_enemycooldown <= 0:
                enemies.append(enemy(random.randrange(16,784,16),768,1))
                lvl.isempty = False
                endless_enemycooldown = random.randrange(1,20)
            else:
                endless_enemycooldown -= 1
            
            if plr.score % 10 == 0 and plr.score > 0 and plr.healthgained == False:
                plr.health+=1
                plr.healthgained = True


        stddraw.text(0.9,0.97,f"SCORE: {plr.score} ")
        stddraw.text(0.9,0.95,f"HEALTH: {plr.health}")
        stddraw.text(0.9,0.93,f"LEVEL: {lvl.level_name}")
        stddraw.show(50)

