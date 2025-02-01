## Andi to do this
"""All the game characters are created here."""
import abc
import logging
from enum import Enum
import pandas as pd
import random


class Building():
    """Base class for all the buildings."""
    
    def __init__(self, name, cost, color, victory_points, actions):
        self.name = name
        self.cost = cost
        self.color = color
        self.victory_points = victory_points
        self.actions = actions

    def special_action(self):
        """Perform a special action specific to the building."""
        pass

def generate_deck(filename):
    ##file "./citadels/buildings/ListBuildings.xlsx"
    df = pd.read_excel(filename)
    buildings = []
    for item in df.iterrows():
        for i in range(item[1]['Frequency']):
            _building = Building(name=item[1]['Name'],
                    cost=item[1]['Cost'],
                    color=item[1]['Color'],
                    victory_points=item[1]['VictoryPoints'],
                    actions=item[1]['SpecialAbility'])
            buildings.append(_building)
    random.shuffle(buildings)
    return buildings
for item in generate_deck("./citadels/buildings/ListBuildings.xlsx"):
    print(item.name)
    print(item.cost)
    print(item.color)
    print(item.victory_points)
    print(item.actions)

    

