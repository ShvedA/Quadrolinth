from models.Location import Location
from models.Wall import Wall


class Cell:
    def __init__(self, row, column):
        self.north = Wall()
        self.east = Wall()
        self.south = Wall()
        self.west = Wall()
        self.location = Location(row, column)
        self.has_treasure = False
        self.has_armoury = False
