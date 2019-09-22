import tkinter as tk
import Dots

class Interface:

    def __init__(self, root, window_size, game):
        self.root = root
        self.game = game
        self.dot_color = "black"
        self.window_size = window_size
        self.spacer = int(self.window_size / self.game.board_size + 1)
        self.offset = self.spacer / 2
        self.selectedDot = None
        self.dot_size = self.spacer / 8
        self.canvas = tk.Canvas(root,
                                width=self.window_size+self.spacer,
                                height=self.window_size+self.spacer)
        # Modifications
        self.root.title("{}".format(type(self.game).__name__))
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

    def draw_line(self, dot_1, dot_2):
                dot_1.connect_dots(dot_2)
                dot_2.connect_dots(dot_1)
                self.canvas.create_line(dot_1.get_pos(self.spacer, self.offset)[0] + self.offset,
                                        dot_1.get_pos(self.spacer, self.offset)[1] + self.offset,
                                        dot_2.get_pos(self.spacer, self.offset)[0] + self.offset,
                                        dot_2.get_pos(self.spacer, self.offset)[1] + self.offset,
                                        fill="black")
                self.game.change_player()

    def claim_box(self, dot_1, dot_2):
        for dot in [dot_1, dot_2]:
            for posX in range(-1, 2):
                for posY in range(-1, 2):
                    if not dot:
                        break
                    next_dot = self.game.get_dot_by_row_col(dot.get_row() + posX, dot.get_col() + posY)
                    if next_dot:
                        if not next_dot.get_box():
                            if self.game.is_box(next_dot):
                                self.game.change_player() # Bug with claiming 2 squares
                                self.canvas.create_text(
                                ((next_dot.get_row()+1) * self.spacer) + self.offset,
                                ((next_dot.get_col()+1) * self.spacer) + self.offset,
                                text=self.game.current_player.get_initial(),
                                font="TimesNewRoman 20")

    def select_dot(self, event=None): # On Event we select a dot
        if event:
            self.selectedDot = self.game.get_dot_by_posXY(event.x, event.y, self.spacer, self.offset)



