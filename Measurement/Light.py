from Measurement import Device as dvc
import grovepi as gpi

lys = 0

def set_lys(x):
    global lys
    lys = x
def get_lys():
    return lys

class Light():
    _Device = dvc.Device(0,"NaN",0,"OFF")
    _sqlDevice = []
    def __init__(self, sqlDevice, *device):
        self._Device = device
        self._sqlDevice = sqlDevice
    def run(self):
        set_lys(gpi.analogRead(self._Device.get_ConnectorPin()))
        if get_lys() > 10:
            return ("TÆNDT")
        if get_lys() < 10:
            return ("SLUKKET")
    def get_light(self, cp):
        print("LIGHT")
        print(str(gpi.analogRead(cp)))
        return str(gpi.analogRead(cp))
        #return "40"

def TaandLys():
    print("Tænder lyset")
