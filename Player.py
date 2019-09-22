class Player:

    def __init__(self, initial="A", points=0):
        self.initial = initial[0]
        self.points = points

    def add_points(self, points):
        self.points += points

    def get_points(self):
        return self.points

    def set_initial(self, initial):
        self.initial = initial[0]

    def get_initial(self):
        return self.initial
