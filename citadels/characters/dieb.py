from .character import Character

class Dieb(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Dieb'
        self.description = 'At any time use his characters skill'
        # self.img = 'dieb.jpg'
    
    def use_skill(self):
        print("Using Dieb's skill")

dieb = Dieb()