from .character import Character, Color

class Magier(Character):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'Magier'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    @property
    def color(self):
        return Color.NONE

    def use_ability(self):
        print("Using Magier's skill")

#magier = Magier()