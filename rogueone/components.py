from rogueone import constants


class Player:
    pass


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Renderable:
    def __init__(self, character, color=constants.COLOR_WHITE):
        self.character = character
        self.color = color
