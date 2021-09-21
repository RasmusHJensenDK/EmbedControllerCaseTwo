from Measurement import Room as room

class Device():
    _ConnectorPin = 0
    _State = "OFF"
    _Type = "None"
    _Room = room.Room(0,0,0, False)
    def __init__(self, CP, Type, Room, *State):
        self._ConnectorPin = CP
        self._Type = Type
        self._Room = Room
        self._State = State
    def get_ConnectorPin(self):
        return self._ConnectorPin
    def set_ConnectorPin(self, x):
        self._ConnectorPin = x
    def get_Type(self):
        return self._Type
    def set_Type(self, x):
        self._Type = x
    def get_Room(self):
        return self._Room
    def set_Room(self, x):
        self._Room = x
    def get_State(self):
        return self._State
    def set_State(self, x):
        self._State = x