import threading
import Device as dvc
import grovepi as gpi

temperature = 0

def set_temp(x):
    global temperature
    temperature = x
def get_temp():
    return temperature

class Temperature():
    _Device = dvc.Device(0,"NaN",0,"OFF")
    def __init__(self, device):
        self._Device = device
    def run(self):
        [temp, hum] = gpi.dht(self._Device.get_ConnectorPin(), 0)
        if self.room._ID == 1:
            if temp > 23:
                set_temp(temp)
                #Throw warning
            if temp < 23: 
                set_temp(temp)
                #Temp is fine
        if self.room_ID == 2:
            if temp > 18:
                set_temp(temp)
                #Throw warning
            if temp < 18:
                set_temp(temp)
                #Temp is fine