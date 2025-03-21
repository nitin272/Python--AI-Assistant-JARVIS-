import os
import eel
from engine.feature import *
from engine.command import *
from engine.config import *
from engine.feature import *
eel.init("www")

def start():
    playAssistantSound()


    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html' , mode=None, host='localhost' , block=True)
