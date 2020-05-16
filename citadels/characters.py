"""All the game characters are created here."""
import abc
import logging
from enum import Enum


class Color(Enum):
    GOLDEN = 1
    GREEN = 2
    BLUE = 3
    RED = 4


class Character(abc.ABC):
    """Base class for all the characters."""

    def __init__(self, game):
        self._logger = logging.getLogger(__name__).getChild(str(self))

        # List of actions executed after activation
        self._actions = []

        # game instance
        self.game = game

    def __str__(self):
        """Return class name as str."""
        return type(self).__name__

    @property
    def current_player(self):
        """Player who plays with this character in current round."""
        if not hasattr(self, '_player'):
            raise ValueError('%s has no current player yet!' % self)

        return self._player

    @current_player.setter
    def current_player(self, player):
        self._logger.debug('Current player changed to %s' % player)
        self._player = player

    @property
    @abc.abstractmethod
    def color(self):
        """Color of the character. Can be yellow, green, blue, red or None."""
        ...

    @property
    def active(self):
        """This flag determines if the character will be played during a round."""
        if not hasattr(self, '_active'):
            self._active = False
        return self._active

    @active.setter
    def active(self, active):
        self._logger.debug('Setting %s character to active=%s', self, active)
        self._active = active

        if active:
            self.execute_actions()

    @abc.abstractmethod
    def use_ability(self):
        """Uses the characters special ability."""
        ...

    def add_action(self, action):
        self._actions.append(action)

    def execute_actions(self):
        self._logger.debug('Exectuting %i actions', len(self._actions))
        while len(self._actions):
            action = self._actions.pop()
            action()

    def isCharacter(self, str):
        """Compares if given string is this character."""
        return str.lower() == str(self).lower()

    def play(self):
        self.use_ability()


