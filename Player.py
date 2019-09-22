class Player:

    def __init__(self, initial="A", points=0):
        self.initial = initial[0]
        self.points = points
        self.createdBox = False

    def add_points(self, points):
        self.points += points

    def get_points(self):
        return self.points

    def set_initial(self, initial):
        self.initial = initial[0]

    def get_initial(self):
        return self.initial

    def get_created_box(self):
        return self.createdBox

    def set_created_box(self, bool):
        self.createdBox = bool