"""Handles the states of the game at the highest level."""
from random import choice, shuffle
import logging

from citadels.buildings.buildings import generate_deck
from citadels.characters import generate_characters
from citadels.states.turn import PlayerTurnContext 
from citadels.states.choose_characters import ChooseCharacterContext

class Game:
    """The game state."""

    logger = logging.getLogger(__name__).getChild('Game')

    def __init__(self, players):
        self.logger.debug('Creating game with players %s', players)

        self.players = players
        for player in players:
            player.set_game(self)

        # The player that currently has the turn
        self.current_player = players[0]

        # Player that chooses the first character
        self.next_start_player = choice(players)
        self.logger.debug('Next start player (considered King) is %s', self.next_start_player)

        self.deck = generate_deck("./citadels/buildings/ListBuildings.xlsx")
        self.discard = []
        self.characters = generate_characters(self)

        self.choose_character_context = ChooseCharacterContext(self)

        self.round = 0
        self.last_round = False

    def start(self):
        """Start the game."""
        while True:         
            self.round += 1
            print("Entering round", self.round)
            self.logger.debug(f"Round {self.round}")

            # Assign characters to players
            self.choose_character_context.request()

            while len(self.characters):
                # Do turns for one player
                self.current_player = self._get_next_player()

                if self.current_player is None:
                    break

                self.logger.debug("Player %s's turn", self.current_player.name)
                print(f"Player {self.current_player.name}'s turn")
                next_turn = PlayerTurnContext(self.current_player, self)
                next_turn.request()

                self.last_round = self._player_reached_win_condition(self.current_player)
                if self.last_round:
                    self.logger("Win condition reached by player %s", self.current_player.name)
            
            self.logger.debug("Round %d ended", self.round)
            self.characters = generate_characters(self)
            for player in self.players:
                player.characters = []

    def draw(self):
        """Draw a card from the deck."""
        if not len(self.deck):
            self.deck = shuffle(self.discard)
            self.discard = []

        return self.deck.pop()

    def _player_reached_win_condition(self, player):
        """Check if the player reached the win condition."""
        return len(player.city) >= 8

    def _get_next_player(self):
        """Based on the character order, get the next player."""
        while len(self.characters):
            character = self.characters.pop(0)
            for player in self.players:
                if character in player.characters:
                    return player


if __name__ == '__main__':
    from citadels.player import Player

    logging.basicConfig(level=logging.DEBUG)

    game = Game([
        Player('Alice'),
        Player('Bob'),
        # Player('Charlie'),
    ])
    game.start()