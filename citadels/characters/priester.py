from .character import Character

class Priester(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Priester'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    def use_skill(self):
        print("Using Priester's skill")

priester = Priester()