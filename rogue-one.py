import lib.libtcodpy as libtcod
from rogue_one.ecs import Entity
from rogue_one.map import Level
from rogue_one.generation.map_generation import TileGenerator
from rogue_one.generation.bsp_generation import BSPGenerator


def handle_keys():
    global fov_recompute

    key = libtcod.console_wait_for_keypress(True)

    if key.vk == libtcod.KEY_ESCAPE:
        return True

    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        fov_recompute = True
        player.move(0, -1)

    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        fov_recompute = True
        player.move(0, 1)

    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        fov_recompute = True
        player.move(-1, 0)

    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        fov_recompute = True
        player.move(1, 0)


def render_all(fov_map):
    world.draw(fov_map)

    for object in objects:
        if libtcod.map_is_in_fov(fov_map, object.x, object.y):
            object.draw()

    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_WIDTH = 70
MAP_HEIGHT = 46

FOV_ALGO = 0
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

random = libtcod.random_new()

libtcod.console_set_custom_font(
    'terminal12x12_gs_ro.png',
    libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)

libtcod.console_init_root(
    SCREEN_WIDTH, SCREEN_HEIGHT, 'rogue-one', False, libtcod.RENDERER_GLSL)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

map_gen = BSPGenerator(random)
map = map_gen.generate_map(MAP_WIDTH, MAP_HEIGHT, 1)
map_gen.run(map)

world = Level(MAP_WIDTH, MAP_HEIGHT, con)
tiler = TileGenerator()
tiler.run(world, map)

player = Entity(27, 22, '@', libtcod.white, con, world)
npc = Entity(56, 27, 'J', libtcod.yellow, con, world)
objects = [npc, player]

fov_map = libtcod.map_new(MAP_WIDTH, MAP_HEIGHT)
for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        libtcod.map_set_properties(
            fov_map, x, y,
            not world[x][y].block_sight, not world[x][y].blocked)

fov_recompute = True

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white)

    if fov_recompute:
        fov_recompute = False
        libtcod.map_compute_fov(
            fov_map, player.x, player.y,
            TORCH_RADIUS, FOV_LIGHT_WALLS, FOV_ALGO)

    render_all(fov_map)

    libtcod.console_flush()

    for object in objects:
        object.clear()

    if handle_keys():
        break

exit()
