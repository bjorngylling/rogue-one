from rogueone import constants


class Position:
    def __init__(self, x=0, y=0, map=0):
        self.x = x
        self.y = y
        self.map = map


class Renderable:
    def __init__(self, character, color=constants.COLOR_WHITE):
        self.character = character
        self.color = color


class MapSection:
    def __init__(self, data):
        self.data = data
