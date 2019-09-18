import Dots

class DotGame:

    def __init__(self, board_size=8):
        self.board_size = board_size # Amount of dots across the board
        self.board = []
        # Main
        self.new_board()

    def new_board(self):
        self.board = []
        for row in range(0,self.board_size): # Adds dots to board
            self.board.append([])
            for col in range(0,self.board_size):
                self.board[row].append(Dots.Dot(row,col))

    def get_dot_by_row_col(self, row, col):
        if self.is_on_board([row, col]):
            return self.board[row][col]
        return None

    def get_dot_by_posXY(self, x, y, spacer, offset):
        x = int((x - offset) / spacer)
        y = int((y - offset) / spacer)
        if self.is_on_board([x,y]):
            return self.board[x][y]

    def is_on_board(self, coordinates): # Takes coordinates of row and col as an array to determine if on the board
        for pos in coordinates:
            if pos < 0 or pos >= self.board_size:
                return False
        return True

    def connect_dots(self, dot1, dot2):
        dot1.connect_dots(dot2)
        dot2.connect_dots(dot1)

    def is_line(self, dot_1, dot_2):
        return dot_1.is_connected(dot_2)

    def is_box(self, dot):
        if not dot:
            return False
        corner_dot = self.get_dot_by_row_col(dot.get_row() + 1, dot.get_col() + 1)
        if not corner_dot:
            return False
        if not self.is_on_board([dot.get_row(), dot.get_col()]):
            return False
        for pos in [[1,0],[0,1]]:
            if not dot.is_connected(self.get_dot_by_row_col(dot.get_row() + pos[0], dot.get_col() + pos[1])):
                return False
        for pos in [[-1, 0], [0, -1]]:
            if not corner_dot.is_connected(self.get_dot_by_row_col(corner_dot.get_row() + pos[0], corner_dot.get_col() + pos[1])):
                return False
        dot.set_box()
        return True


