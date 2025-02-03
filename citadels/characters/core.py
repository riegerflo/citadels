from .baumeister import Baumeister
from .dieb import Dieb
from .haendler import Haendler
from .koenig import Koenig
from .magier import Magier
from .priester import Priester
from .meuchler import Meuchler
from .soeldner import Soeldner


def generate_characters(game):
    """Generate the characters for the game."""
    characters = [
        Meuchler(game),
        Dieb(game),
        Magier(game),
        Koenig(game),
        Haendler(game),
        Baumeister(game),
        Priester(game),
        Soeldner(game),
    ]
    return characters