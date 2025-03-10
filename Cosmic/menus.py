import stddraw,time



def start_menu():
    
    
    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(50)
        
        stddraw.text(0.5,0.9,"SPACE PILLAGERS")
        stddraw.setFontSize(20)
        stddraw.text(0.5,0.8,"Press space to start")
        stddraw.setFontSize(15)
        stddraw.text(0.5,0.75,"Press H for help")
        stddraw.setFontSize(20)
        stddraw.show(100)
    #\x1b -> ESC
        if stddraw.hasNextKeyTyped():
                match stddraw.nextKeyTyped():
                    case ' ': break
                    case 'h': help_menu()
        
    

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
                case '\x1b':break
                case 'h': help_menu()

    stddraw.clear(stddraw.GRAY)

def keybindings():
    selected = [' ']*7
    selected[0] = '>'
    selectnum = 0 # [Current selected keybind, Previous]
    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(40)

        stddraw.text(0.5,0.9,"KEYBINDINGS")
        stddraw.setFontSize(20)
        stddraw.text(0.5,0.85,"Press ESC to return")
        stddraw.setFontSize(15)
        stddraw.text(0.5,0.825,"Use Q and E to navigate up and down")
        stddraw.setFontSize(20)
        stddraw.text(0.5,0.7,f"{selected[0]  }UP         w")
        stddraw.text(0.5,0.675,f"{selected[1]}DOWN      s")
        stddraw.text(0.5,0.65,f"{selected[2] }LEFT      a")
        stddraw.text(0.5,0.625,f"{selected[3]}RIGHT     d")
        stddraw.text(0.5,0.6,f"{selected[4]  }FIRE        space")
        stddraw.text(0.5,0.575,f"{selected[5]}PAUSE      esc")
        stddraw.text(0.5,0.55,f"{selected[6] }SPAWN ENEMY      p")
        
        stddraw.setFontSize(20)
        stddraw.show(100)
        if stddraw.hasNextKeyTyped():
            
            match stddraw.nextKeyTyped():
                case '\x1b':break
                case 'q':
                    if selectnum>0:
                        selected[selectnum] = ' '
                        selectnum-= 1
                        selected[selectnum] = '>'
                    else:
                        selected[selectnum] = ' '
                        selectnum = len(selected) -1
                        selected[selectnum] = '>'
                case 'e':
                    if selectnum<len(selected)-1:
                        selected[selectnum] = ' '
                        selectnum += 1
                        selected[selectnum] = '>'
                    else:
                        selected[selectnum] = ' '
                        selectnum = 0
                        selected[selectnum] = '>'
                case '\r':  pass  #TODO: add keybind switching (ENTER)

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
