import lib.libtcodpy as libtcod


class Object:

    def __init__(self, x, y, char, color, con, current_level):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.con = con
        self.current_level = current_level

    def move(self, dx, dy):
        if not self.current_level[self.x + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy

    def draw(self):
        libtcod.console_set_default_foreground(self.con, self.color)
        libtcod.console_put_char(self.con, self.x, self.y,
                                 self.char, libtcod.BKGND_NONE)

    def clear(self):
        libtcod.console_put_char(self.con, self.x, self.y,
                                 ' ', libtcod.BKGND_NONE)
