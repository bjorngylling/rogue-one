import abc

import libtcodpy as libtcod

from ..World import Tile


class BaseGenerator(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run(self, map):
        return

    def generate_map(self, width, height, el=1):
        return [[el
                 for y in range(height)]
                for x in range(width)]


class TileGenerator:

    color_wall = libtcod.Color(48, 34, 21)
    color_floor = libtcod.Color(48, 42, 21)

    def carve_square(self, x, y, map):
        map[x][y].blocked = False
        map[x][y].block_sight = False
        map[x][y].char = "."
        map[x][y].fg_color = self.color_floor

    def carve_room(self, room, map):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.carve_square(x, y, map)

    def run(self, level, map):
        """Convert a generated map represented with numbers to a map with tiles.

        Keyword arguments:
        level -- the actual level (World.Level)
        map -- the map with numerical values
        """

        for x in level.width:
            for y in level.height:
                if map[x][y] == 1:
                    level[x][y] = Tile("#", self.color_wall, True)
                elif map[x][y] == 0:
                    level[x][y] = Tile(".", self.color_floor, False)

        return level
