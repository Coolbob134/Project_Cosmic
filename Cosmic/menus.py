import stddraw,time


from buttons import btn
from singleplayer import mainloop

def start_menu():
    
    buttonnums = [[0.5,0.7,0.04,0.12],[0.5,0.6,0.04,0.12],[0.5,0.5,0.04,0.12],[0.5,0.4,0.04,0.12]]
    button = [btn(0.5,0.7,0.04,0.12,"PLAY"),btn(0.5,0.6,0.04,0.12,"CUSTOM LEVEL"),btn(0.5,0.5,0.04,0.12,"HELP"),btn(0.5,0.4,0.04,0.12,"EXIT")]
    selectedbutton = -1



    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(50)
        
        stddraw.text(0.5,0.9,"PLACEHOLDER_NAME") #TODO get name
        stddraw.setFontSize(20)
        for k in range(len(button)):
            button[k].draw()

        

        if stddraw.mousePressed(): #check if any menu buttons are pressed
            selectedbutton = -1
            clickx = stddraw.mouseX()
            clicky = stddraw.mouseY()
            for k in range(len(buttonnums)):
                if (clickx >= buttonnums[k][0] - buttonnums[k][3] and clickx <= buttonnums[k][0] + buttonnums[k][3]) and (clicky >= buttonnums[k][1] - buttonnums[k][2] and clicky <= buttonnums[k][1] + buttonnums[k][2]):
                    selectedbutton = k
                    break
            
        match selectedbutton:
            case 0:
                endstate = mainloop(1)
                stddraw.setPenColor(stddraw.BLACK)
                match endstate[0]:
                    case 1:
                        match end_menu(endstate):
                            case 1:
                                selectedbutton = 0 #play again
                            case 2:
                                selectedbutton = -1
                        
                    case 2:
                        match end_menu(endstate,won=True):
                            case 1:
                                selectedbutton = 0 #play again
                            case 2:
                                selectedbutton = -1
                    case -1:
                        selectedbutton = -1
            case 1:
                selectedbutton = -1
                lvlpath = customlvlmenu()
                if lvlpath != -1:
                    
                    endstate = mainloop(2,lvlpath=lvlpath)
                    match endstate[0]:
                        case 1:
                            match end_menu(endstate):
                                case 1:
                                    selectedbutton = 1 #play again
                                case 2:
                                    selectedbutton = -1
                        case 2:
                            match end_menu(endstate, won=True):
                                case 1:
                                    selectedbutton = 1 #play again
                                case 2:
                                    selectedbutton = -1
                        case -1:
                            selectedbutton = -1
                stddraw.setPenColor(stddraw.BLACK)
            case 2:
                selectedbutton = -1
                help_menu()
            case 3:
                
                exit()
    
        stddraw.show(100)
                    


    #\x1b -> ESC
        # if stddraw.hasNextKeyTyped():
        #         match stddraw.nextKeyTyped():
        #             case ' ': break
        #             case 'h': help_menu()
        
def end_menu(argarray = [0,0,0], won = False):
    
    restartTimer = 100 #10 seconds
    
    buttonnums = [[0.5,0.5,0.04,0.12],[0.5,0.4,0.04,0.12],[0.7,0.5,0.04,0.04]]
    button = [btn(0.5,0.5,0.04,0.12,f"PLAY AGAIN [{restartTimer}]"),btn(0.5,0.4,0.04,0.12,"MAIN MENU"),btn(0.675,0.5,0.04,0.04,"X")]
    selectedbutton = -1

    score = argarray[1]
    high_score = argarray[2]


    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(50)
        if won == True:
            stddraw.text(0.5,0.9,"YOU WON!")
        else:
            stddraw.text(0.5,0.9,"GAME OVER")
        stddraw.setFontSize(30)
        stddraw.text(0.5,0.6,f"SCORE: {score}")
        stddraw.text(0.5,0.63,f"HIGH SCORE: {high_score}")
        stddraw.setFontSize(20)

        if restartTimer <= 0 and restartTimer != -10:
            return 1 # Play again
        else:
            if restartTimer != -10: # if restart timer has not been cancelled
                restartTimer -= 1
        if restartTimer != -10:
            button[0].text = f"PLAY AGAIN [{restartTimer/10}]"
        else:
            button[0].text = f"PLAY AGAIN"
            if len(button) == 3:
                del button[2]
                del buttonnums[2]

        for k in range(len(button)):
            button[k].draw()

        stddraw.show(100)

        if stddraw.mousePressed(): #check if any menu buttons are pressed
            selectedbutton = -1
            clickx = stddraw.mouseX()
            clicky = stddraw.mouseY()
            for k in range(len(buttonnums)):
                if (clickx >= buttonnums[k][0] - buttonnums[k][3] and clickx <= buttonnums[k][0] + buttonnums[k][3]) and (clicky >= buttonnums[k][1] - buttonnums[k][2] and clicky <= buttonnums[k][1] + buttonnums[k][2]):
                    selectedbutton = k
                    break
            
            match selectedbutton:
                case 0:
                    return 1    #play again
                case 1:
                    return 2 #return to main menu
                case 2: #cancel play again
                    restartTimer = -10
                    


def help_menu():
    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(40)

        stddraw.text(0.5,0.9,"HELP MENU")
        stddraw.setFontSize(15)
        stddraw.text(0.5,0.8,"Press ESC to return")
        stddraw.setFontSize(15)
        stddraw.text(0.5,0.77,"Press K for keybindings")
        stddraw.setFontSize(20)
        stddraw.text(0.5,0.6,"You must destroy the sooty enemies by shooting them")
        stddraw.text(0.5,0.57,"When an enemy hits the bottom of the screen or your health")
        stddraw.text(0.5,0.54,"drops to 0, the game ends.")
        stddraw.text(0.5,0.51,"Upon hitting an enemy, its health is reduced by 1.")
        stddraw.text(0.5,0.48,"When you kill an enemy, your score increases by 1.")
        stddraw.text(0.5,0.45,"(In endless mode) Every 10 score, you gain 1 health.")
        stddraw.text(0.5,0.42,"To enter endless mode, select CUSTOM LEVEL & enter \"endless_1\".")
        stddraw.text(0.5,0.39,"Double tapping \"a\" or \"d\" will make you move faster.")
        stddraw.text(0.5,0.36,"Getting hit by an enemy will reduce your health.")
        stddraw.text(0.5,0.33,"You will gain a short period of invincibility when you're hit.")
        stddraw.text(0.5,0.30,"(For advanced users) To create a custom level, read \"levels.md\".")
        stddraw.text(0.5,0.27,"To play a custom level, enter the level's name in the CUSTOM LEVEL tab.")


        stddraw.show(100)
        if stddraw.hasNextKeyTyped():
            match stddraw.nextKeyTyped():
                case '\x1b': break
                case 'k': keybindings()

def pause_menu():
    buttonnums = [[0.5,0.6,0.04,0.12],[0.5,0.5,0.04,0.12],[0.5,0.4,0.04,0.12],[0.5,0.3,0.04,0.12]]
    button = [btn(0.5,0.6,0.04,0.12,"RESUME"),btn(0.5,0.5,0.04,0.12,"HELP MENU"),btn(0.5,0.4,0.04,0.12,"MAIN MENU")]
    stddraw.setPenColor(stddraw.BLACK)
    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(40)

        stddraw.text(0.5,0.9,"GAME PAUSED")
        stddraw.setFontSize(20)
        stddraw.text(0.5,0.8,"Press ESC to resume")
        stddraw.setFontSize(20)
        for k in range(len(button)):
            button[k].draw()
        stddraw.show(100)
        if stddraw.hasNextKeyTyped():
            match stddraw.nextKeyTyped():
                case '\x1b':
                    stddraw.setPenColor(stddraw.LIGHT_GRAY)
                    break
        
        if stddraw.mousePressed(): #check if any menu buttons are pressed
            selectedbutton = -1
            clickx = stddraw.mouseX()
            clicky = stddraw.mouseY()
            for k in range(len(buttonnums)):
                if (clickx >= buttonnums[k][0] - buttonnums[k][3] and clickx <= buttonnums[k][0] + buttonnums[k][3]) and (clicky >= buttonnums[k][1] - buttonnums[k][2] and clicky <= buttonnums[k][1] + buttonnums[k][2]):
                    selectedbutton = k
                    break
            
            match selectedbutton:
                case 0:
                    break
                case 1:
                    help_menu()
                case 2:
                    return -1

    stddraw.clear(stddraw.GRAY)

def keybindings():
    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(40)

        stddraw.text(0.5,0.9,"KEYBINDINGS")
        stddraw.setFontSize(20)
        stddraw.text(0.5,0.85,"Press ESC to return")
        stddraw.setFontSize(20)
        stddraw.text(0.45,0.7,"STOP AIM")
        stddraw.text(0.55,0.7,"w")
        stddraw.text(0.45,0.675,"STOP MOVE")
        stddraw.text(0.55,0.675,"s")
        stddraw.text(0.45,0.65,"LEFT")
        stddraw.text(0.55,0.65,"a")
        stddraw.text(0.45,0.625,"RIGHT")
        stddraw.text(0.55,0.625,"d")
        stddraw.text(0.45,0.6,"FIRE")
        stddraw.text(0.55,0.6,"space")
        stddraw.text(0.45,0.575,"PAUSE")
        stddraw.text(0.55,0.575,"esc")
        stddraw.text(0.45,0.55,"AIM LEFT")
        stddraw.text(0.55,0.55,"q")
        stddraw.text(0.45,0.525,"AIM RIGHT")
        stddraw.text(0.55,0.525,"e")
        stddraw.text(0.45,0.5,"STOP AIM")
        stddraw.text(0.55,0.5,"w")
        
        stddraw.setFontSize(20)
        stddraw.show(100)
        if stddraw.hasNextKeyTyped():
            
            match stddraw.nextKeyTyped():
                case '\x1b':break

def customlvlmenu():
    inputmode = True
    teststr = '_'
    nextkey = ''
    buttonnums = [[0.5,0.5,0.04,0.12],[0.5,0.4,0.04,0.12]]
    button = [btn(0.5,0.5,0.04,0.12,"SUBMIT"),btn(0.5,0.4,0.04,0.12,"BACK")]

    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(40)

        stddraw.text(0.5,0.9,"ENTER LEVEL NAME")
        stddraw.setFontSize(30)
        stddraw.text(0.5,0.8,f"{teststr}")
        stddraw.setFontSize(20)
        for k in range(len(button)):
            button[k].draw()
        stddraw.show(100)

        if stddraw.mousePressed(): #check if any menu buttons are pressed
                    selectedbutton = -1
                    clickx = stddraw.mouseX()
                    clicky = stddraw.mouseY()
                    for k in range(len(buttonnums)):
                        if (clickx >= buttonnums[k][0] - buttonnums[k][3] and clickx <= buttonnums[k][0] + buttonnums[k][3]) and (clicky >= buttonnums[k][1] - buttonnums[k][2] and clicky <= buttonnums[k][1] + buttonnums[k][2]):
                            selectedbutton = k
                            break
                    
                    match selectedbutton:
                        case 0:
                            
                            if inputmode == False: return f"levels/user/{teststr}"
                            else: return f"levels/user/{teststr[:-1]}"
                        case 1:
                            return -1


        if stddraw.hasNextKeyTyped():
            nextkey = stddraw.nextKeyTyped()
            if inputmode:
                match nextkey:
                    case '\x1b':teststr = teststr[:-1];inputmode = False
                    case '\x08':teststr = teststr[:-2]+'_'
                    case '\r':teststr = teststr[:-1];inputmode = False
                    case '\t':teststr = teststr[:-1];inputmode = False
                    case _: teststr = teststr[:-1]+nextkey+'_'
            else:
                
                match nextkey:
                    case '\r': return f"levels/user/{teststr}"

def inputTest(): #TODO remove func
    inputmode = False
    teststr = ''
    nextkey = ''
    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(40)

        stddraw.text(0.5,0.9,"ENTER LEVEL NAME")
        stddraw.setFontSize(30)
        stddraw.text(0.5,0.8,f"{teststr}")
        stddraw.show(10)
        if stddraw.hasNextKeyTyped():
            nextkey = stddraw.nextKeyTyped()
            if inputmode:
                
                match nextkey:
                    case '\x1b':teststr = teststr[:-1];inputmode = False
                    case '\x08':teststr = teststr[:-2]+'_'
                    case '\r':teststr = teststr[:-1];inputmode = False
                    case '\t':teststr = teststr[:-1];inputmode = False
                    case _: teststr = teststr[:-1]+nextkey+'_'
                
                
            else:
                match nextkey:
                    case '\x1b':break
                    case 'h': help_menu()
                    case '\r': inputmode = True;teststr += '_'
