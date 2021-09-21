class Room():
    _number = 0
    _building = 0
    _ID = 0
    def __init__(self, number, building, ID):
        self._number = number
        self._building = building
        self._ID = ID
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