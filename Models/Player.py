from Models.Location import Location


class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.location = Location(x, y)
        self.shots_left = 5
        self.mines = 1
        self.has_treasure = False
        self.alive = True
