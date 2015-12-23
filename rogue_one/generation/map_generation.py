import abc
import lib.libtcodpy as libtcod

from rogue_one.map import Tile


class BaseGenerator(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, seed):
        self.seed = seed

    @abc.abstractmethod
    def run(self, map, seed):
        pass

    def generate_map(self, width, height, el=1):
        return [[el
                 for y in range(height)]
                for x in range(width)]


class TileGenerator(object):

    color_wall = libtcod.Color(48, 34, 21)
    color_floor = libtcod.Color(48, 42, 21)

    def run(self, level, map):
        """Convert a generated map represented with numbers to a map with tiles.

        Keyword arguments:
        level -- the actual level (World.Level)
        map -- the map with numerical values
        """

        for x in range(level.map_width):
            for y in range(level.map_height):
                if map[x][y] == 1:
                    level[x][y] = Tile("#", self.color_wall, True)
                elif map[x][y] == 0:
                    level[x][y] = Tile(".", self.color_floor, False)

        return level
