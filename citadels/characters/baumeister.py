from citadels.characters import Character, Color


class Baumeister(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Baumeister'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    @property
    def color(self):
        return Color.NONE

    def use_ability(self):
        print("Using Baumeister's skill")

baumeister = Baumeister()