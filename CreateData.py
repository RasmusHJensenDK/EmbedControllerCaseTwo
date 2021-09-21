import sqlite3
import Room as rr
import Device as dvc

con = sqlite3.connect('example.db')
#with con:
#    data = con.execute("SELECT * FROM ROOM")
#    for row in data:
#        print(row)
#    data2 = con.execute("SELECT * FROM Device")
#    for row in data2:
#        print(row)
#with con:
#    con.execute("""
#        CREATE TABLE ROOM (
#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#            name TEXT,
#            building INTEGER NOT NULL,
#            number INTEGER NOT NULL,
#            vinduerAabent BOOL
#        );
#    """)
#with con:
#    con.execute("""
#        CREATE TABLE Device (
#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#            CP INTEGER NOT NULL,
#            TYPE TEXT,
#            Room INTEGER,
#            State TEXT
#        );
#    """)

#sql = 'INSERT INTO ROOM (name, building, number, vinduerAabent) values(?,?,?,?)'
#data = [
#    ("City ground floor South", 1, 1, False),
#    ("City ground floor Center", 1, 2, False),
#    ("City ground floor North", 1, 3, False),
#    ("City first floor South", 1, 4, False),
#    ("City first floor Center", 1, 5, False),
#    ("City first floor North", 1, 6, False)
#]
#sqldevice = 'INSERT INTO Device(CP, TYPE, Room, State) values(?,?,?,?)'
#datadevice = [
#    (7, "Temp", 1, "ON"),
#    (15, "Light", 1, "ON"),
#    (14, "Sound", 1, "ON")
#]

#with con:
#    con.executemany(sqldevice, datadevice)

