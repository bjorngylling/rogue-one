import lib.libtcodpy as libtcod
from rogue_one.world import World
from rogue_one.map import Level
from rogue_one import system
from rogue_one import component
from rogue_one.generation.map_generation import TileGenerator
from rogue_one.generation.bsp_generation import BSPGenerator


def render_screen(con):
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_WIDTH = 70
MAP_HEIGHT = 46

random = libtcod.random_new()

libtcod.console_set_custom_font(
    'terminal12x12_gs_ro.png',
    libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)

libtcod.console_init_root(
    SCREEN_WIDTH, SCREEN_HEIGHT, 'rogue-one', False, libtcod.RENDERER_GLSL)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

map_gen = BSPGenerator(random)
generated_map = map_gen.generate_map(MAP_WIDTH, MAP_HEIGHT, 1)
map_gen.run(generated_map)

map = Level(MAP_WIDTH, MAP_HEIGHT, con)
tiler = TileGenerator()
tiler.run(map, generated_map)

fov_map = libtcod.map_new(MAP_WIDTH, MAP_HEIGHT)
for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        libtcod.map_set_properties(
            fov_map, x, y,
            not map[x][y].block_sight, not map[x][y].blocked)

world = World(random)
world.map = map

world.add_system(system.WorldRenderer(1, con))
world.add_system(system.UpdateFOV(0))
world.add_system(system.HandleInput(10))

world.create_entity([component.FieldOfView(fov_map), component.Player(),
                    component.Movement(), component.Position(5, 5),
                    component.Renderable("@")])

world.create_entity([component.Movement(), component.Position(5, 8),
                    component.Renderable("J", libtcod.yellow)])


step = 0
while not libtcod.console_is_window_closed():

    libtcod.console_flush()

    world.step()

    render_screen(con)

    print "Step %s" % (step)
    step += 1
