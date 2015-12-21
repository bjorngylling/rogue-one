import lib.libtcodpy as libtcod
import copy


class Level(object):

    def __init__(self, map_height, map_width, con):
        self.map_height = map_height
        self.map_width = map_width
        self.con = con
        self.level = [[]]

    def __setitem__(self, key, item):
        self.level[key] = item

    def __getitem__(self, key):
        return self.level[key]

    def draw(self, fov_map):
        for y in range(self.map_height):
            for x in range(self.map_width):
                tile = self.level[x][y]
                in_fov = libtcod.map_is_in_fov(fov_map, x, y)
                if in_fov:
                    tile.explored = True
                if tile.explored:
                    self.draw_tile(tile, x, y, in_fov)

    def draw_tile(self, tile, x, y, in_fov):
        bk_color = tile.bk_color
        fg_color = tile.fg_color

        if in_fov:
            bk_color = bk_color * 2
            fg_color = fg_color * 2

        libtcod.console_set_char_background(
            self.con, x, y, bk_color, libtcod.BKGND_SET)
        libtcod.console_set_default_foreground(self.con, fg_color)
        libtcod.console_put_char(
            self.con, x, y, tile.char, libtcod.BKGND_NONE)

    def fill_map(self, tile):
        self.level = [[copy.deepcopy(tile)
                       for y in range(self.map_height)]
                      for x in range(self.map_width)]


class Tile(object):

    def __init__(self, char, fg_color, blocked, bk_color=None,
                 block_sight=None):
        self.char = char
        if bk_color is None:
            bk_color = libtcod.black
        self.bk_color = bk_color
        self.fg_color = fg_color

        self.blocked = blocked

        if block_sight is None:
            block_sight = blocked
        self.block_sight = block_sight

        self.explored = False
