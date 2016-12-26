import tdl
import esper
import operator

from rogueone import components, processors, constants

MOVEMENT_OPS = {
    'UP': (0, -1), 'DOWN': (0, 1),
    'LEFT': (-1, 0), 'RIGHT': (1, 0),
    'K': (0, -1), 'J': (0, 1),
    'H': (-1, 0), 'L': (1, 0)
}


class RogueOneApp(tdl.event.App):
    def __init__(self, renderer):
        super().__init__()
        self.renderer = renderer
        self.generate_map()
        self.setup_world()

    def setup_world(self):
        self.world = esper.World()
        self.player = self.world.create_entity(
            components.Position(1, 1),
            components.Velocity(),
            components.Renderable("@"))

        self.world.add_processor(
            processors.CollisionProcessor(self.player, self.map_sections),
            priority=100)
        self.world.add_processor(processors.MovementProcessor(), priority=90)
        self.world.add_processor(
            processors.RenderProcessor(self.renderer,
                                       self.player,
                                       self.map_sections), priority=0)

    def generate_map(self):
        map_section = Map(80, 50)
        for x, y in map_section:
            wall = False
            if ((x, y) in [(4, 4), (4, 5), (4, 6), (5, 7)]):
                wall = True
            map_section.transparent[x, y] = not wall
            map_section.walkable[x, y] = not wall
        self.map_sections = [map_section]

    def ev_QUIT(self, ev):
        raise SystemExit('The window has been closed.')

    def key_ESCAPE(self, ev):
        raise SystemExit('The window has been closed.')

    def ev_KEYDOWN(self, ev):
        if ev.keychar.upper() in MOVEMENT_OPS:
            vel = self.world.component_for_entity(self.player,
                                                  components.Velocity)
            dx, dy = MOVEMENT_OPS[ev.keychar.upper()]
            vel.dx += dx
            vel.dy += dy

    def update(self, dt):
        self.world.process()
        tdl.flush()


class Map(tdl.map.Map):
    def char_for_pos(self, x, y):
        if self.walkable[x, y]:
            return '.'
        else:
            return '#'

    def color_for_pos(self, x, y):
        if self.walkable[x, y]:
            return (constants.COLOR_FLOOR, constants.COLOR_BG)
        else:
            return (constants.COLOR_WALLS, constants.COLOR_BG)
