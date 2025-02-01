from .character import Character, Color

class Haendler(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Haendler'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    @property
    def color(self):
        return Color.GREEN

    def use_ability(self):
        print("Using Haendler's skill")

#haendler = Haendler()