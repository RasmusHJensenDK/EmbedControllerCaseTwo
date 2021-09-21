class Room():
    _number = 0
    _building = 0
    _ID = 0
    _VinduerAabent = False
    def __init__(self, number, building, ID, vinduerAabent):
        self._number = number
        self._building = building
        self._ID = ID
        self._VinduerAabent = vinduerAabent
    def get_number(self):
        return self._number
    def set_number(self, x):
        self._number = x
    def get_building(self):
        return self._building
    def set_building(self, x):
        self._building = x
    def get_id(self):
        return self._ID
    def set_id(self, x):
        self._ID = x
    def get_vindue_state(self):
        return self._VinduerAabent
    def set_vindue_state(self, x):
        self._VinduerAabent = x