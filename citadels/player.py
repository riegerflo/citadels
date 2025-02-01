class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 2
        self.hand = []
        self.city = []
        self.characters = []
        self.game = None

    def set_game(self, game):
        self.game = game
