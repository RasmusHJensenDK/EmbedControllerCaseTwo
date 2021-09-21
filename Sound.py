import threading
import Device as dvc
import grovepi as gpi

sound = 0

def set_sound(x):
    global sound
    sound = x
def get_sound():
    return sound

class SoundCheck():
    _Device = dvc.Device(0,"NaN",0,"OFF")
    def __init__(self, device):
        self._Device = device
    def run(self):
        while True:
            sound_level = gpi.analogRead(self._Device.get_ConnectorPin())
            if sound_level > 600:
                return "WARNING SOUND"
            else:
                set_sound(sound_level)