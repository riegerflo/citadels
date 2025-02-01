from .character import Character, Color

class Dieb(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Dieb'
        self.description = 'At any time use his characters skill'
        # self.img = 'dieb.jpg'
        
    @property
    def color(self):
        return Color.NONE
    
    def use_ability(self):
        print("Using Dieb's skill")

#dieb = Dieb()