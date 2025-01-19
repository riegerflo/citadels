from .character import Character

class Haendler(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Haendler'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    def use_skill(self):
        print("Using Haendler's skill")

haendler = Haendler()