from Measurement import Device as dvc
#import grovepi as gpi

class SoundCheck():
    _Device = dvc.Device(0,"NaN",0,"OFF")
    _sqlDevice = []
    def __init__(self, sqlDevice, *device):
        self._Device = device
        self._sqlDevice = sqlDevice
    def run(self):
        while True:
            #sound_level = gpi.analogRead(self._Device.get_ConnectorPin())
            sound_level = 40
            print(str(sound_level))
            if sound_level > 600:
                return "WARNING SOUND " + str(sound_level)
            else:
                return "Sound is fine " + str(sound_level)
    def get_sound(self):
        # str(gpi.analogRead(self._sqlDevice[1]))
        return "40"