import stdio, sys, random, picture, stddraw

import menus,singleplayer

def main():
    stddraw.setCanvasSize(800,800)
    
    menus.start_menu()
    
    singleplayer.mainloop()
    
    menus.inputTest()


if __name__ == "__main__" : main()