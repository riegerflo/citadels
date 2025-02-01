from .character import Character, Color

class Koenig(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Koenig'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    @property
    def color(self):
        return Color.GOLDEN

    def use_ability(self):
        print("Using Koenig's skill")

koenig = Koenig()