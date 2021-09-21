import Room as rr
import Device as dvc
import SystemCheck as sc
import grove_rgb_lcd as grl
import time
import API as myApi

class main():
    grl.setRGB(150,150,150)
    grl.setText("Starting up..")

    _RoomIDToExamine = 0
    _RoomDevicesToExamine = []
    grl.setText("Awating input..\nHint: Keyboard")
    buildingInput = input("Drivhus ID? :")
    time.sleep(2)
    grl.setRGB(0,255,0)
    grl.setText("Nothing to show")
    
    for x in _DATA._Rooms:
        if str(x.get_id()) == str(buildingInput):
            _RoomIDToExamine = x.get_id()

    for x in _DATA._LightDevices:
        if (str(x.get_Room().get_id()) == str(_RoomIDToExamine)):
            _RoomDevicesToExamine.append(x)
    for x in _DATA._SoundDevices:
        if (str(x.get_Room().get_id()) == str(_RoomIDToExamine)):
            _RoomDevicesToExamine.append(x)
    for x in _DATA._TempDevices:
        if (str(x.get_Room().get_id()) == str(_RoomIDToExamine)):
            _RoomDevicesToExamine.append(x)

    _SYSTEM = sc.SystemCheck(1, "MainThread", _RoomDevicesToExamine)
    _SYSTEM.start()
#    _API = myApi.APP(2, "APITread")
#    _API.start()

main()