import Device as dvc
import Room as rr
import Temp as temp
import sqlite3
from sqlite3 import Error

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

def update_row(conn, task):
    sql = ''' UPDATE ROOM
              SET vinduerAabent = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

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
        for p in rooms:
            if id == p[0]:
                newRoom = rr.Room(p[3], p[2], p[0], p[4])
                if str(newRoom.get_Room().get_id()) == str(id):
                    if bool(newRoom.get_Room().get_vindue_state()) == False:
                        newRoom.get_Room().set_vindue_state(True)
                        try:
                            with con:
                                update_row(con, (True, id))
                        except Error as e:
                            print(e)
                        self._Outcome = "Åbner vinduerne i bygning : " + str(newRoom.get_Room().get_building()) + " i lokale : " + str(newRoom.get_Room().get_number()) 
                    else:
                        newRoom.get_Room().set_vindue_state(False)
                        try:
                            with con:
                                update_row(con, (False, id))
                        except Error as e:
                            print(e)
                        self._Outcome = "Lukker vinduerne i " + str(newRoom.get_Room().get_building()) + " i lokale : " + str(newRoom.get_Room().get_number()) 
    def outcome(self):
        return self._Outcome