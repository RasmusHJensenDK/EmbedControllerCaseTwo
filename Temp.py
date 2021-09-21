import threading
import Device as dvc
import grovepi as gpi

class Temperature():
    _Device = dvc.Device(0,"NaN",0,"OFF")
    _Temp = 0
    def __init__(self, device):
        self._Device = device
    def run(self):
        [temp, hum] = gpi.dht(self._Device.get_ConnectorPin(), 0)
        if self.room._ID == 1:
            if temp > 23:
                self._Temp = temp
                return "TEMP IS TOO HIGH IN : " + str(self._Device.get_Room().get_building()) + " Celcius : " + str(self._Temp)
            else:
                return 0