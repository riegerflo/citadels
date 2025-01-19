from .character import Character

class Koenig(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Koenig'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    def use_skill(self):
        print("Using Koenig's skill")

koenig = Koenig()