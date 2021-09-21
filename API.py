import flask as fk
import threading
import Temp as temp
import Device as dvc
import SystemCheck as SC
import Room as rr

app = fk.Flask(__name__)
app.config["DEBUG"] = False

City_Ground_floor_South = rr.Room(1,1,1)
City_Ground_floor_Center = rr.Room(2,1,2)
City_Ground_floor_North = rr.Room(3,1,3)

City_Device_Ground_Floor_South_Temperature = dvc.Device(7, "Temp", City_Ground_floor_South, "ON")
City_Device_Ground_Floor_South_Light = dvc.Device(15, "Light", City_Ground_floor_South, "ON")
City_Device_Ground_Floor_South_Sound = dvc.Device(14, "Sound", City_Ground_floor_South, "ON")

_Devices = []
_Devices.append(City_Device_Ground_Floor_South_Temperature)
_Devices.append(City_Device_Ground_Floor_South_Light)
_Devices.append(City_Device_Ground_Floor_South_Sound)

systemtjek = SC.SystemCheck(2, "SystemCheck", _Devices)
systemtjek.start()

class APP(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    @app.route('/', methods=['GET'])
    def Home():
        return "<h1>TEST</h1>"

    @app.route('/Temperature/Room/<int:id>', methods=['GET'])
    def NotHome(id):
        for x in _Devices:
            if (str(x.get_Room().get_id()) == str(id)):
                if x._Type == "Temp":
                    output_temp = temp.Temperature(x)
                    return output_temp.run()

app.run()