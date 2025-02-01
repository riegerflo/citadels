from .character import Character, Color

class Soeldner(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Soeldner'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    @property
    def color(self):
        return Color.RED

    def use_ability(self):
        print("Using Soeldner's skill")

soeldner = Soeldner()