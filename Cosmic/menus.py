import stddraw,time

import leveleditor
from buttons import btn

def start_menu():
    
    buttonnums = [[0.5,0.6,0.04,0.12],[0.5,0.5,0.04,0.12],[0.5,0.4,0.04,0.12],[0.5,0.3,0.04,0.12]]
    button = [btn(0.5,0.6,0.04,0.12,"PLAY"),btn(0.5,0.5,0.04,0.12,"LEVEL EDITOR"),btn(0.5,0.4,0.04,0.12,"HELP"),btn(0.5,0.3,0.04,0.12,"EXIT")]



    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(50)
        
        stddraw.text(0.5,0.9,"PLACEHOLDER_NAME") #TODO get name
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
                    break
                case 1:
                    leveleditor.lvleditor_mainmenu()
                case 2:
                    help_menu()
                case 3:
                    exit()
                    


    #\x1b -> ESC
        # if stddraw.hasNextKeyTyped():
        #         match stddraw.nextKeyTyped():
        #             case ' ': break
        #             case 'h': help_menu()
        
    

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
        stddraw.show(100)
        if stddraw.hasNextKeyTyped():
            match stddraw.nextKeyTyped():
                case '\x1b': break
                case 'k': keybindings()

def pause_menu():
    stddraw.setPenColor(stddraw.BLACK)
    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(40)

        stddraw.text(0.5,0.9,"GAME PAUSED")
        stddraw.setFontSize(20)
        stddraw.text(0.5,0.8,"Press ESC to resume")
        stddraw.setFontSize(15)
        stddraw.text(0.5,0.75,"Press H for help")
        stddraw.setFontSize(20)
        stddraw.show(100)
        if stddraw.hasNextKeyTyped():
            match stddraw.nextKeyTyped():
                case '\x1b':
                    stddraw.setPenColor(stddraw.LIGHT_GRAY)
                    break
                case 'h': help_menu()

    stddraw.clear(stddraw.GRAY)

def keybindings():
    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(40)

        stddraw.text(0.5,0.9,"KEYBINDINGS")
        stddraw.setFontSize(20)
        stddraw.text(0.5,0.85,"Press ESC to return")
        stddraw.setFontSize(20)
        stddraw.text(0.45,0.7,"UP")
        stddraw.text(0.55,0.7,"w")
        stddraw.text(0.45,0.675,"DOWN")
        stddraw.text(0.55,0.675,"s")
        stddraw.text(0.45,0.65,"LEFT")
        stddraw.text(0.55,0.65,"a")
        stddraw.text(0.45,0.625,"RIGHT")
        stddraw.text(0.55,0.625,"d")
        stddraw.text(0.45,0.6,"FIRE")
        stddraw.text(0.55,0.6,"space")
        stddraw.text(0.45,0.575,"PAUSE")
        stddraw.text(0.55,0.575,"esc")
        stddraw.text(0.45,0.55,"SPAWN ENEMY")
        stddraw.text(0.55,0.55,"p")
        
        stddraw.setFontSize(20)
        stddraw.show(100)
        if stddraw.hasNextKeyTyped():
            
            match stddraw.nextKeyTyped():
                case '\x1b':break

def inputTest(): #TODO remove func
    inputmode = False
    teststr = ''
    nextkey = ''
    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(40)

        stddraw.text(0.5,0.9,"GAME PAUSED")
        stddraw.setFontSize(20)
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
