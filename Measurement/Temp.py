import threading
from Measurement import Device as dvc
#import grovepi as gpi

class Temperature():
    _Device = dvc.Device(0,"NaN",0,"OFF")
    _VinduerAabent = False
    def __init__(self, device, VinduerAabent):
        self._Device = device
        self._VinduerAaben = VinduerAabent
    def run(self):
        #[temp, hum] = gpi.dht(self._Device.get_ConnectorPin(), 0)
        temp = 20
        print(str(temp))
        if self._Device.get_Room().get_id() == 1:
            if temp > 22:
                if self._VinduerAabent:
                    return "Temp is too high, but windows are open " + str(temp)
                return "TEMP IS TOO HIGH IN : " + str(self._Device.get_Room().get_building()) + " Celcius : " + str(temp)
            else:
                if self._VinduerAabent:
                    self._VinduerAabent = False
                    return "Closing windows as Temp is fine"
                else:
                    return "Temp is fine at : " + str(temp)
    def getVinduerState(self):
        return self._VinduerAabent