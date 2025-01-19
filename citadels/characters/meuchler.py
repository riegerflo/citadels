from .character import Character

class Meuchler(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Meuchler'
        self.description = 'At any time use his characters skill'
        # self.img = 'meuchler.jpg'

    def use_skill(self):
        print("Using Meuchler's skill")

meuchler = Meuchler()