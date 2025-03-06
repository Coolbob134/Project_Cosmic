import stddraw,time



def start_menu():
    
    
    while stddraw.hasNextKeyTyped() == False:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(50)
        
        stddraw.text(0.5,0.9,"SPACE PILLAGERS")
        stddraw.setFontSize(20)
        stddraw.text(0.5,0.8,"Press any key to start")
        stddraw.setFontSize(15)
        stddraw.text(0.5,0.75,"Press H for help")
        stddraw.setFontSize(20)
        stddraw.show(100)
    #\x1b -> ESC
    if stddraw.nextKeyTyped() == 'h':
        help_menu()
    
    

def help_menu():
    while 1==1:
        stddraw.clear(stddraw.GRAY)
        stddraw.setFontSize(40)

        stddraw.text(0.5,0.9,"HELP MENU")
        stddraw.setFontSize(15)
        stddraw.text(0.5,0.8,"Press ESC to return")
        stddraw.setFontSize(15)
        stddraw.text(0.5,0.75,"Press H for help")
        stddraw.setFontSize(20)
        stddraw.show(100)
        if stddraw.hasNextKeyTyped():
            match stddraw.nextKeyTyped():
                case '\x1b': break

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