class Wall:
    def __init__(self, is_wall=True, breakable=True, is_exit=False):
        self.is_wall = is_wall
        self.breakable = breakable
        self.is_exit = is_exit
