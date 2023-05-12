class Dot:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.dots_connected = [] # Lines between dots
        self.is_box = False

    def is_connected(self, cell):
        if cell in self.dots_connected:
            return True
        return False

    def connect_dots(self, dot):
        if not self.is_connected(dot):
            self.dots_connected.append(dot)

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_pos(self, spacer, offset):
        pos = []
        for item in [self.get_row(), self.get_col()]:
            pos.append(((item * spacer) + offset))
        return pos

    def get_box(self):
        return self.is_box

    def set_box(self):
        self.is_box = True

    def is_adjacent(self, dot):
        if dot == self:
            return False
        elif dot.get_row() - self.get_row() in [-1,  1] and dot.get_col() == self.get_col(): # Checks if in same row
            return True
        elif dot.get_col() - self.get_col() in [-1 , 1] and dot.get_row() == self.get_row(): # Checks if in same col
            return True
        return False

