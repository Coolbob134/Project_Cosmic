#WIP level editor
# currently not doing anything

import stddraw

from buttons import btn

def lvleditor_mainmenu():
    
    buttondims = [[0.5,0.6,0.04,0.12],[0.5,0.5,0.04,0.12],[0.5,0.4,0.04,0.12],[0.5,0.3,0.04,0.12]]
    button = [btn(0.5,0.6,0.04,0.12,"NEW"),btn(0.5,0.5,0.04,0.12,"LOAD"),btn(0.5,0.4,0.04,0.12,"HELP"),btn(0.5,0.3,0.04,0.12,"BACK")]

    while 1==1:

        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(30)
        
        stddraw.text(0.5,0.8,"LEVEL EDITOR")
        stddraw.setFontSize(20)
        
        for l in range(len(button)):
            button[l].draw()


        if stddraw.mousePressed():
            selectedbutton = -1
            clickx = stddraw.mouseX()
            clicky = stddraw.mouseY()
            for k in range(len(buttondims)):
                if (clickx >= buttondims[k][0] - buttondims[k][3] and clickx <= buttondims[k][0] + buttondims[k][3]) and (clicky >= buttondims[k][1] - buttondims[k][2] and clicky <= buttondims[k][1] + buttondims[k][2]):
                    selectedbutton = k
                    break
            
            match selectedbutton:
                case 0:
                    print("new level")
                case 1:
                    print("load level")
                case 2:
                    lvleditor_help()
                case 3:
                    break
            
        
        stddraw.show(100)

def lvleditor_help():

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
                case 'k': lvleditor_keybindings()


def lvleditor_keybindings():
    while 1==1:

        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(40)
        stddraw.text(0.5,0.9,"KEYBINDS")
        stddraw.setFontSize(15)
        stddraw.text(0.5,0.8,"Press ESC to return")
        stddraw.setFontSize(15)
        stddraw.setFontSize(20)
        stddraw.text(0.45,0.7,  f"ENEMY")
        stddraw.text(0.55,0.7,  f"e")
        stddraw.text(0.45,0.675,f"RANDOM ENEMY")
        stddraw.text(0.55,0.675,f"r")
        stddraw.text(0.45,0.65, f"ERASER")
        stddraw.text(0.55,0.65, f"del")
        stddraw.text(0.45,0.625,f"BOSS")
        stddraw.text(0.55,0.625,f"b")
        stddraw.text(0.45,0.6,  f"RANDOM BOSS")
        stddraw.text(0.55,0.6,  f"v")
        stddraw.text(0.45,0.575,f"HELP")
        stddraw.text(0.55,0.575,f"h")
        stddraw.text(0.45,0.55, f"MENU")
        stddraw.text(0.55,0.55, f"ESC")


        stddraw.setFontSize(20)
        stddraw.show(100)
        if stddraw.hasNextKeyTyped():
            match stddraw.nextKeyTyped():
                case '\x1b': break
