from .character import Character

class Soeldner(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Soeldner'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    def use_skill(self):
        print("Using Soeldner's skill")

soeldner = Soeldner()