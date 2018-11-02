from models.Location import Location
from models.Wall import Wall
from models.Direction import Direction


class Cell:

    def create_walls_dir(self, walls, unbreakable):
        walls_dir = {}
        for direction in Direction:
            if walls is not None and direction in walls:
                if unbreakable is not None and direction in unbreakable:
                    walls_dir[direction] = Wall(True, False)
                else:
                    walls_dir[direction] = Wall(True, True)
            else:
                if unbreakable is not None and direction in unbreakable:
                    walls_dir[direction] = Wall(False, False)
                else:
                    walls_dir[direction] = Wall(False, True)
        return walls_dir

    def __init__(self, row, column, walls=None, unbreakable=None):
        self.walls = self.create_walls_dir(walls, unbreakable)
        self.location = Location(row, column)
        self.has_treasure = False
        self.has_armoury = False
