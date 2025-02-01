"""Handles the states of the game at the highest level."""
from random import choice

from citadels.characters import characters
from citadels.states.turn import PlayerTurnContext, ChooseCharactersContext

class Game:
    def __init__(self, players):
        self.players = players
        for player in players:
            player.set_game(self)
        self.current_player = players[0]
        self.next_start_player = choice(players)

        self.deck = []
        self.discard = []
        self.characters = []

        self.round = 0
        self.last_round = False

    def start(self):
        """Start the game."""
        while True:
            self.characters = characters 
            self.round += 1
            print("Entering round", self.round)

            # Assign characters to players
            ChooseCharactersContext(self).request()

            while self.characters:
                # Do turns for one player
                self.current_player = self._get_next_player()
                print(f"Player {self.current_player.name}'s turn")
                next_turn = PlayerTurnContext(self.current_player, self)
                next_turn.request()

                self.last_round = self._player_reached_win_condition(self.current_player)

    def _player_reached_win_condition(self, player):
        """Check if the player reached the win condition."""
        return len(player.buildings) >= 8

    def _get_next_player(self):
        """Based on the character order, get the next player."""
        character = self.characters.pop(0)
        for player in self.players:
            if character in player.characters:
                return player


if __name__ == '__main__':
    from citadels.player import Player

    game = Game([
        Player('Alice'),
        Player('Bob'),
        Player('Charlie'),
    ])
    game.start()