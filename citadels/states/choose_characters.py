"""State machine for choosing characters"""
import abc
import logging

class TwoPlayerStrategy:
    """Character drawing strategy for two players."""
    def __init__(self, context):
        self.context = context

    def next_state(self, current_state):

        # Initial state
        if current_state is None: 
            return DropFirstCharacterAction(self.context)

        # End character selection
        if not len(self.context.characters):
            return None

        elif isinstance(current_state, DropFirstCharacterAction):
            return ChooseAction(self.context)

        elif isinstance(current_state, ChooseAction):
            if isinstance(self.context.last_state, DropFirstCharacterAction):
                return NextPlayerState(self.context)
            elif isinstance(self.context.last_state, NextPlayerState):
                return DropAction(self.context)
        
        elif isinstance(current_state, DropAction):
            return NextPlayerState(self.context)
        
        elif isinstance(current_state, NextPlayerState):
            return ChooseAction(self.context)
        
        else:
            raise ValueError(f"Invalid state: {current_state}")


def get_strategy(context):
    if len(context.game.players) == 2:
        logging.debug("Using TwoPlayerStrategy")
        return TwoPlayerStrategy(context)
    else:
        raise NotImplementedError("Only two player games are supported for now.")


class ChooseCharacterContext:
    def __init__(self, game):
        logging.debug("Creating ChooseCharacterContext")
        self.game = game
        self._next_state_strategy = get_strategy(self)

        self.characters = game.characters.copy()

        self.current_player = game.next_start_player
        self.current_player_index = game.players.index(self.current_player)

        self.state = None
        self.last_state = None

    def next_state(self, current_state):
        self.state = self._next_state_strategy.next_state(current_state)
        logging.debug(f"Next state: {self.state}")

    def request(self):
        """Request the player to choose a character."""
        self.next_state(self.state)
        while self.state is not None:
            self.state.handle()
            last_state = self.state
            self.next_state(self.state)
            self.last_state = last_state


class State(abc.ABC):
    def __init__(self, context):
        self.context = context

    def handle(self):
        raise NotImplementedError

class ChooseAction(State):
    def handle(self):
        print("Choosing a character")
        character_idx = self.get_user_input() - 1
        character = self.context.characters.pop(character_idx)
        self.context.current_player.characters.append(character)
        print("Chose character: ", character)

    def get_user_input(self):
        character_str = "\n".join([f"({i+1}) {character}" for i, character in enumerate(self.context.characters)])
        return int(input(f"Choose a character: \n{character_str}\n"))


class DropAction(State):
    def handle(self):
        print("Dropping a character")
        if len(self.context.characters) > 1:
            character_idx = self.get_user_input() - 1
        else:
            character_idx = 0
        character = self.context.characters.pop(character_idx)
        print("Dropped character: ", character)

    def get_user_input(self):
        character_str = "\n".join([f"({i+1}) {character}" for i, character in enumerate(self.context.characters)])
        return int(input(f"Drop a character: \n{character_str}\n"))


class NextPlayerState(State):
    def handle(self):
        self.context.current_player_index += 1
        if self.context.current_player_index >= len(self.context.game.players)-1:
            self.context.current_player_index = 0

        self.context.current_player = self.context.game.players[self.context.current_player_index]
        print(f"Next player: {self.context.current_player.name}")


class DropFirstCharacterAction(State):
    def handle(self):
        print("Dropping first character")
        character = self.context.characters.pop(0)
        self.send_user_msg(character)

    def send_user_msg(self, character):
        print(f"Dropped first character: \n{character}\n")


if __name__ == '__main__':
    from unittest.mock import Mock
    from citadels.player import Player

    logging.basicConfig(level=logging.DEBUG)

    game = Mock()
    game.players = [
        Player('Alice'),
        Player('Bob'),
        Player('Charlie'),
    ]
    game.characters = [
        "Meuchler",
        "Dieb",
        "Baumeister",
        "Magier",
        "König",
        "Händler",
        "Prediger",
        "Söldner",
    ]
    game.next_start_player = game.players[0]
    game.start()
    ChooseCharacterContext(game, TwoPlayerStrategy).request()