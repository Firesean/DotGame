import Dots
import Player

class DotGame:

    def __init__(self, board_size=8, players=[Player.Player("A"), Player.Player("B")]):
        self.board_size = board_size # Amount of dots across the board
        self.board = []
        self.players = players
        self.current_player = self.players[0]
        # Main
        self.new_game()


    def reset_players(self):
        for player in self.players:
            player.reset_points()

    def get_current_player(self):
        return self.current_player

    def change_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def new_game(self):  # Adds dots to board
        self.reset_players()
        self.board = []
        for row in range(0,self.board_size):
            self.board.append([])
            for col in range(0,self.board_size):
                self.board[row].append(Dots.Dot(row, col))

    def get_dot_by_row_col(self, row, col):
        if self.is_on_board([row, col]):
            return self.board[row][col]
        return None

    def get_dot_by_posXY(self, x, y, spacer, offset):
        x = int((x - offset) / spacer)
        y = int((y - offset) / spacer)
        return self.get_dot_by_row_col(x,y)

    def is_on_board(self, coordinates): # Takes coordinates of row and col as an array to determine if on the board
        for pos in coordinates:
            if pos < 0 or pos >= self.board_size:
                return False
        return True

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

    def is_game_over(self):
        if (self.board_size - 1)**2 == self.players[0].get_points() + self.players[1].get_points():
            return True
        return False

    def get_winner(self):
        p1 = self.players[0]
        p2 = self.players[1]
        if p1.get_points() == p2.get_points():
            return "Draw"
        if p1.get_points() > p2.get_points():
            return p1.get_initial()
        return p2.get_initial()



