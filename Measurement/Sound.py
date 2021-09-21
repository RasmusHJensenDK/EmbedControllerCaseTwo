import threading
import Device as dvc
import grovepi as gpi

class SoundCheck():
    _Device = dvc.Device(0,"NaN",0,"OFF")
    def __init__(self, device):
        self._Device = device
    def run(self):
        while True:
            sound_level = gpi.analogRead(self._Device.get_ConnectorPin())
            print(str(sound_level))
            if sound_level > 600:
                return "WARNING SOUND " + str(sound_level)
            else:
                return "Sound is fine " + str(sound_level)