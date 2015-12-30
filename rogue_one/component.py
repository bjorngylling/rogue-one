import lib.libtcodpy as libtcod

from ecs import Component


class Movement(Component):
    def __init__(self, dx=0, dy=0):
        self.dx = dx
        self.dy = dy


class Position(Component):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


class Renderable(Component):
    def __init__(self, char=None, fg_color=libtcod.white,
                 bk_color=libtcod.black):
        self.char = char
        self.bk_color = bk_color
        self.fg_color = fg_color


class Player(Component):
    def __init__(self):
        self.player = True


class Health(Component):
    def __init__(self, current_hp=0, max_hp=0):
        self.current_hp = current_hp
        self.max_hp = max_hp


class FieldOfView(Component):
    def __init__(self, fov_map=None, algorithm=libtcod.FOV_BASIC,
                 light_walls=False, view_distance=10, recompute=True):
        self.algorithm = algorithm
        self.light_walls = light_walls
        self.view_distance = view_distance
        self.fov_map = fov_map
        self.recompute = recompute
