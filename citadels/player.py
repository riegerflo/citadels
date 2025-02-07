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

    def add_character(self, character):
        self.characters.append(character)

    def get_input(self, msg):
        return input(f"({self.name}): {msg}")

    def send_msg(self, msg):
        print(f"({self.name}): {msg}")

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "Player(%r)" % self.name

    
