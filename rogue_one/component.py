import lib.libtcodpy as libtcod

from ecs import Component


class Movement(Component):
    def __init__(self):
        dx = 0
        dy = 0


class Position(Component):
    def __init__(self):
        x = None
        y = None


class Renderable(Component):
    def __init__(self):
        char = None
        bg_color = libtcod.BKGND_NONE
        fb_color = libtcod.white


class Player(Component):
    def __init__(self):
        pass


class Health(Component):
    def __init__(self):
        current_hp = 0
        max_hp = 0


class FieldOfView(Component):
    def __init__(self):
        algorithm = libtcod.FOV_BASIC
        light_walls = False
        view_distance = 0
        fov_map = None
        recompute = True
