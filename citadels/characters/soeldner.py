from citadels.characters import Character, Color

class Soeldner(Character):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'Soeldner'
        self.description = 'At any time use his characters skill'
        # self.img = 'koenig.jpg'

    @property
    def color(self):
        return Color.RED

    def use_ability(self):
        print("Using Soeldner's skill")
        ## user input select player
        
        player_names = [item.name for item in self.game.players]
        #print(player_names)
        ask_players ='Choose player by number: '
        for count,item in enumerate(player_names):
            ask_players = ask_players + "\n" + str(count +1) + ') '+ item
        target_player = input(f"{ask_players}")
        #building_names =
        available_buildings = self.game.players[int(target_player)-1].city
        print(available_buildings)
        ask_target_building = 'Choose building by number: '
        for item in enumerate(available_buildings):
            ask_target_building = ask_target_building + "\n" + str(item[0] +1) + ') '+ item[1]
        input_building = input(f"{ask_target_building}")
        print(input_building)
        del available_buildings[int(input_building)-1]

        self.game.players[int(target_player)-1].city = available_buildings
        print(self.game.players[int(target_player)-1].city)


#soeldner = Soeldner()

if __name__ == "__main__":
    from unittest.mock import Mock
    from citadels.player import Player
    
    game = Mock()
    player1 = Player('Player 1')
    player1.city = ["Jagdschloss", "Kaserne"]
    player2 = Player('Player 2')
    player2.city = ["Kaserne", "Arschgesicht", "Puff"]
    game.players = [player1, player2]
    
    soeldner = Soeldner(game)
    soeldner.use_ability()