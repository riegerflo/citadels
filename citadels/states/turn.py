"""Handles the states of a players turn.

A players turn goes as follows:

* Take two gold coins
* OR draw two cards AND throw one away
* Lay out a building
* At any time use his characters skill
"""
from unittest.mock import MagicMock

class State:
    def __init__(self, context):
        self.context = context
    def handle(self):
        raise NotImplementedError("Handle method not implemented")


class DecideAction(State):
    def get_user_input(self):
        return input("Choose action: \n(1) Take two gold coins, \n(2) Draw two cards and throw one away:\n ")
    def handle(self):
        action = self.get_user_input()
        if action == '1':
            self.context.state = TakeTwoGoldCoins(self.context)
        elif action == '2':
            self.context.state = DrawTwoCards(self.context)
        else:
            print("Invalid action. Try again.")
            self.context.state = DecideAction(self.context)

class TakeTwoGoldCoins(State):
    def handle(self):
        print("Taking two gold coins")
        self.context.player.gold += 2
        self.context.state = LayOutBuilding(self.context)

class DrawTwoCards(State):
    def get_user_input(self, cards):
        card = input(f"Choose a card to keep: \n(1) {cards[0]} \n(2) {cards[1]}\n")
        if card not in ['1', '2']:
            print("Invalid card. Try again. Choose 1 or 2.")
            self.get_user_input(cards)
        return int(card)

    def handle(self):
        print("Drawing two cards")
        cards = [self.context.game.draw() for _ in range(2)]
        card = self.get_user_input(cards)
        print(f"Keeping card: {cards[card-1]}")
        self.context.player.hand.append(cards[card-1])
        self.context.state = LayOutBuilding(self.context)

class LayOutBuilding(State):
    def get_user_input(self):
        choices = [card.name for card in self.context.player.hand]
        choices_str = "\n(0) No"
        choices_str += "\n" + "\n".join([f"({i+1}) {card}" for i, card in enumerate(choices)])
        return int(input(f"Do you want to lay out a building?: {choices_str}\n"))

    def handle(self):
        build = self.get_user_input()
        if not build:
            print("Not laying out a building")
        else:
            building = self.context.player.hand.pop(build-1)

            if not self.context.player.gold >= building.cost:
                print(f"Not enough gold ({self.context.player.gold}) to lay out building ({building.cost})")
                self.context.player.hand.insert(build-1, building)
                self.context.state = LayOutBuilding(self.context)
                return

            print(f"Laying out building: {building} for {building.cost} gold")
            self.context.player.city.append(building)
            self.context.player.gold -= building.cost
        self.context.state = UseCharacterSkill(self.context)

class UseCharacterSkill(State):
    def handle(self):
        use_skill = input("Do you want to use your character's skill? (yes/no): ")
        if use_skill.lower() == 'yes':
            print("Using character skill")
        self.context.state = EndTurn(self.context)

class EndTurn(State):
    def handle(self):
        print("Ending turn")
        self.context.state = None  # No next state

class PlayerTurnContext:
    def __init__(self, player, game):
        self.state = DecideAction(self)
        self.player = player
        self.game = game

    def request(self):
        while self.state is not None:
            self.state.handle()

# Example usage
if __name__ == "__main__":
    turn = PlayerTurnContext(MagicMock(), MagicMock())
    turn.request()

