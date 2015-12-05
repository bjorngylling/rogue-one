import libtcodpy as libtcod
from classes.Object import Object
from classes.World import Level
from classes.world_generation.RandomRoomGeneration import RandomRoomGeneration


def handle_keys():

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
    'terminal12x12_gs_ro.png',
    libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)

libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'rogue-one', False)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

rrgen = RandomRoomGeneration()
world = Level(MAP_HEIGHT, MAP_WIDTH, con)
rrgen.make_map(world)

player = Object(27, 22, '@', libtcod.white, con, world)
npc = Object(56, 27, '@', libtcod.yellow, con, world)
objects = [player, npc]

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white)

    render_all()

    libtcod.console_flush()

    for object in objects:
        object.clear()

    if handle_keys():
        break
