from .character import Character, Color

class Meuchler(Character):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'Meuchler'
        self.description = 'At any time use his characters skill'
        # self.img = 'meuchler.jpg'

    @property
    def color(self):
        return Color.NONE

    def use_ability(self):
        print("Using Meuchler's skill")

#meuchler = Meuchler()