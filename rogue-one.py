import libtcodpy as libtcod
from classes.Object import Object
from classes.World import Map


def handle_keys():
    global playerx, playery

    key = libtcod.console_wait_for_keypress(True)

    if key.vk == libtcod.KEY_ESCAPE:
        return True

    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move(0, -1)

    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move(0, 1)

    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(-1, 0)

    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move(1, 0)


def render_all():
    world.draw()

    for object in objects:
        object.draw()

    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_WIDTH = 80
MAP_HEIGHT = 45

libtcod.console_set_custom_font(
    'arial10x10.png',
    libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'rogue-one', False)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white, con)
npc = Object(SCREEN_WIDTH/2 + 3, SCREEN_HEIGHT/2 + 3, '@', libtcod.yellow, con)
objects = [player, npc]

world = Map(MAP_HEIGHT, MAP_WIDTH, con)
world.make_map()

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white)

    render_all()

    libtcod.console_flush()

    for object in objects:
        object.clear()

    if handle_keys():
        break
