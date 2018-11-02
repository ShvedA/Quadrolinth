from models.Cell import Cell
from models.Direction import Direction

class Table:

    def any_outer(self, i, j):
        any_outer = []
        if i == 0: any_outer.append(Direction.NORTH)
        if i == self.rows - 1: any_outer.append(Direction.SOUTH)
        if j == 0: any_outer.append(Direction.WEST)
        if j == self.cols - 1: any_outer.append(Direction.EAST)
        return any_outer

    def draw_map(self):
        for i in range(self.rows * 2 + 1):
            for j in range(self.cols * 2 + 1):
                if i == self.rows * 2:
                    if j % 2 == 0:
                        print(' ', end='')
                    elif self.maze[i // 2 - 1][j // 2].walls[Direction.SOUTH].is_wall:
                        print('*', end='')
                    else:
                        print('.', end='')
                elif i % 2 == 0:
                    if j % 2 == 0:
                        print(' ', end='')
                    elif self.maze[i // 2][j // 2].walls[Direction.NORTH].is_wall:
                        print('*', end='')
                    else:
                        print('.', end='')
                else:
                    if j == self.cols * 2:
                        if self.maze[i // 2][j // 2 - 1].walls[Direction.EAST].is_wall:
                            print('*', end='')
                        else:
                            print('.', end='')
                    elif j % 2 == 1:
                        print('c', end='')
                    elif self.maze[i // 2][j // 2].walls[Direction.WEST].is_wall:
                        print('*', end='')
                    else:
                        print('.', end='')
            print()

    def __init__(self, rows, cols=-1):
        self.rows = rows
        if cols == -1:
            self.cols = rows
        self.maze = [None]*rows

        for i in range(self.rows):
            self.maze[i] = [None]*self.cols
            for j in range(self.cols):
                self.maze[i][j] = Cell(i, j, unbreakable=self.any_outer(i, j))

Table(6).draw_map()
