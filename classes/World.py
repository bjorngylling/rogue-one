import libtcodpy as libtcod
import copy


class Map:

    def __init__(self, map_height, map_width, con):
        self.map_height = map_height
        self.map_width = map_width
        self.con = con
        self.map = [[]]

    def make_map(self):
        self.map[30][22].blocked = True
        self.map[30][22].block_sight = True
        self.map[30][22].char = '#'
        self.map[50][22].blocked = True
        self.map[50][22].block_sight = True
        self.map[50][22].char = '#'

    def draw(self):
        for y in range(self.map_height):
            for x in range(self.map_width):
                tile = self.map[x][y]

                libtcod.console_set_char_background(
                    self.con, x, y, tile.bk_color, libtcod.BKGND_SET)
                libtcod.console_set_default_foreground(self.con, tile.fg_color)
                libtcod.console_put_char(
                    self.con, x, y, tile.char, libtcod.BKGND_NONE)

    def fill_map(self, tile):
        self.map = [[copy.deepcopy(tile)
                     for y in range(self.map_height)]
                    for x in range(self.map_width)]


class Tile:

    def __init__(self, char, fg_color, blocked, bk_color=None, block_sight=None):
        self.char = char
        if bk_color is None:
            bk_color = libtcod.black
        self.bk_color = bk_color
        self.fg_color = fg_color

        self.blocked = blocked

        if block_sight is None:
            block_sight = blocked
        self.block_sight = block_sight
