from models.Cell import Cell


class Table:
    def __init__(self, rows):
        self.nr_rows = rows
        self.maze = [None]*rows

        for i in range(rows):
            self.maze[i] = [None]*rows
            for j in range(rows):
                self.maze[i][j] = Cell(i, j)
