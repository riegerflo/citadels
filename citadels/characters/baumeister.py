from .character import Character

class Baumeister(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Bauemeister'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    def use_skill(self):
        print("Using Baumeister's skill")

baumeister = Baumeister()