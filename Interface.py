import tkinter as tk
from tkinter import messagebox


class Interface:
    line_width = 6
    def __init__(self, root, window_size, game):
        self.root = root
        self.game = game
        self.fire_icon_path = r"FireIcon32x32.ico"
        self.dot_color = "black"
        self.text_color = "white"
        self.font_style = "TimeNewRoman 20"
        self.window_size = window_size
        self.spacer = int(self.window_size / self.game.board_size + 1)
        self.offset = self.spacer / 2
        self.selectedDot = None
        self.dot_size = self.spacer / 8
        self.canvas = tk.Canvas(root,
                                width=self.window_size+self.spacer,
                                height=self.window_size+self.spacer)
        # Modifications
        self.root.iconbitmap(self.fire_icon_path)
        self.update_current_player_title()
        self.root.resizable(width=False, height=False)
        # Binds
        self.root.bind("<ButtonPress>", lambda event: self.select_dot(event))
        self.root.bind("<ButtonRelease>", lambda event: self.is_line(event))
        # Main
        self.create_interface()
        self.root.mainloop()

    def create_interface(self):
        self.canvas.pack()
        self.draw_dots()

    def draw_dots(self): # Draws dots on the board based on position in array
        for i in range(1,self.game.board_size+1):
            for j in range(1,self.game.board_size+1):
                position = self.game.get_dot_by_row_col(i-1, j-1).get_pos(self.spacer, self.offset)
                self.canvas.create_oval((position[0]-self.offset-self.dot_size)+self.spacer,
                                        (position[1]-self.offset-self.dot_size)+self.spacer,
                                        (position[0]-self.offset+self.dot_size)+self.spacer,
                                        (position[1]-self.offset+self.dot_size)+self.spacer,
                                         fill=self.dot_color)

    def is_line(self, event=None): # Draws lines between dots ; Called by Event
        if event: # Event is a class within Tkinter
            dot = self.game.get_dot_by_posXY(event.x, event.y, self.spacer, self.offset)
            if dot == self.selectedDot: # Prevents making a line for just itself
                return
            if dot:  # Is not None
                if not dot.is_adjacent(self.selectedDot): # Check if dots are next too each other X or Y
                    return
                if not dot.is_connected(self.selectedDot):  # Checks if connected
                    self.draw_line(dot, self.selectedDot)
                    self.claim_box(dot, self.selectedDot)
                    if self.game.is_game_over():
                        winner = self.game.get_winner()
                        self.restart_game(winner)

    def draw_line(self, dot_1, dot_2):
        dot_1.connect_dots(dot_2)
        dot_2.connect_dots(dot_1)
        self.canvas.create_line(dot_1.get_pos(self.spacer, self.offset)[0] + self.offset,
                                dot_1.get_pos(self.spacer, self.offset)[1] + self.offset,
                                dot_2.get_pos(self.spacer, self.offset)[0] + self.offset,
                                dot_2.get_pos(self.spacer, self.offset)[1] + self.offset,
                                fill=self.game.get_current_player().get_color(),
                                width=self.line_width)
        self.game.change_player()
        self.update_current_player_title()

    def claim_box(self, dot_1, dot_2):
        claimed = False
        for dot in [dot_1, dot_2]:
            for posX in range(-1, 2):
                for posY in range(-1, 2):
                    if not dot:
                        break
                    next_dot = self.game.get_dot_by_row_col(dot.get_row() + posX, dot.get_col() + posY)
                    if next_dot:
                        if not next_dot.get_box():
                            if self.game.is_box(next_dot):
                                if not claimed:
                                    claimed = True
                                    self.game.change_player()
                                    self.update_current_player_title()
                                self.canvas.create_text(
                                ((next_dot.get_row()+1) * self.spacer) + self.offset,
                                ((next_dot.get_col()+1) * self.spacer) + self.offset,
                                text=self.game.get_current_player().get_initial(),
                                font=self.font_style,
                                fill=self.game.get_current_player().get_color())
                                self.game.get_current_player().add_points(1)
                                print(self.game.get_current_player().get_points())

    def update_current_player_title(self):
        self.root.title("{0} - Turn : {1}".format(type(self.game).__name__,
                                                  self.game.get_current_player().get_initial()))

    def select_dot(self, event=None): # On Event we select a dot
        if event:
            self.selectedDot = self.game.get_dot_by_posXY(event.x, event.y, self.spacer, self.offset)

    def restart_game(self, winner):
        self.display_winner(winner)
        self.clear_board() # Clears Canvas
        self.new_game() # Creates new game
        self.create_interface() # Draws board again

    def display_winner(self, winner):
        # Create background
        board_length = self.spacer * self.game.board_size
        win_text = "Winner : {}".format(winner)
        self.canvas.create_rectangle(self.spacer, self.spacer,
                                     board_length,board_length, fill=self.dot_color)
        if winner == "Draw":
            win_text = "Its a draw"
        # Display Text
        pos = self.window_size/2+self.offset
        self.canvas.create_text(pos, pos,
                                text=win_text, fill=self.text_color, font=self.font_style)
        messagebox.showinfo("Winner", win_text)

    def clear_board(self):
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.root,
                                width=self.window_size+self.spacer,
                                height=self.window_size+self.spacer)
    def new_game(self):
        self.game.new_game()