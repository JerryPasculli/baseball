class Squadra:
    def __init__(self, ID, teamCode, name, year):
        self._ID = ID
        self._teamCode = teamCode
        self._name = name
        self._year = year

    def __eq__(self, other):
        if other is None:
            return False
        return self._ID == other._ID

    def __hash__(self):
        return hash(self._ID)