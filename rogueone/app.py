import tdl
import esper
import operator

from rogueone import components, processors

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
            components.Renderable("@"))
        self.world.add_processor(
            processors.RenderProcessor(self.renderer,
                                       self.player,
                                       self.map_sections))

    def generate_map(self):
        map_section = tdl.map.Map(80, 50)
        for x, y in map_section:
            map_section.transparent[x, y] = True
            map_section.walkable[x, y] = True
        self.map_sections = [map_section]

    def ev_QUIT(self, ev):
        raise SystemExit('The window has been closed.')

    def key_ESCAPE(self, ev):
        raise SystemExit('The window has been closed.')

    def ev_KEYDOWN(self, ev):
        if ev.keychar.upper() in MOVEMENT_OPS:
            pos = self.world.component_for_entity(self.player,
                                                  components.Position)
            dx, dy = MOVEMENT_OPS[ev.keychar.upper()]
            pos.x += dx
            pos.y += dy

    def update(self, dt):
        self.world.process()
        tdl.flush()
