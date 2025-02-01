from .character import Character, Color

class Priester(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Priester'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    @property
    def color(self):
        return Color.BLUE

    def use_ability(self):
        print("Using Priester's skill")

#priester = Priester()