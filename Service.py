from Measurement import Device as dvc
from Measurement import Room as rr
from Measurement import Temp as temp
import sqlite3
from sqlite3 import Error


devices = []
rooms = []

def updatestuff():
    devices.clear()
    rooms.clear()
    con = sqlite3.connect('example.db')
    with con:
        data = con.execute("SELECT * FROM ROOM")
        for row in data:
            rooms.append(row)
        data2 = con.execute("SELECT * FROM Device")
        for row in data2:
            print(row)
            devices.append(row)

def set_devices(x):
    global devices 
    devices = x
def set_rooms(x):
    global rooms
    rooms = x

def get_devices():
    updatestuff()
    return devices

def get_rooms():
    updatestuff()
    return rooms

class Service():
    _Outcome = ""
    def __init__(self, id, Type):
        for x in devices:
            for p in rooms:
                if id == p[0]:
                    newRoom = rr.Room(p[3], p[2], p[0], p[4])
                    newDevice = dvc.Device(x[1], x[2], newRoom, x[4])
                    if str(newDevice.get_Type()) == Type:
                        output_temp = temp.Temperature(newDevice, newRoom.get_vindue_state())
                        self._Outcome = output_temp.run()
                        break
    def outcome(self):
        return self._Outcome

class OpenWindows():
    _Outcome = ""
    def __init__(self, id):
        con = sqlite3.connect('example.db')
        for p in rooms:
            if id == p[0]:
                newRoom = rr.Room(p[3], p[2], p[0], p[4])
                if str(newRoom.get_id()) == str(id):
                    if bool(newRoom.get_vindue_state()) == False:
                        try:
                            with con:
                                sql = ''' UPDATE ROOM SET vinduerAabent = 1 WHERE id = ''' + str(id)
                                con.execute(sql)
                            self._Outcome = "1"
                        except Error as e:
                            self._Outcome = str(e)
                    else:
                        try:
                            with con:
                                sql = ''' UPDATE ROOM SET vinduerAabent = 0 WHERE id = ''' + str(id)
                                con.execute(sql)
                            self._Outcome = "0"
                        except Error as e:
                            self._Outcome = str(e)
    def outcome(self):
        return self._Outcome