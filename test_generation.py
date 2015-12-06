import libtcodpy as libtcod

from classes.world_generation.BSPGenerator import BSPGenerator

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

bsp = BSPGenerator(libtcod.random_new())
map = bsp.generate_map(SCREEN_WIDTH, SCREEN_HEIGHT, 0)
tree = bsp.run(map)


def trace_sections(tree):
    rect = tree.data

    def listener(x, y):
        map[x][y] = 3
        return True

    libtcod.line(rect.x1, rect.y1, rect.x2, rect.y1, listener)
    libtcod.line(rect.x1, rect.y1, rect.x1, rect.y2, listener)
    libtcod.line(rect.x2, rect.y1, rect.x2, rect.y2, listener)
    libtcod.line(rect.x1, rect.y2, rect.x2, rect.y2, listener)

    if tree.left is not None:
        trace_sections(tree.left)
    if tree.right is not None:
        trace_sections(tree.right)

trace_sections(tree)

libtcod.console_set_custom_font(
    'terminal12x12_gs_ro.png',
    libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'rogue-one', False)

for x in range(SCREEN_WIDTH):
    for y in range(SCREEN_HEIGHT):
        col = libtcod.Color(60 * map[x][y], 60 * map[x][y], 60 * map[x][y])
        libtcod.console_set_char_background(0, x, y, col)
        libtcod.console_set_default_foreground(0, libtcod.dark_grey)
        libtcod.console_put_char(0, x, y, ".")

libtcod.console_flush()

libtcod.console_wait_for_keypress(True)
