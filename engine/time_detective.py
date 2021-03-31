class TimeDetective:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TimeDetective, cls).__new__(cls)
        return cls.instance

    def __init__(self, move=None, game=None, all_time=None):
        self.move = move

    def get_move(self):
        return self.move
