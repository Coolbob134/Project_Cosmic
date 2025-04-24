import stdaudio
from threading import Thread, Event

#--------------------------------------------
#written by Ann
#--------------------------------------------

def _shoot_sound():
    stdaudio.playFile("assets/sounds/retro-laser")


def shoot_sound():
    Thread(target=_shoot_sound,daemon=True).start()

def _gameover():
    stdaudio.playFile("assets/sounds/game-over")

def gameover():
    Thread(target=_gameover,daemon=True).start()