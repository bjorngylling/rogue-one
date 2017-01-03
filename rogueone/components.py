from rogueone import constants


class Position:
    def __init__(self, x: int = 0, y: int = 0, map_section: int = 0) -> None:
        self.x = x
        self.y = y
        self.map_section = map_section


class Velocity:
    def __init__(self, dx: int = 0, dy: int = 0) -> None:
        self.dx = dx
        self.dy = dy


class Collision:
    def __init__(self) -> None:
        pass


class Renderable:
    def __init__(self, character: str,
                 color: Ellipsis = constants.COLOR_WHITE) -> None:
        self.character = character
        self.color = color


class Creature:
    def __init(self,
               strength: int = 10,
               dexterity: int = 10,
               intelligence: int = 10) -> None:
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
