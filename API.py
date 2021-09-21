import flask as fk
import threading
import Temp as temp
import Sound as sd
import Device as dvc
import SystemCheck as SC
import Room as rr
import sqlite3

app = fk.Flask(__name__)
app.config["DEBUG"] = False

rooms = []
devices = []

con = sqlite3.connect('example.db')
with con:
    data = con.execute("SELECT * FROM ROOM")
    for row in data:
        print(row)
        rooms.append(row)
    data2 = con.execute("SELECT * FROM Device")
    for row in data2:
        print(row)
        devices.append(row)


@app.route('/', methods=['GET'])
def Home():
    return "<h1>Welcome to Rasmus Høholt Jensen RaspberrI Pi Proj | Embedded Controller H3</h1>"

@app.route('/Temperature/Room/<int:id>', methods=['GET'])
def Temp(id):
    for x in devices:
        for p in rooms:
            if id == p[0]:
                newRoom = rr.Room(p[3], p[2], p[0], p[4])
                newDevice = dvc.Device(x[1], x[2], newRoom, x[4])
                if str(newDevice.get_Type()) == "Temp":
                    output_temp = temp.Temperature(newDevice, newRoom.get_vindue_state())
                    return output_temp.run()

@app.route('/Sound/Room/<int:id>', methods=['GET'])
def Sound(id):
    for x in devices:
        if str(x.get_Room().get_id()) == str(id):
            if x._Type == "Sound":
                output_sound = sd.SoundCheck(x)
                return output_sound.run()

@app.route('/AabnVinduer/Room/<int:id>', methods=['GET'])
def AabnVinduer(id):
    for x in devices:
        if str(x.get_Room().get_id()) == str(id):
            if bool(x.get_Room().get_vindue_state()) == False:
                x.get_Room().set_vindue_state(True)
                return "Åbner vinduerne i bygning : " + str(x.get_Room().get_building()) + " i lokale : " + str(x.get_Room().get_number()) 
            else:
                x.get_Room().set_vindue_state(False)
                return "Lukker vinduerne i " + str(x.get_Room().get_building()) + " i lokale : " + str(x.get_Room().get_number()) 

app.run()