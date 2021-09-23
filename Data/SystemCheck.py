import threading
import time
import grovepi as gpi
from Measurement import Light as li
from Measurement import Sound as sd
from Measurement import Temp as tp
import grove_rgb_lcd as grl
import Service as svc

def lcdMessage(message):
    grl.setText(message)

class WebCheck(threading.Thread):
    _sqlDevice = []
    def __init__(self, threadID, name, sqlDevice):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self._sqlDevice = sqlDevice
    def run(self):
        while True:
            time.sleep(1)
            for device in self._sqlDevice:
                if device[2] == "Light":
                    devLight = li.Light(device)
                    measuredLight = devLight.get_light()
                    if measuredLight < 10:
                        lcdMessage("Tænder \n for lyset")
                if self._sqlDevice[2] == "Sound":
                    devSound = sd.SoundCheck(device)
                    measuredSound = devSound.get_sound()
                    if measuredSound > 600:
                        lcdMessage("WARNING \n SOUND TO HIGH")
                if self._sqlDevice[2] == "Temp":
                    devTemp = tp.Temperature(device)
                    measuredTemp = devTemp.get_temp()
                    if measuredTemp > 23:
                        svc.OpenWindows(device[3])
                        lcdMessage("WARNING \n TEMP TO HIGH")

class SystemCheck(threading.Thread):
    _Devices = []
    def __init__(self, threadID, name, Devices):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self._Devices = Devices
    def run(self):
        while True:
            time.sleep(1)
            for i in self._Devices:
                if i._Type == "Light":
                    if i._State == "OFF":
                        break
                    else:
                        MeasuredLight = gpi.analogRead(i.get_ConnectorPin())
                        if MeasuredLight < 10:
                            lcdMessage("Tænder lyset i bygning: " + str(i.get_Room().get_building()) + "C\n" + "I lokale: " + str(i.get_Room().get_number()))
                            print("Tænder lyset i bygning : " + str(i.get_Room().get_building()))
                            print("Tænder lyset i bygning : " + str(i.get_Room().get_number()))
                            input("Press a key to move on..")
                            return "Lyst er Tændt i rum " + str(i.get_Room().get_number())
                if i._Type == "Sound":
                    if i._State == "OFF":
                        break
                    else:
                        MeasuredSound = gpi.analogRead(i.get_ConnectorPin())
                        if MeasuredSound > 600:
                            grl.setRGB(255,0,0)
                            lcdMessage(" WARNING  SOUND" + "\n" + "Build:" + str(i.get_Room().get_building()) + " Room:"+ str(i.get_Room().get_number()))
                            print("WARNING - SOUND")
                            print("Above 600 in building: " + str(i.get_Room().get_building()))
                            print("Above 600 in room: " + str(i.get_Room().get_number()))
                            input("Press a key to move on..")
                            grl.setRGB(0,255,0)
                            grl.setText("Nothing to show")
                            return "Lyden er høj i rum " + str(i.get_Room().get_number())
                if i._Type == "Temp":
                    if i._State == "OFF":
                        break
                    else:
                        [temp,hum] = gpi.dht(i.get_ConnectorPin(),0)
                        if temp > 23:
                            grl.setRGB(255,0,0)
                            lcdMessage("  WARNING TEMP" + "\n" + "Build:" + str(i.get_Room().get_building()) + " Room:"+ str(i.get_Room().get_number()))
                            print("The temperature is too high in :")
                            print("Building : " + str(i.get_Room().get_building()))
                            print("Room : " + str(i.get_Room().get_number()))
                            print("Opening windows in 3..2..1..")
                            input("Press a key to disable warning")
                            grl.setRGB(0,255,0)
                            grl.setText("Nothing to show")
                            


