from .character import Character

class Magier(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Magier'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    def use_skill(self):
        print("Using Magier's skill")

magier = Magier()