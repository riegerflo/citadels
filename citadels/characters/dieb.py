from .character import Character, Color

class Dieb(Character):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'Dieb'
        self.description = 'At any time use his characters skill'
        # self.img = 'dieb.jpg'
        
    @property
    def color(self):
        return Color.NONE
    
    def use_ability(self):
        print("Using Dieb's skill")

#dieb = Dieb()